# AGENTTASKS.md

**AgentTask Specification, Structure, Lifecycle, and Complexity Model**

This document defines the AgentTask subsystem used by all agents in the multi-agent software development environment.
AgentTasks are the primary mechanism for planning, delegating, and executing work across the SDLC.

AgentTasks convert:

* user intent
* requirements
* designs
* architecture
* quality expectations
* skills
* memory references

into structured, executable units of work handled by specialist agents.

---

# 1. Purpose of AgentTasks

AgentTasks ensure:

* predictable execution
* deterministic structure
* role-aligned delegation
* complete context for implementation
* traceable decisions
* decoupling between planning and execution
* standardized cross-agent communication

AgentTasks act as the **contract** between phases and roles.

---

# 2. Ownership of AgentTasks

Only the following agents may **create** AgentTasks:

* Project Manager (primary owner)
* Product Manager
* Requirements Engineer
* Architect
* Designer
* Database Engineer

These agents belong to the Planning and Design phases and create tasks for execution roles.

All other agents may **execute** AgentTasks but are prohibited from creating new ones unless explicitly instructed.

---

# 3. AgentTask Structure (Canonical Schema)

Every AgentTask must follow this exact format:

```
id: "AUTO-GENERATED"
title: "<Role> | <Brief description>"

phase: "<planning | design | implementation | deployment | qa>"
assigned_to: "<Agent role>"
created_by: "<Agent role>"
created_at: "<Timestamp ISO8601>"

goal:
  summary: "High-level description of what this task must accomplish."
  objectives:
    - "Specific objective #1"
    - "Specific objective #2"
  success_criteria:
    - "Measurable condition #1"
    - "Measurable condition #2"

why:
  business_value: "Why this task exists."
  user_impact: "How this impacts end users."
  risk_if_skipped: "What happens if this is not done."

context:
  description: "Relevant background needed to understand the task."
  domain_information: |
    "Domain knowledge, assumptions, stakeholders, known constraints."
  extracted_requirements: |
    "Requirements from Planning or Design phase."
  architectural_references: |
    "References to architecture documentation if relevant."
  design_references: |
    "References to UX/UI or system design if relevant."
  memory_references: |
    "Links to memory system entries."
  skills_required:
    - "<Skill Name 1>"
    - "<Skill Name 2>"
  patterns_examples: |
    "Examples from patterns folders, if applicable."
  constraints: |
    "Non-functional constraints, compatibility requirements, etc."

implementation:
  approach: |
    "High-level plan or approved implementation pattern."
  steps:
    - "Step 1"
    - "Step 2"
    - "Step 3"
  technical_notes: |
    "Important notes, warnings, performance considerations."

validation:
  required_tests:
    - "Test case #1"
    - "Test case #2"
  acceptance_criteria:
    - "Acceptance criteria #1"
    - "Acceptance criteria #2"
  manual_validation:
    - "Checklist item #1"
    - "Checklist item #2"

deliverables:
  output_files:
    - "path/to/file1"
    - "path/to/file2"
  documentation:
    - "path/to/doc"
  summary_required: true

completion:
  reporting:
    summary_format: |
      "Structure of completion summary expected from agent."
    store_memory:
      required: true
      category: "Learning or Pattern"
```

This structure is mandatory.

---

# 4. AgentTask Lifecycle

AgentTasks follow a controlled, five-stage lifecycle:

## 4.1 Creation

Only planning/design-phase agents generate tasks.
The task must contain full context.
No execution may begin until the Project Manager approves it.

## 4.2 Assignment

Each AgentTask must be assigned to exactly one agent role.

Example:

```
assigned_to: "Developer"
```

## 4.3 Execution

The receiving agent:

1. verifies inputs
2. loads required Skills
3. consults memory
4. follows task structure exactly
5. produces deterministic deliverables

Execution agents must not modify the task.

## 4.4 Validation

The executing agent self-validates deliverables using:

* test requirements
* acceptance criteria
* skill validation rules
* memory-pattern compliance

If validation fails → escalate to Project Manager.

## 4.5 Completion

The executing agent produces:

* deliverables
* completion summary
* memory entry (if required)

Then notifies the Project Manager.

---

# 5. Task Types

AgentTasks fall into five categories, aligned with SDLC phases:

