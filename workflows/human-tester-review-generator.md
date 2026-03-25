---
description: Human Tester Review Generator
---

## Purpose

This workflow reviews all changes introduced in the current branch by comparing it with the main branch and generates a **human-readable testing guide** for a **non-technical tester**.  
The goal is to explain *what needs to be checked and how to check it* from a user perspective, without requiring any technical knowledge.

---

## Inputs Required From the User

Before running the workflow, the user must provide the following information:

1. **Task description**  
   - Taken from Jira, Trello, GitHub Projects, or a similar system  
   - Describes the purpose of the change in business or product terms

2. **Additional context**  
   - Any details discussed verbally or in meetings  
   - Information that was not written in the original task description

3. **Optional notes**  
   - Edge cases  
   - Known limitations  
   - Areas that require extra attention during testing

---

## Agent Responsibilities

- Analyze **all differences between the feature branch and the main branch**
- Understand changes from a **high-level (“eagle view”)**, focusing on visible behavior and user impact
- Ignore internal implementation details unless they directly affect what the user sees
- Ask clarifying questions when needed:
  - Maximum of **5–10 questions**
  - Only ask questions that help produce clearer testing instructions

---

## Output

### Markdown File

- Generate **one Markdown file**
- The **file name must exactly match the branch name**
- The file must contain clear, structured testing instructions

---

## Target Audience

- The tester is **not a technical person**
- Do **not** include:
  - Code-level explanations
  - Technical architecture
  - Method, class, schema, or API descriptions
- Use simple, clear language focused on user actions and visible results

---

## Content Guidelines

The generated Markdown file should include:

- Step-by-step testing instructions
- Clear headings and bullet points
- Short, easy-to-understand sentences

For each change, clearly describe:

- Which **portal or application** to open (e.g., Admin Portal, User Portal)
- Which **pages or sections** to navigate to
- What **actions** the tester should perform:
  - Clicking buttons
  - Filling forms
  - Submitting data
- What should be **checked or verified**:
  - Page loads correctly
  - UI elements are visible and usable
  - Forms behave as expected
  - Correct messages appear
- What the **expected result** is

---

## Writing Style Rules

- Focus on *what the tester does* and *what they should see*
- Avoid technical terminology
- Add small explanatory notes when they help understanding
- Be specific enough that the tester can follow the steps without asking questions

---

## Key Principles

- Think like a product tester, not a developer
- Describe behavior, not implementation
- Prioritize clarity and usability over technical completeness
- Assume zero technical background

---

## Workflow Execution Steps

### 1. Gather Initial Information (REQUIRED - Wait for User Input)

**STOP HERE AND ASK THE USER FOR THE FOLLOWING INFORMATION:**

Please provide the following details before proceeding:

**1. Task Description** (Required)
   - Copy the task description from your project management system (Jira, Trello, GitHub Projects, etc.)
   - What is the feature or change about?
   - What problem does it solve?

**2. Additional Context** (Required)
   - Any details discussed in meetings or conversations that weren't in the task description?
   - Any specific requirements or decisions made?
   - Any constraints or dependencies?

**3. Optional Notes** (Optional but helpful)
   - Edge cases to test?
   - Known limitations?
   - Areas that need extra attention?
   - Specific user roles or permissions involved?

**WAIT FOR THE USER TO PROVIDE ALL THREE ITEMS BEFORE PROCEEDING TO STEP 2.**

Do not skip this step or proceed without user input.

### 2. Analyze Branch Changes
// turbo
Run the following command to see all changes in the current branch compared to main:
```bash
git diff main...HEAD --name-only
```

Then review the actual changes:
```bash
git diff main...HEAD
```

Focus on understanding:
- Which **pages/portals** are affected
- What **UI elements** changed (buttons, forms, modals, etc.)
- What **user actions** are now possible or changed
- What **validations or behaviors** changed

### 3. Ask Clarifying Questions (if needed)
// turbo
If the changes are unclear or you need more context, ask the user targeted questions:
- Which portal(s) should the tester use?
- Are there specific user roles or permissions needed?
- Should the tester test with real data or test data?
- Are there any environment-specific considerations?
- What are the success criteria?

Keep questions to a maximum of 5-10 and focus on what helps create better testing instructions.

### 4. Map Changes to User Actions
// turbo
Create a mental map of:
- **Portal/Application** → which system to open
- **Navigation path** → which pages/sections to visit
- **User actions** → what buttons to click, forms to fill
- **Expected results** → what should happen after each action
- **Verification points** → what to check to confirm it works

### 5. Generate Markdown File
// turbo
Create a new Markdown file named exactly after the branch name with the following structure:

```markdown
# Testing Guide: [Feature Name]

## Overview
[Brief explanation of what changed and why, in simple terms]

## Prerequisites
- Which portal to use
- Any required permissions or roles
- Test data needed (if any)

## Test Scenarios

### Scenario 1: [User Action/Feature]
**Steps:**
1. Open [Portal Name]
2. Navigate to [Page/Section]
3. [Action to perform]
4. [Expected result]

**Verification:**
- [ ] [What to check]
- [ ] [What to check]

### Scenario 2: [Next User Action/Feature]
[Repeat structure]

## Edge Cases / Special Considerations
- [Any edge cases or special scenarios]
- [Known limitations if any]

## Notes
- [Any additional information helpful for the tester]
```

### 6. Save the File
// turbo
Save the generated Markdown file to the repository root or a designated testing folder with the exact branch name as the filename.

Example: If the branch is `1442-add-phone-number-icon`, the file should be:
```
1442-add-phone-number-icon.md
```

### 7. Deliver to Tester
// turbo
Share the generated file with the tester along with:
- Link to the test environment
- Any credentials needed
- Expected timeline for testing
- How to report issues
