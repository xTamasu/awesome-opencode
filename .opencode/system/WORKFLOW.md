# WORKFLOW.md

**End-to-End SDLC Workflow for the Multi-Agent Software Development System**

This document defines the complete, regulated software development workflow used by all agents in the system.
It governs the sequence of phases, role interactions, handoffs, and validation checkpoints from initial requirement to final quality assurance.

The workflow ensures:

* predictable execution
* strict responsibility separation
* structured phase progression
* deterministic outputs
* Skills-driven specialization
* memory-first consistency
* safe collaboration between agents

---

# 1. Overview of the Development Workflow

The workflow follows a strict SDLC sequence:

```
User Request
↓
Planning Phase
↓
Design Phase
↓
Implementation Phase
↓
Deployment Phase
↓
QA Phase
↓
Completion & Review
```

Only the Project Manager may open or close phases.
All agents must follow the Workflow Rules defined in AGENTS.md.

---

# 2. Core Principles of the Workflow

### 2.1 Phase Discipline

No agent may enter a phase unless the Project Manager opens it.
No work may advance until the previous phase's exit criteria are met.

### 2.2 Structured Outputs

Each phase produces strict, deterministic deliverables used by the next phase.

### 2.3 Task-Driven Execution

Execution-phase agents never work without a formally issued AgentTask.

### 2.4 Skills-Based Expertise

Agents load Skills only when required to complete a task and never make assumptions.

### 2.5 Memory-First

Before reading Skills and before executing work, agents must:

1. search memory
2. apply relevant patterns
3. validate against historical context

### 2.6 Escalation

Any ambiguity, missing input, unclear criteria, or violation of phase boundaries must be escalated to the Project Manager.

---

# 3. Phase Breakdown

The workflow consists of five major phases:

1. **Planning**
2. **Design**
3. **Implementation**
4. **Deployment**
5. **Quality Assurance**

Each phase has:

* purpose
* allowed roles
* required inputs
* required outputs
* exit criteria
* escalation triggers

---

# 4. Planning Phase

## 4.1 Purpose

Transform the user’s initial request into structured, validated, implementable work.

## 4.2 Allowed Roles

* Project Manager
* Product Manager
* Requirements Engineer

## 4.3 Required Inputs

* User request
* Existing memory patterns
* Existing Skills (if required for clarification)

## 4.4 Activities

1. Requirements collection
2. Refinement and clarification
3. Validation with stakeholders
4. Creation of:
    * **backlog items** – created by the *Requirements Engineer*
    * **user stories** – written by the *Product Manager*
    * **acceptance criteria** – defined by the *Product Manager*
5. Risk analysis
6. Prioritization
7. Generation of **initial Planning AgentTasks** (if needed)

## 4.5 Outputs

* Backlog entries
* Structured user stories
* Acceptance criteria
* Requirement specifications

## 4.6 Exit Criteria

* All user stories validated
* Acceptance criteria defined
* Requirements complete, unambiguous, traceable
* Ambiguities resolved
* Approved by Project Manager

---

# 5. Design Phase

## 5.1 Purpose

Convert validated requirements into architecture, technical design, and UX specifications.

## 5.2 Allowed Roles

* Architect
* Designer
* Database Engineer

## 5.3 Required Inputs

* Backlog + User Stories
* Acceptance Criteria
* Requirement documentation
* Architecture and design Skills
* Memory patterns

## 5.4 Activities

1. Architecture modeling
2. API definition
3. DB schema modeling
4. UX/UI design
5. System constraints definition
6. Producing **Design AgentTasks** for implementation agents

## 5.5 Outputs

* Architecture specification
* UX design documents
* DB schema specification
* Interface contracts
* Technical design documentation
* Implementation AgentTasks

## 5.6 Exit Criteria

* Architecture consistent and feasible
* UX validated
* Schema approved
* All design docs complete
* All relevant implementation tasks created
* Approved by Project Manager

---

# 6. Implementation Phase

## 6.1 Purpose

Transform designs and specifications into working code, tests, and documentation.

## 6.2 Allowed Roles

