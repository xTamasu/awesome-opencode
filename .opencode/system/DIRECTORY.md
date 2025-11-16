# DIRECTORY.md

**Repository Structure Specification for the Multi-Agent Software Development System**

This document defines the full directory hierarchy, purpose, and governance rules for all project files used by the multi-agent development system.
It ensures structural consistency, discoverability, and predictable behavior across phases, roles, memory, tasks, and skills.

This directory layout is mandatory for all agents.

---

# 1. Top-Level Layout (Overview)

```
/
├── AGENTS.md                    # Global governance for all agents
├── .opencode/
│   ├── agent/                   # Individual agent definitions
│   ├── system/                  # System-level specifications
│   ├── agenttasks-templates/    # Task templates
│   ├── agenttasks/              # All generated AgentTasks
│   ├── memory/                  # Project memory folders
│   └── skills/                  # Domain-specific skills
└── src/                         # Source code (app logic)
```

Everything under `.opencode/` is part of the **agent operating system**.
Everything outside is application code or external docs.

---

# 2. `.opencode/` — Multi-Agent Operating System Root

This folder contains all files and directories required to govern agents, tasks, memory, workflow, and skills.

```
.opencode/
├── agent/
├── system/
├── agenttasks-templates/
├── agenttasks/
├── memory/
└── skills/
```

Each section is described below.

---

# 3. `AGENTS.md` (root-level)

```
/AGENTS.md
```

This file defines:

* global rules
* behavior contracts
* SDLC phase boundaries
* skill usage policies
* escalation rules
* cross-role separation

It is the **constitution** for the entire agent system.

Every agent references this file implicitly.

---

# 4. `.opencode/agent/` — Agent Role Definitions

```
.opencode/agents/
  project-manager.md
  product-manager.md
  requirements-engineer.md
  designer.md
  architect.md
  database-engineer.md
  developer.md
  ai-engineer.md
  system-engineer.md
  devops-engineer.md
  security-engineer.md
  qa-engineer.md
  tester.md
  user.md
```

Each agent file follows the structure defined in AGENTS.md:

1. Identity
2. Mission
3. Responsibilities
4. Limits
5. Required Inputs
6. Required Outputs
7. Workflow / Behavior
8. Escalation Rules
9. Required Skills
10. Phase

Agents must not exist outside this folder.

---

# 5. `.opencode/system/` — System Specifications

```
.opencode/system/
  AGENTTASKS.md      # AgentTask schema, types, lifecycle, complexity
  MEMORY.md          # Memory rules, storage, retrieval, update
  SKILLS.md          # Skills system, structure, usage, versioning
  WORKFLOW.md        # End-to-end SDLC process used by all agents
```

These documents define the global systems that agents rely on.
They do not contain agent-specific rules — those belong in agent definitions.

---

# 6. `.opencode/agenttasks-templates/` — Task Templates

```
.opencode/agenttasks-templates/
  tiny-task-template.yaml
  small-task-template.yaml
  medium-task-template.yaml
  large-task-template.yaml
  user-story-template.yaml
  bug-task-template.yaml
```

Templates are referenced by:

* Project Manager
* Product Manager
* Requirements Engineer
* Architect
* Designer

They generate AgentTasks that follow **AGENTTASKS.md**.

Execution agents must never modify templates.

---

# 7. `.opencode/agenttasks/` — Generated Tasks and Stories

This folder holds all actual AgentTasks created during the SDLC.

```
.opencode/agenttasks/
  features/
    FEATURE-001-authentication/
      index.md                       # High-level feature description
      user-stories/
        US-001-login-flow.md
        US-002-refresh-token.md
      tasks/
        TASK-123-developer-login-endpoint.md
        TASK-124-tester-login-cases.md
```

### Structure Breakdown

```
features/
  <feature>/
    index.md
    user-stories/
    tasks/
```

**Features**: large, multi-scope objectives (formerly “stories”).
**User Stories**: written by Product Manager.
**Tasks**: structured AgentTasks assigned to specialists.

This layout makes tasks traceable from idea → story → task → summary.

---

# 8. `.opencode/memory/` — Project Memory System

Memory follows the structure defined in MEMORY.md.

```
.opencode/memory/
  learning/         # Lessons learned, troubleshooting insights
  pattern/          # Project-specific patterns derived from real deliverables
  knowledge/        # Architecture decisions, conventions, internal rules
  debugging/        # Debugging cases + resolutions
  configuration/    # Settings, environment nuances, build setups
```

Memory entries use the schema from MEMORY.md.
Agents must read memory before using skills.

---

# 9. `.opencode/skills/` — Skill System (Claude-style Skills)

Skills follow the structure defined in SKILLS.md.

```
.opencode/skills/
  csharp/
    index.md
    patterns/
      async-pattern.md
      error-handling.md
    workflows/
      implementing-api-endpoints.md

  react/
    index.md
    patterns/
      component-structure.md
    workflows/
      routing-setup.md

  api/
    index.md
    design/
      versioning-rules.md
    rules/
      error-contracts.md

  dotnet/
  python/
  sql/
  testing/
  documentation/
  ux/
```

### Notes:

* Skills **replace capabilities**
* Skills are **loaded on demand**
* Skills must be deterministic, role-neutral, and reusable
* Agents never write or modify skills

The structure is future-proof for:

* PDL skill synthesis
* MCP-delivered skills
* automated skill discovery
* skill packs per language/framework

---

# 10. `src/` — Application Code (Non-agent)

```
src/
  backend/
  frontend/
  infrastructure/
  scripts/
```

This folder holds your actual project code.
Agents may edit this folder (if their role/phase allows).

---

# 11. Additional Optional Folders

### `/docs/`

User documentation, architecture diagrams, design system documents.

### `/tests/`

Manual or human-authored tests, load tests, exploratory tests.

Agents will also generate tests inside `src/...`.

### `/infra/`

Infrastructure code (Bicep, Terraform, Helm Charts, etc.)

---

# 12. Interaction Map (How Everything Connects)

```
AGENTS.md
↳ governs all agent behavior

.opencode/system/*
↳ defines systems (tasks, memory, skills, workflow)

.opencode/agenttasks-templates/*
↳ defines how tasks are created

Planning/Design Agents
↳ create AgentTasks in /opencode/agenttasks/...

Execution Agents
↳ read Memory → load Skills → execute Task → write deliverables

.opencode/memory/*
↳ shared project knowledge updated via tasks

.opencode/skills/*
↳ reusable domain knowledge
```

Everything resolves through this architecture.

---

# 13. Example Full Project Structure

```
/
├── AGENTS.md
├── .opencode/
│   ├── agents/
│   ├── system/
│   ├── agenttasks-templates/
│   ├── agenttasks/
│   │   └── features/
│   │       └── FEATURE-001-authentication/
│   │           ├── index.md
│   │           ├── user-stories/
│   │           └── tasks/
│   ├── memory/
│   │   ├── learning/
│   │   ├── pattern/
│   │   ├── knowledge/
│   │   ├── debugging/
│   │   └── configuration/
│   └── skills/
│       ├── csharp/
│       ├── react/
│       ├── api/
│       └── documentation/
└── src/
    ├── backend/
    ├── frontend/
    └── infrastructure/
```
