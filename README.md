# README.md

# OpenCode Multi-Agent Development System - Awesome-OpenCode

This repository provides a complete **multi-agent software development environment** for OpenCode.
It models a real engineering team with **13 specialized agents**, a structured SDLC, a **Skills system** for domain expertise, and a **Memory system** for project-specific knowledge.

This system enables consistent, reproducible, high-quality software development with strict role separation.

---

## What This System Contains

### 1. Regulated Multi-Agent Team

13 agents representing professional roles:

* **Leadership:** Project Manager, Architect
* **Design & Requirements:** Product Manager, Requirements Engineer, Designer
* **Development:** Developer, AI Engineer, Database Engineer
* **Operations:** DevOps Engineer, System Engineer
* **Quality & Security:** Security Engineer, QA Engineer, Tester (white-box), User (black-box)

Each agent is defined in `.opencode/agents/` and follows strict behavioral rules.

---

### 2. Skills System (Domain Expertise)

Filesystem-based expert modules used by agents to perform tasks correctly.

Examples:
C# Skill, .NET Skill, Python Skill, React Skill, API Design Skill, SQL Skill, Azure Bicep Skill

Skills provide:

* best practices
* workflows
* patterns
* examples
* troubleshooting

Agents load Skills on demand.
Details: `SKILLS.md`

---

### 3. Memory System (Project Knowledge)

Persistent project-specific knowledge created over time:

* reusable patterns
* resolved bugs
* architecture decisions
* conventions
* configuration notes

Agents must search Memory before executing tasks.
Details: `MEMORY.md`

---

### 4. Structured AgentTasks

All work happens through AgentTasks with:

* goal and business value
* full context
* required Skills
* implementation steps
* validation criteria
* completion requirements

Tasks are sized automatically: Nano → Tiny → Medium → Large → Mega
Details: `AGENTTASKS.md`

---

### 5. SDLC Phases

All work follows a regulated lifecycle:

1. Planning
2. Design
3. Implementation
4. Deployment
5. QA

Agents may only work inside their assigned phase.
Details: `WORKFLOW.md`


## When to Read What

| File            | Purpose                                |
| --------------- | -------------------------------------- |
| `SETUP.md`      | How to install and use the system      |
| `AGENTS.md`     | Global agent behavior & SDLC rules     |
| `SKILLS.md`     | How agents load domain expertise       |
| `MEMORY.md`     | How project knowledge is stored & used |
| `AGENTTASKS.md` | Task structure & complexity tiers      |
| `WORKFLOW.md`   | End-to-end SDLC flow                   |
| `DIRECTORY.md`  | Repo structure                         |

---

## Why This Exists

This system enables:

* predictable, high-quality agent behavior
* strict role separation
* reusable domain expertise via Skills
* evolving project knowledge via Memory
* reproducible development through AgentTasks
* a full software team simulation inside OpenCode

It is suitable for complex, long-running software projects that require consistency and auditability.
