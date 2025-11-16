# SKILLS.md

**Skill System Specification for the Multi-Agent Development Environment**

This document defines the structure, usage rules, and lifecycle of **Skills**, the modular knowledge system that provides domain-specific expertise to agents.

Skills are modeled after the “Agent Skills” framework described in Claude’s documentation:

[https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)

Skills turn general-purpose agents into specialists without modifying agent prompts or global configuration.

---

# 1. Purpose of the Skill System

Skills are **filesystem-based, reusable knowledge modules** that provide:

* domain expertise
* workflows
* patterns
* best practices
* conventions
* troubleshooting
* architecture rules
* coding standards
* design systems
* checklists
* reusable logic

Unlike prompts or AgentTask content, Skills are **persistent**, **composable**, and **load-on-demand**.

Skills ensure:

* no repeated instruction across sessions
* consistent expert behavior
* stable domain knowledge
* scalable growth of team expertise
* guaranteed adherence to patterns
* future-proofing (skills evolve without breaking agents)

---

# 2. What Skills Are (and Are Not)

### 2.1 Skills ARE:

* reusable context blocks
* structured, organized knowledge
* persistent filesystem resources
* modular expert systems
* loaded dynamically when an agent requests them
* self-contained units of domain guidance
* versionable and updatable independently of agents

### 2.2 Skills are NOT:

* role prompts
* system prompts
* AgentTasks
* tools or capabilities
* direct instructions to modify files
* conversational reminders
* implementation-specific commands
* execution-level logic
* hallucinated content

Skills augment agents **only through reading, not writing**.

---

# 3. Why Skills (according to Claude’s design philosophy)

Claude Skills are designed for:

* reproducible reasoning
* expert consistency
* elimination of repeated context
* separation of concerns
* safe extensibility
* long-term maintainability
* scalable, modular knowledge injection

This environment uses the same principles.

---

# 4. Skill Folder Structure

Skills are stored in a dedicated top-level directory:

```
skills/
  <skill-name>/
    metadata.yaml
    overview.md
    workflows/
      ...
    patterns/
      ...
    examples/
      ...
    troubleshooting/
      ...
    references/
      ...
```

### 4.1 Skill Directory Requirements

Every skill MUST contain:

**metadata.yaml**
Defines the identity, version, purpose, and scope of the skill.

**overview.md**
Provides a high-level explanation of the domain and core principles.

Optional subfolders:

* `workflows/` – step-by-step procedures
* `patterns/` – reusable patterns, templates, structures
* `examples/` – code examples or architectural examples
* `troubleshooting/` – known issues and solutions
* `references/` – standards, RFCs, style guides, external docs

Agents must never modify skill files.

---

# 5. Skill Metadata Specification

Every skill includes a `metadata.yaml`:

```yaml
name: "CSharp Skill"
id: csharp
version: "1.0.0"

description: >
  Provides expert knowledge, patterns, standards, and workflows 
  for developing C# and .NET applications.

tags:
  - backend
  - dotnet
  - csharp
  - language

role_applicability:
  - developer
  - ai-engineer
  - system-engineer

phase_applicability:
  - implementation
  - qa

includes:
  - overview.md
  - workflows/
  - patterns/
  - examples/
  - troubleshooting/
```

This metadata allows agents to:

* discover relevant skills
* validate that the skill matches their role
* validate that the skill matches the current phase
* load only the required components

---

# 6. Skill Loading Rules for Agents

Agents load skills dynamically **based on task need**, not automatically.

### 6.1 When an agent may request a skill

Agents may request skills when:

* the AgentTask indicates a specific domain (e.g., "React component")
* the agent identifies a domain need (e.g., “backend API design”)
* the task refers to a skill by name
* the agent is uncertain and needs domain standards
* the task requires language-specific patterns

### 6.2 How agents request skills

Agents request skills by name:

> “Load the React Skill to proceed.”

or when explicit:

> “Load the C# Skill for .NET patterns and workflows.”

### 6.3 What an agent receives when loading a skill

