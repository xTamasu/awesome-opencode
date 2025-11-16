# MEMORY.md

**Memory System Specification for the Multi-Agent Software Development Environment**

This document defines the memory subsystem used by all agents.
Memory provides a persistent, structured, project-specific knowledge base that evolves as tasks are completed.

Memory captures *what this project has learned* — not how the world works.

Memory is factual, historical, and grounded in actual work performed by the agents.

---

# 1. Purpose of the Memory System

Memory exists to:

1. Preserve reusable **project-specific** knowledge
2. Prevent repeated mistakes
3. Encode implementation patterns actually used in this project
4. Capture debugging experiences and resolutions
5. Record architectural decisions taken during development
6. Improve output consistency across agents and tasks
7. Serve as a “project brain” that grows over time
8. Provide deterministic references for future work

Memory is not a prompt, not a Skill, and not an instruction layer.

Memory is a **long-term knowledge base derived from the project itself**.

---

# 2. Nature of Memory

Memory entries must be:

* factual
* historical
* derived from real execution
* project-specific
* concise and technical
* written after completion of an AgentTask
* structured and deterministic

Memory must **never** contain:

* assumptions
* instructions
* planning
* speculative content
* best practices
* domain-general expertise (belongs in Skills)
* subjective commentary
* duplicated Skill content

Memory describes what *has happened*, not what *should happen*.

---

# 3. Memory vs Skills

This distinction is fundamental to the entire system:

| Aspect           | Skills                                      | Memory                                                     |
| ---------------- | ------------------------------------------- | ---------------------------------------------------------- |
| **Purpose**      | Domain knowledge, workflows, best practices | Project-specific history, solved issues, emerging patterns |
| **Origin**       | Human-authored                              | Agent-authored (based on execution)                        |
| **Scope**        | Universal                                   | Local to this project                                      |
| **Lifecycle**    | Stable, versioned manually                  | Evolves continuously                                       |
| **Content**      | “How experts work”                          | “How this project works”                                   |
| **Usage**        | Loaded during tasks as needed               | Must be consulted before every task                        |
| **Modification** | Only by humans                              | By agents (with rules) + human review                      |
| **Volatility**   | Low                                         | High, growing with work                                    |

Memory is **execution-derived, not instruction-derived**.

Skills teach agents *how to work*.
Memory teaches agents *how this project behaves*.

Both are required for safe and consistent outcomes.

---

# 4. Memory Directory Structure

Memory is stored in:

```
memory/
  Learning/
  Pattern/
  Knowledge/
  Debugging/
  Configuration/
```

### 4.1 Learning

New insights discovered during implementation or debugging.
Examples:

* “JWT edge cases in this project”
* “State handling issues specific to our React architecture”

### 4.2 Pattern

Reusable project-specific patterns derived from actual code delivered.
Examples:

* “Project’s canonical API controller structure”
* “Shared React state management pattern used across routes”

### 4.3 Knowledge

Recorded architectural decisions and long-term project-wide information.
Examples:

* chosen tech stack rules
* architecture decision records (ADR)
* naming conventions unique to the project

### 4.4 Debugging

Resolved debugging events, including:

* root cause
* steps taken
* fix
* validation strategy
* future prevention

### 4.5 Configuration

Setup, infrastructure, and environment-specific project details.

---

# 5. Memory Entry Format (Unified Schema)

Every memory entry must follow the same structure:

```
# Title

## Summary
Short explanation of the entry and why it matters.

## Context
Where and why this entry became relevant within the project.

## Details
Comprehensive explanation of what happened or what was discovered.

## Pattern (if applicable)
Reusable pattern derived from actual implementation.

## Steps Taken (for debugging)
Chronological actions used to resolve the issue.

## Validation
How correctness was confirmed.

## References
Links to code, relevant tasks, skills, or external docs.

## Version
v1.0.0
```

---

# 6. Memory Creation Rules

Memory updates must only occur:

* after successful completion of an AgentTask
* when new, reusable **project-specific** knowledge is discovered
* when a novel debugging event occurred
* when an existing memory entry requires factual update
* when required explicitly by the Project Manager

### Who may write memory?

| Role                  | Allowed?                          |
| --------------------- | --------------------------------- |
| Planning agents       | No                                |
| Design agents         | No                                |
| Implementation agents | Yes (with task requirement)       |
| Deployment agents     | Yes (deployment insights only)    |
| QA/Test agents        | Yes (bug patterns, test insights) |
| Project Manager       | Yes                               |

Only agents whose tasks generate new project insights may add memory entries.

---

# 7. Mandatory Memory Usage Before Tasks

Before executing any AgentTask, agents must:

1. Read the entire task
2. Search `memory/` for relevant entries
3. Load applicable patterns or insights
4. Compare task requirements with memory
5. Apply lessons learned to avoid regressions
6. Reference used memory entries in their completion summary

This rule applies to:

* Developers
* AI Engineers
* Database Engineers
* System Engineers
* QA Engineers
* Testers

Memory must always be consulted **before** loading Skills.

---

# 8. Memory Search Protocol

Agents must search using:

* keywords from the task
* technology matches (C#, React, API, SQL, etc.)
* previously solved issues
* structural patterns
* debugging categories

If no relevant memory exists:

* proceed with Skill loading + task context
* do not fabricate memory
* do not inject assumptions

If relevant memory exists:

* fully incorporate it into the task execution
* respect the project's previous decisions and patterns

---

# 9. Memory Update Protocol

After completing a task, an agent may update memory only when:

* the AgentTask explicitly requires a memory addition
* a new reusable project pattern emerges
* a debugging issue was resolved
* an architecture detail changed factually
* versioning requires updating an entry

Memory entries must be:

* concise
* factual
* project-specific
* free of speculation
* free of redundancy
* aligned with the unified schema

Memory updates must be referenced in the AgentTask completion summary:

```
Memory Update:
- created: memory/Pattern/api-controller-structure-v1.md
```

---

# 10. Quality Standards for Memory

Memory entries must be:

* technical
* accurate
* non-repetitive
* not general best practices
* based only on real project history
* deterministic
* independently verifiable

Memory must avoid:

* duplicating Skill content
* mixing general theory with project facts
* conversational or verbose explanations
* ambiguous guidelines
* personal tone or subjective conclusions

Memory is part of the permanent codebase and must remain maintainable.

---

# 11. Memory Versioning

Memory entries use semantic versioning:

* **MAJOR** — breaking conceptual change
* **MINOR** — new insight added
* **PATCH** — clarifications, typo fixes

Only humans may update major or minor versions during review cycles.
Agents may only create new entries using `v1.0.0` unless instructed otherwise.

---

# 12. Memory in the SDLC

Memory enhances every SDLC phase:

### Planning Phase

* Validates previous decisions
* Ensures historical constraints are respected

### Design Phase

* Provides architecture decisions taken earlier in the project
* Prevents design drift

### Implementation Phase

* Reuses established implementation patterns
* Avoids previously encountered bugs

### Deployment Phase

* Guides environment-specific setups
* Avoids repeated deployment issues

### QA Phase

* Informs test design
* Prevents recurring bugs
* Helps classify common failure points

---

# 13. Memory as a Stability Mechanism

Memory ensures that the multi-agent environment:

* grows more intelligent over time
* prevents regressions
* maintains consistency across contributors
* avoids re-solving known problems
* enforces historical project decisions
* supports deterministic execution
* allows agents to onboard immediately with full context

Memory is the backbone of **long-term project intelligence**.
