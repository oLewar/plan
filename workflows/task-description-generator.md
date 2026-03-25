---
description: Task Description Generator
---

## Purpose

This workflow generates a structured task description in the standardized format for the task board. It takes raw task information and transforms it into a well-organized, comprehensive task description that follows the project's template.

---

## Inputs Required From the User

Before running the workflow, the user must provide the following information:

1. **Task Title** (Required)
   - The name of the task
   - Should be concise and descriptive
   - Example: "Database Schema Refactoring", "Company Creation Form Component"

2. **Feature Description** (Required)
   - What is the task about?
   - What problem does it solve?
   - What are the main deliverables?
   - 2-3 bullet points or a short paragraph

3. **Proposed Solution** (Required)
   - How should this task be approached?
   - What are the key steps or phases?
   - Any technical approach or strategy?

4. **Where to Implement** (Required)
   - Which files, directories, or modules are affected?
   - Frontend, backend, database, or shared components?
   - Specific file paths if known

5. **Dependencies** (Required)
   - What other tasks must be completed first?
   - External libraries or tools needed?
   - Any prerequisites?

6. **Acceptance Criteria** (Required)
   - What defines "done"?
   - List of checkpoints or requirements
   - Testing requirements if applicable

7. **Additional Context** (Optional)
   - Related documentation
   - GitHub issues or tickets
   - Timeline estimates
   - Known issues or constraints
   - Data structures or examples

---

## Agent Responsibilities

- Organize user input into the standardized format
- Ensure all required sections are complete
- Ask clarifying questions if information is missing or unclear
- Format the output as valid Markdown
- Validate that acceptance criteria are measurable and clear
- Ensure dependencies are clearly stated

---

## Output

### Markdown Format

Generate a task description following this exact structure:

```markdown
### [Task Title]

### Feature Description

[Description of what the task is about]

- [Bullet point 1]
- [Bullet point 2]
- [Bullet point 3]

### Proposed Solution

[How to approach this task]

1. [Step 1]
2. [Step 2]
3. [Step 3]

### Where this feature should be implemented

- [Location 1]
- [Location 2]
- [Location 3]

### Dependencies

- [Dependency 1]
- [Dependency 2]
- [Dependency 3]

### Acceptance Criteria

- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

### Additional Context

**Related Documentation:**
- [Link/Reference 1]
- [Link/Reference 2]

**Current Issues:**
- [Issue 1]
- [Issue 2]

**Estimated Timeline:** [X days/weeks]
```

---

## Workflow Execution Steps

### 1. Gather Task Information (REQUIRED - Wait for User Input)

**STOP HERE AND ASK THE USER FOR THE FOLLOWING INFORMATION:**

Please provide the following details before proceeding:

**1. Task Title** (Required)
   - What is the name of this task?
   - Example: "Database Schema Refactoring"

**2. Feature Description** (Required)
   - What is this task about?
   - What problem does it solve?
   - What are the main deliverables?
   - Provide 2-3 bullet points or a short paragraph

**3. Proposed Solution** (Required)
   - How should this task be approached?
   - What are the key steps or phases?
   - Any technical approach or strategy?

**4. Where to Implement** (Required)
   - Which files, directories, or modules are affected?
   - Frontend, backend, database, or shared components?
   - Provide specific file paths if known

**5. Dependencies** (Required)
   - What other tasks must be completed first?
   - External libraries or tools needed?
   - Any prerequisites?

**6. Acceptance Criteria** (Required)
   - What defines "done"?
   - Provide a list of checkpoints or requirements
   - Include testing requirements if applicable

**7. Additional Context** (Optional but helpful)
   - Related documentation or links?
   - GitHub issues or ticket references?
   - Timeline estimates?
   - Known issues or constraints?
   - Data structures or code examples?

**WAIT FOR THE USER TO PROVIDE ALL REQUIRED ITEMS (1-6) BEFORE PROCEEDING TO STEP 2.**

Do not skip this step or proceed without user input.

### 2. Validate Input Completeness
// turbo
Review the provided information:

- [ ] Task Title is clear and descriptive
- [ ] Feature Description explains the problem and deliverables
- [ ] Proposed Solution outlines the approach with steps
- [ ] Implementation locations are specific and accurate
- [ ] Dependencies are clearly identified
- [ ] Acceptance Criteria are measurable and testable
- [ ] Additional Context provides helpful references

If any required section is missing or unclear, ask clarifying questions:
- Maximum of 3-5 follow-up questions
- Focus on completing missing information
- Ask for clarification if criteria are too vague