* Developer
* AI Engineer
* System Engineer

## 6.3 Required Inputs

* Implementation AgentTasks
* Architecture documents
* UX design
* DB schema
* Required Skills (C#, React, API Design, Testing, etc.)
* Memory patterns

## 6.4 Activities

1. Load relevant Skills
2. Follow established Memory patterns
3. Implement code according to design
4. Write unit + integration tests
5. Validate against acceptance criteria
6. Produce technical documentation (if required)
7. Produce completion summary
8. Update memory (if required)

## 6.5 Outputs

* Code
* Tests
* Documentation
* Memory updates (if applicable)
* Completion summary

## 6.6 Exit Criteria

* All acceptance criteria fulfilled
* All required tests implemented and validated
* Code follows patterns + Skills
* Memory updated if new patterns discovered
* Approved by Project Manager

---

# 7. Deployment Phase

## 7.1 Purpose

Package, configure, and deploy the implemented software.

## 7.2 Allowed Roles

* DevOps Engineer
* Security Engineer

## 7.3 Required Inputs

* Completed implementation deliverables
* Deployment Skills (CI/CD, Bicep, IaC, cloud operations)
* Memory related to infrastructure

## 7.4 Activities

1. Build and release pipelines
2. Infrastructure-as-Code
3. Environment configuration
4. Security validation
5. Deployment AgentTasks execution

## 7.5 Outputs

* Deployable artifacts
* Configurations
* IaC templates
* Deployment documentation

## 7.6 Exit Criteria

* Successful deployment to the required environment
* No blocking security issues
* Documentation complete
* Approved by Project Manager

---

# 8. QA Phase

## 8.1 Purpose

Validate correctness, stability, and functional behavior of the delivered software.

## 8.2 Allowed Roles

* QA Engineer
* Tester
* User (black-box)

## 8.3 Required Inputs

* Deployment artifacts
* Acceptance criteria
* Requirements
* Memory bug patterns
* Testing and QA Skills

## 8.4 Activities

1. Test plan creation
2. Execution of:

   * unit tests
   * integration tests
   * system tests
   * regression tests
3. Bug detection
4. Creation of bug AgentTasks
5. User acceptance testing

## 8.5 Outputs

* Test reports
* QA documentation
* Bug tickets
* Acceptance decision

## 8.6 Exit Criteria

* All defined acceptance criteria satisfied
* All tests passed or documented
* No unresolved high-severity issues
* Approved by Project Manager

---

# 9. Cross-Phase Handoff Contracts

Every phase transition must meet its **exit criteria** and produce required deliverables.

Examples:

**Planning → Design**

* Requirements validated
* AC complete
* Stories approved

**Design → Implementation**

* Architecture and UX ready
* All Implementation AgentTasks created

**Implementation → Deployment**

* Code + tests complete
* All acceptance criteria met

**Deployment → QA**

* Deployed artifacts stable
* Configurations documented

**QA → Completion**

* All tests passed
* All open issues addressed

No agent may proceed without explicit PM approval.

---

# 10. Escalation Workflow

Agents must escalate to the Project Manager when:

* any required input is missing
* acceptance criteria are incomplete
* ambiguity is detected
* design conflicts exist
* tasks exceed allowed scope
* skills required are missing
* memory references do not resolve
* phase is not open

Escalation halts workflow until resolved.

---

# 11. Integration of Skills and Memory into the Workflow

## 11.1 Skill Usage

Agents load Skills only **when executing a task** (never preloaded).
Skills govern how work is done.

## 11.2 Memory Usage

Memory is consulted **before** skill-loading to reuse past solutions.

Workflow order:

```
Receive AgentTask
↓
Verify Inputs
↓
Search Memory
↓
Load Relevant Skills
↓
Execute
↓
Validate
↓
Create Summary
↓
Optional: Update Memory
```

---

# 12. Summary

This workflow ensures:

* strict control over agent behavior
* predictable SDLC progression
* complete separation of responsibilities
* reliable task delegation
* robust error handling
* consistent use of Skills and Memory
* clear, auditable transitions between phases

This document forms the backbone of the entire development process.
