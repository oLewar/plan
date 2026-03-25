---
description: Migrate old module from controller-based pattern to new registry/service architecture
---

# Migrate Old Module to New Architecture

This workflow guides you through migrating any old module from the controller-based pattern to the new modular architecture pattern. Replace `{MODULE}` and `{module}` with your actual module name (e.g., `auth`, `user`, `company`).

## Overview

The new architecture follows a vertical slice pattern with clear separation of concerns:
- **Registry**: Database operations only
- **Handlers**: Business logic coordination
- **Service**: RPC endpoints and validation
- **Controller**: Express route handlers
- **Router**: Route definitions
- **Errors**: Domain-specific error types
- **Schema**: Request/response validation schemas
- **Validators**: Input validation using AJV

## Current Status

✅ **Already Implemented** (New Architecture):
- `/apps/backend/api/src/{domain}/{module}/{module}-schema.ts` - Request/response schemas
- `/apps/backend/api/src/{domain}/{module}/{module}-errors.ts` - Error types and handling
- `/apps/backend/api/src/{domain}/{module}/{module}-registry.ts` - Database operations
- `/apps/backend/api/src/{domain}/{module}/{module}-validators.ts` - Input validation
- `/apps/backend/api/src/{domain}/{module}/{module}-service.ts` - RPC endpoints
- `/apps/backend/api/src/{domain}/{module}/{module}-controller.ts` - Express handlers
- `/apps/backend/api/src/{domain}/{module}/{module}-routers.ts` - Route definitions
- New router integrated into `/apps/backend/api/src/index.ts`

⚠️ **Still Active** (Old Architecture):
- `/apps/backend/api/src/controllers/{domain}/{module}.ts` - Old implementation (DO NOT DELETE YET)
- `/routes/{domain}/{module}.ts` - Old route definitions (may still be in use)

## Migration Steps

### Step 1: Verify New Implementation Works
1. Run the application: `npm run dev`
2. Test all endpoints for the module
3. Verify all endpoints return expected responses
4. Check error handling and validation

### Step 2: Update Frontend to Use New Endpoints
If frontend is using the old endpoints, update API calls to use new routes:
- Routes should remain the same (only backend implementation changes)
- Verify API contract is maintained

Note: Routes are the same, but backend implementation is now modular.

### Step 3: Verify Old Routes Are No Longer Used
1. Check `/routes/{domain}/{module}.ts` to see if it's still registered in `index.ts`
2. Search codebase for any direct imports of `/controllers/{domain}/{module}.ts`
3. Confirm no other code is calling the old controller directly
4. Use: `grep -r "controllers/{domain}/{module}" /apps/backend/api/src`

### Step 4: Remove Old Implementation
Once verified that new implementation works and old is not used:

1. **Delete old controller file**:
   ```bash
   rm /apps/backend/api/src/controllers/{domain}/{module}.ts
   ```

2. **Remove old route file** (if separate):
   ```bash
   rm /routes/{domain}/{module}.ts
   ```

3. **Remove old route registration from index.ts**:
   - Find and remove: `import { {module}Router } from '@routes/{domain}/{module}';`
   - Find and remove the router from `app.use()` call

4. **Verify no broken imports**:
   - Run: `npm run build`
   - Check for any compilation errors related to removed files

### Step 5: Test Complete Flow
1. Run full test suite: `npm run test`
2. Run E2E tests: `npm run e2e`
3. Verify all module flows work end-to-end

### Step 6: Update Documentation
1. Update architecture documentation to reference new module implementation
2. Document the new pattern for future features in this module
3. Add this as a reference implementation for other modules

## Key Differences: Old vs New

### Old Pattern (Controller-based)
```
Controller ({module}.ts)
├── Direct Prisma queries
├── Business logic mixed with HTTP handling
├── Manual error handling
└── No validation schema
```

### New Pattern (Registry/Service)
```
Router ({module}-routers.ts)
└── Controller ({module}-controller.ts)
    └── Service ({module}-service.ts)
        ├── Validators ({module}-validators.ts)
        └── Registry ({module}-registry.ts)
            └── Prisma (Database)
```

## Benefits of New Architecture

1. **Separation of Concerns**: Each layer has a single responsibility
2. **Testability**: Each layer can be tested independently
3. **Reusability**: Registry functions can be used by multiple services
4. **Consistency**: Follows same pattern as other modules (user, company, etc.)
5. **Maintainability**: Clear data flow and error handling
6. **Scalability**: Easy to add new endpoints or features

## Troubleshooting

### Issue: "Cannot find module '@{domain}/{module}/{module}-routers'"
- **Solution**: Ensure all new files are created in `/apps/backend/api/src/{domain}/{module}/`
- Check that `tsconfig.json` has correct path aliases

### Issue: "Old routes still being called"
- **Solution**: Search for all imports of old controller
- Remove from `index.ts` and any other files
- Verify new router is registered in `app.use()`

### Issue: "Validation errors on new endpoints"
- **Solution**: Check request body matches schema definitions in `{module}-schema.ts`
- Verify all required fields are present and types match

## Rollback Plan

If issues occur with new implementation:

1. Keep old controller file until fully tested
2. Register both old and new routers temporarily
3. Route traffic to old implementation while debugging new one
4. Once new is verified, remove old routes

## Schema Refactoring Best Practices

### Breaking Down Monolithic Schemas
When refactoring a module with a large monolithic schema object:

1. **Extract Individual Schemas**:
   - Break down into separate constants: `<functionName>ParamsSchema`, `<functionName>ResSchema`
   - Use camelCase for schema names
   - Auto-generated types will be PascalCase: `<FunctionName>ParamsSchema`