### 3. Organize Information into Structure
// turbo
Map the user's input to the standardized format:

1. **Task Title** → Use as-is
2. **Feature Description** → Organize into clear bullet points or paragraph
3. **Proposed Solution** → Structure as numbered steps or phases
4. **Where to Implement** → Format as bulleted file/directory paths
5. **Dependencies** → List as bulleted items
6. **Acceptance Criteria** → Format as checkboxes (- [ ])
7. **Additional Context** → Organize into subsections (Related Documentation, Current Issues, Timeline)

### 4. Generate Markdown Content
// turbo
Create the task description using the standardized format:

```markdown
### [Task Title]

### Feature Description

[Organized description with bullet points]

### Proposed Solution

[Structured approach with numbered steps]

### Where this feature should be implemented

[Bulleted list of locations]

### Dependencies

[Bulleted list of dependencies]

### Acceptance Criteria

[Checkboxes for each criterion]

### Additional Context

[Organized subsections with references and details]
```

### 5. Review and Validate Output
// turbo
Check the generated content:

- [ ] All required sections are present
- [ ] Formatting is consistent and clean
- [ ] Acceptance Criteria are measurable
- [ ] Dependencies are clear
- [ ] No missing information
- [ ] Markdown syntax is valid
- [ ] Content is well-organized and easy to read

### 6. Present Output to User
// turbo
Display the generated task description and ask for confirmation:

"Here is the generated task description. Please review and let me know if any changes are needed."

Provide the full Markdown output for the user to copy.

### 7. Make Revisions (if needed)
// turbo
If the user requests changes:

1. Ask which sections need modification
2. Request the updated information
3. Update the Markdown content
4. Present the revised version
5. Repeat until user is satisfied

### 8. Save to Task Board
// turbo
Once approved, save the task description to the appropriate location:

- Add to `docs/tow-registration-flow/TASK_BOARD.md` (or relevant task board file)
- Or create a new task board file if needed
- Format with proper Markdown separators (---)
- Ensure consistent formatting with existing tasks

---

## Best Practices

1. **Clarity First** - Ensure descriptions are clear and unambiguous
2. **Specificity** - Use concrete file paths and specific requirements
3. **Measurability** - Make acceptance criteria testable and verifiable
4. **Completeness** - Include all relevant context and dependencies
5. **Consistency** - Follow the standardized format exactly
6. **Validation** - Ensure all criteria are achievable and realistic

---

## Example Task Description

```markdown
### Database Schema Refactoring

### Feature Description

Clean up and refactor the Tow Company database schema to fix structural issues and add missing fields required for the registration flow.

- Remove duplicate foreign key from TowCompanyFacility table
- Create User ↔ Facility N:M junction table
- Add missing fields: taxId, status, isPrimaryContact

### Proposed Solution

Execute database migration in phases:
1. Create new junction table for User ↔ Facility N:M relationship
2. Migrate existing data from `TowCompanyUser.towCompanyFacilityId`
3. Remove duplicate `towCompanyFacilityLocationId` from TowCompanyFacility
4. Add new fields with appropriate defaults
5. Create unique constraint for isPrimaryContact per company

### Where this feature should be implemented

- Database: Prisma schema (`prisma/schema.prisma`)
- Migrations: `prisma/migrations/`
- Registry: `apps/backend/api/src/tow/company/company-registry.ts`

### Dependencies

- Prisma CLI for migrations
- PostgreSQL database
- Existing tow company data (must be migrated safely)

### Acceptance Criteria

- [ ] All migrations applied successfully without errors
- [ ] Prisma schema updated and validated
- [ ] No duplicate foreign keys in schema
- [ ] User ↔ Facility N:M relationship functional
- [ ] Existing tests pass without modification

### Additional Context

**Related Documentation:**
- Database schema review: `docs/tow-registration-flow/00-database-schema-review.md`

**Estimated Timeline:** 2-3 days
```

---

## Troubleshooting

**Issue: User provides vague acceptance criteria**
- Ask for specific, measurable criteria
- Example: Instead of "Works correctly", ask for "All migrations applied successfully without errors"

**Issue: Missing implementation locations**
- Ask for specific file paths or directories
- Provide examples from the codebase

**Issue: Unclear dependencies**
- Ask what must be completed before this task starts
- Ask what external tools or libraries are needed

**Issue: Incomplete feature description**
- Ask what problem this solves
- Ask what the deliverables are
- Ask for 2-3 key points