## 5.1 Planning Tasks

Produced by PM, Product Manager, Requirements Engineer.

Examples:

* refine requirements
* create user stories
* define acceptance criteria

## 5.2 Design Tasks

Produced by Designer, Architect, Database Engineer.

Examples:

* create architecture spec
* produce UI design
* define DB schema

## 5.3 Implementation Tasks

Produced by PM / Architect / Designer.

Examples:

* implement feature
* create endpoints
* write tests
* build UI component

## 5.4 Deployment Tasks

Produced by Architect / PM.

Examples:

* create CI/CD pipeline
* define IaC
* configure environments

## 5.5 QA Tasks

Produced by PM / QA Engineer.

Examples:

* write QA test plan
* perform integration tests
* user acceptance testing

---

# 6. Complexity Model

The complexity scoring system determines the size, risk, and expected workload of an AgentTask.

This system ensures tasks are:

* sized consistently
* properly delegated
* broken down when too large
* planned based on realistic complexity

## 6.1 Complexity Tiers

| Tier       | Points | Description          | Examples                          |
| ---------- | ------ | -------------------- | --------------------------------- |
| **Nano**   | 0–2    | trivial, single-file | fix typo, adjust config           |
| **Tiny**   | 3–5    | small scope          | add validation, add missing field |
| **Small**  | 6–10   | multi-file           | small feature, one endpoint       |
| **Medium** | 11–20  | multi-module         | auth integration, UI page         |
| **Large**  | 21–30  | cross-system         | payment flow, full UI section     |
| **Mega**   | 31+    | system-wide          | entire subsystem, refactor        |

**Large & Mega tasks must be split into multiple smaller tasks.**

---

## 6.2 Complexity Calculation

Tasks are scored using the following dimensions:

### 1. File Impact (0–10)

```
1 file: 0 pts  
2–5 files: 2 pts  
6–10 files: 5 pts  
10+ files: 10 pts  
```

### 2. Code Volume (0–10)

```
<50 lines: 0 pts  
50–200 lines: 3 pts  
200–500 lines: 6 pts  
500+ lines: 10 pts  
```

### 3. External Integrations (0–5)

APIs, third-party libraries, cloud services.

### 4. Security Implications (0–3)

Authentication, authorization, sensitive data.

### 5. Coordination Required (0–2)

Cross-agent or cross-phase work.

Total = sum of all dimension points.

---

# 7. Required Validations Before Execution

Agents must not execute an AgentTask unless:

* the phase is open
* required Skills are available
* all required inputs are present
* acceptance criteria are defined
* success criteria are measurable
* design/architecture references exist (if needed)
* memory references resolve
* the assigned role matches the recipient agent

If any check fails → agent must escalate.

---

# 8. Completion Summary Format

Every AgentTask must end with a structured completion summary.

```
# Completion Summary

## Status
Completed / Blocked / Requires Clarification

## Deliverables
- file1
- file2
- documentation

## Skills Used
- <Skill 1>
- <Skill 2>

## Implementation Notes
Concise description of decisions made.

## Validation Performed
- tests executed
- acceptance criteria verified
- manual checks completed

## Memory Update
- created: memory/Pattern/xyz.md
- updated: memory/Learning/abc.md

## Next Steps
If applicable.
```

Summaries must be deterministic and follow this format exactly.

---

# 9. Rules for Execution Agents

Execution agents (Developer, AI Engineer, etc.) must:

* follow the task exactly as written
* load and apply all required Skills
* follow validation criteria
* produce deliverables without deviation
* escalate missing information
* never modify the AgentTask

Execution agents may not:

* create new AgentTasks
* redefine acceptance criteria
* adjust scope
* invent missing requirements
* bypass Skills or Memory

---

# 10. AgentTask File Location

All tasks are written to:

```
agenttasks/
  TASK-<id>-<role>-<shortname>.md
```

Stories (mega tasks) go to:

```
stories/
  STORY-<id>-<shortname>.md
```

---

# 11. Summary

This specification ensures:

* predictable delegation
* consistent work quality
* alignment across roles
* strict separation of responsibilities
* scalable multi-agent coordination
* safe future expansion

AgentTasks are the backbone of the entire system, bridging planning, design, implementation, deployment, and QA through structured, skill-driven, phase-aligned work.