2. **Enum Field Handling**:
   - Define as: `status: { type: 'string', enum: Object.values(StatusEnum) }`
   - Database returns enums as strings - this is correct
   - No type casting needed for enum itself (schema already defines as string)
   - Cast JSON objects: `pickUpAvailableHours: serializedFacility.pickUpAvailableHours as unknown as FacilityPickUpAvailableHoursSchema`

3. **Service Layer Pattern**:
   - Accept complete params objects: `params: GetFunctionParamsSchema`
   - Do NOT destructure in function signature
   - Destructure inside function body: `const { fieldName } = params;`
   - Pass entire params object to registry
   - Use `@argValidate` and `@resValidate` decorators
   - Remove manual validation calls when using decorators
   - No `@client` decorator for internal services

4. **Registry Layer Pattern**:
   - Accept params objects: `params: GetFunctionParamsSchema`
   - Destructure internally to extract individual fields
   - Use `serialize()` for database objects before returning
   - Check for null values before serializing optional fields
   - Use proper schema types for responses (not inline objects)
   - Apply type casting for enum and JSON fields in return statements

5. **Type Safety Rules**:
   - NEVER use `any` - always use proper generated schema types
   - All parameter types must be specific schema types
   - JSON fields need `as unknown as SchemaType` casting
   - Enum fields need `as EnumType` casting

### Example: Status Field Handling
```typescript
// Schema definition (correct pattern used across all modules)
status: { type: 'string', enum: Object.values(TowFacilityStatusEnum) }

// Registry return (with proper casting)
return right({
  ...serializedFacility,
  status: serializedFacility.status as TowFacilityStatusEnum,
  pickUpAvailableHours: serializedFacility.pickUpAvailableHours as unknown as FacilityPickUpAvailableHoursSchema,
});
```

## Testing & Verification Checklist

### Phase 1: Internal Module Validation
- [ ] **Service Method Signatures**: Verify all service methods accept params as objects, not individual arguments
- [ ] **Registry Return Types**: Confirm registry methods return proper schema types (not inline objects)
- [ ] **Decorator Alignment**: Ensure `@argValidate` and `@resValidate` decorators match actual schema names
- [ ] **Import Cleanup**: Remove unused imports after schema refactoring
- [ ] **Type Casting**: Verify enum and JSON fields have proper type casting in return statements

### Phase 2: External Usage Discovery & Fixing
**CRITICAL STEP - Do NOT skip this**

1. **Search for all external usages**:
   ```bash
   grep -r "serviceName\." /apps/backend/api/src --include="*.ts" | grep -v "/{module}/"
   ```

2. **For each external usage found**:
   - Verify it's calling a refactored method
   - Check if it's passing arguments correctly
   - If method signature changed (e.g., from `methodName(id)` to `methodName({ id })`), update the call

3. **Common patterns to fix**:
   - Single argument calls: `getTowCompanyFacilityById(facilityId)` → `getTowCompanyFacilityById({ facilityId })`
   - Conditional calls: `facilityId ? service.method(facilityId) : null` → `facilityId ? service.method({ facilityId }) : null`
   - Array map calls: `.map(id => service.method(id))` → `.map(id => service.method({ id }))`

### Phase 3: Admin/Wrapper Service Validation
- [ ] **Return Type Matching**: Admin service return types MUST match underlying service return types exactly
- [ ] **Import Correctness**: Verify admin service imports the correct schema types
- [ ] **Parameter Passing**: Confirm admin service passes complete params objects to underlying service

### Phase 4: TypeScript Compilation
- [ ] **Run TypeScript compiler**: `npm run build` or `tsc --noEmit`
- [ ] **Fix all type errors**: Address any type mismatches found
- [ ] **Verify no `any` types**: Search for `any` in refactored files and replace with proper types

### Phase 5: Runtime Testing
- [ ] **Unit Tests**: Run tests for refactored module
- [ ] **Integration Tests**: Test interactions with other modules
- [ ] **E2E Tests**: Test complete user flows
- [ ] **Error Handling**: Verify error cases work correctly

### Phase 6: Documentation & Handoff
- [ ] **Update Architecture Docs**: Reference new module implementation
- [ ] **Document Patterns**: Add this as reference implementation for other modules
- [ ] **Create Examples**: Document common patterns used in this module

### Phase 7: Final TypeScript Type Check
**FINAL VERIFICATION - Run before considering refactoring complete**

1. **Run TypeScript compiler in strict mode**:
   ```bash
   npx tsc --noEmit --strict
   ```

2. **Verify no errors in refactored module**:
   - Check for any type mismatches
   - Ensure all `any` types have been replaced
   - Confirm all imports are correct

3. **Check specific areas**:
   - Service method signatures match registry signatures
   - Admin service return types match underlying service return types
   - All external callers pass correct parameter shapes
   - Decorators align with actual schema names and return types

4. **If errors found**:
   - Fix type mismatches immediately
   - Re-run TypeScript compiler
   - Repeat until no errors remain

5. **Success criteria**:
   - ✅ Zero TypeScript errors in refactored module
   - ✅ All external usages compile without errors
   - ✅ Admin/wrapper services have correct types
   - ✅ No `any` types in refactored code

## Notes

- New implementation maintains same API contract as old
- Error handling is improved with proper status codes
- Validation is now centralized and consistent
- Future features in this module should follow this same pattern
- Registry layer is reusable by multiple services if needed
- Service layer can be extended with RPC decorators for cross-service communication
- Schema refactoring enables proper type safety and decorator-based validation
- All modules (auction, billing, tow, etc.) follow the same enum and JSON serialization patterns