Loading a skill provides:

* the `overview.md`
* relevant workflows
* applicable patterns
* examples
* troubleshooting guidance
* references

Agents **do not** receive tool logic, commands, or implementation details.

### 6.4 Agents must never:

* hallucinate new skills
* modify skill content
* load irrelevant skills
* load skills outside their allowed phase
* skip skill usage when domain knowledge is required

---

# 7. Role-to-Skill Binding (Soft Enforcement)

This system uses **soft role-to-skill binding** similar to Claude’s Skill Model:

Roles may use only skills whose metadata lists them under `role_applicability`.

Examples:

### Developer

Allowed skills:

* CSharp Skill
* .NET Skill
* React Skill
* API Skill
* SQL/Database Skill

Not allowed:

* UX Design Skill
* Project Management Skill

### Architect

Allowed:

* Architecture Skill
* API Skill
* Security Skill
* Infrastructure Skill

Not allowed:

* CSharp Implementation Skill
* React Component Skill

---

# 8. Phase-to-Skill Binding (Hard Enforcement)

Example bindings:

### Planning Phase

Allowed skills:

* Business Analysis Skill
* Requirements Skill
* Documentation Skill

Not allowed:

* Coding Skills
* Architecture Skills
* Deployment Skills

### Design Phase

Allowed:

* Architecture Skill
* UX/UI Skill
* Database Modeling Skill
* Documentation Skill

Not allowed:

* Implementation Skills
* Testing Skills

### Implementation Phase

Allowed:

* All language skills (C#, Python, JS, React)
* Framework skills (.NET, Flask, Node.js, etc.)
* Integration & API Skills

Not allowed:

* Planning or UX skills

### Deployment Phase

Allowed:

* DevOps Skill
* IaC/Bicep Skill
* Security Skill

### QA Phase

Allowed:

* Testing Skill
* QA Workflow Skill
* Test Automation Skill
* Documentation Skill

---

# 9. Skill Versioning

Each Skill has a semantic version (`major.minor.patch`):

* **major** → breaking changes
* **minor** → new workflows or patterns
* **patch** → corrections or improvements

Agents must:

* treat each version atomically
* never reference older versions unless explicitly required
* stop and escalate when version mismatches affect the task

---

# 10. How Skills Integrate with Tasks

When an AgentTask requires domain knowledge, the agent:

1. reads the task
2. determines required skills
3. loads them explicitly
4. applies what is relevant
5. executes the task
6. never modifies or extends the skill

Skills provide:

* patterns
* workflows
* validations
* design rules
* architecture frameworks
* coding conventions

Tasks provide:

* intent
* constraints
* acceptance criteria
* project context

---

# 11. Skill Safety & Escalation Rules

Agents must escalate to the Project Manager if:

* a required skill is missing or undefined
* a skill is outside role or phase applicability
* the skill version is incompatible
* the skill contradicts task instructions
* multiple skills conflict
* the skill does not cover the required domain

Agents must not guess when skill content is insufficient.

---

# 12. Skill Creation Guidelines

New skills must follow:

```
skills/
  <skill-name>/
    metadata.yaml
    overview.md
    workflows/
    patterns/
    examples/
    troubleshooting/
    references/
```

All skills must be:

* self-contained
* domain-specific
* generalizable
* understandable without external prompts
* stable and versioned
* file-based (never inline in agent prompts)

---

# 13. Interaction With MCP or Tools

While Skills are conceptual and file-based:

* MCP or tools may use Skills to perform contextual operations
* but agents themselves do not use tools or MCP directly
* Skills never contain tool commands
* Skills serve as **knowledge**, not execution

---

# 14. Summary

Skills enable:

* modular expert systems
* consistent patterns
* scalable knowledge
* deterministic agent behavior
* future-proof extensibility

Agents remain stable because they:

* read Skills
* never embed expert knowledge in prompts
* never change Skills
* request Skills only when needed
* apply Skills to task execution
* always stay within their role and phase

Skills are the backbone of professional-grade specialization in this multi-agent environment.
