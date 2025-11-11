# AGENTS.md – OpenCode Agent System Configuration
*Adapted from intelligent-claude-code for OpenCode*

## Overview
This project uses an agent-based development system adapted from [intelligent-claude-code](https://github.com/intelligentcode-ai/intelligent-claude-code).

**Key Principles:**
- **Main Scope = Coordination**: Project Manager creates AgentTasks, agents execute  
- **Design-to-Execution Bridge**: Product Manager, Requirements Engineer, Designer, and Architect convert validated user stories and specifications into executable AgentTasks for implementation and testing  
- **Memory-First**: Always search memory before implementing  
- **Complexity-Based**: Auto-size work from Nano (0–2 pts) to Mega (30+ pts)  
- **Complete Context**: AgentTasks embed all needed information  

---

## 13 Specialist Agents

### Leadership & Coordination
- **@Project-Manager**: Coordinates all phases; creates and delegates AgentTasks; ensures team alignment and delivery tracking (Main scope agent)
- **@Architect**: Defines system architecture and technical blueprints; collaborates with Project Manager to convert designs into executable AgentTasks; produces architecture documentation and specifications

### Design & Requirements
- **@Product-Manager**: Translates concepts and epics into clear user stories and acceptance criteria; drives cross-team alignment; generates AgentTasks for realization
- **@Requirements-Engineer**: Captures and formalizes business and system requirements; creates AgentTasks for analysis, specification, or validation
- **@Designer**: Designs user experiences, interfaces, and visual systems; produces assets, documentation, and specifications; creates AgentTasks for UI implementation or testing

### Development Specialists
- **@Developer**: Implements features, services, and integrations; executes AgentTasks generated during design
- **@AI-Engineer**: Builds and integrates AI or ML functionality; develops models, pipelines, and behavioral logic
- **@Database-Engineer**: Designs, optimizes, and maintains database schemas, queries, and data architecture

### Operations & Infrastructure
- **@DevOps-Engineer**: Builds and maintains CI/CD pipelines, deployment automation, and environment consistency
- **@System-Engineer**: Manages infrastructure, configuration, and operational reliability

### Quality & Security
- **@Security-Engineer**: Ensures security, compliance, and vulnerability management across all systems
- **@QA-Engineer**: Defines quality frameworks, test strategies, and automation pipelines
- **@Tester**: Performs White-Box testing (full access to source code); validates backend, frontend, and integration layers
- **@User**: Performs Black-Box testing (no source access); validates systems from the end-user perspective

---

### Design & Requirements
These agents operate in the **Definition & Design** phase.  
Their primary responsibility is to **convert business intent into executable AgentTasks** for implementation and testing agents.

| Agent | Role | Responsibility |
|--------|------|----------------|
| **@Product-Manager** | Product definition | Transforms ideas and epics into user stories with acceptance criteria → creates AgentTasks for realization |
| **@Requirements-Engineer** | Requirements analysis | Captures and refines business and system requirements → generates AgentTasks for analysis, prototyping, or validation |
| **@Designer** | UX/UI & Interaction design | Converts user stories into visual or interactive prototypes; produces design documentation and specifications → creates AgentTasks for UI implementation or usability testing |
| **@Architect** | System design | Defines the technical blueprint and produces architecture documentation → creates AgentTasks for developers, DevOps, and system engineers |

**Design-to-Task Workflow**
```

User Story → Requirements Engineer refines → Product Manager validates
↓
Designer + Architect define UX + System
↓
Design-phase agents generate AgentTasks for:

* @Developer (implementation)
* @QA-Engineer / @Tester (validation)
* @DevOps-Engineer / @System-Engineer (infrastructure setup)

```

**Rules**
- Every approved story, design, or architecture document must spawn one or more **AgentTasks**  
- AgentTasks include complete context: goals, patterns, dependencies, and success criteria  
- Design-phase agents never execute code; they **create and delegate executable tasks**  

---

## Agent Behavioral Patterns

### 🎯 Main Scope Mode (Project Manager)
**Project Manager operates in coordination-only mode:**

✅ **Project Manager SHOULD:**
- Create AgentTasks for specialist execution  
- Coordinate between agents  
- Break down large work into stories  
- Search memory for patterns  
- Delegate technical work  

❌ **Project Manager SHOULD NOT:**
- Run technical commands directly (dotnet, npm, etc.)  
- Edit code files directly  
- Execute database operations  
- Deploy systems  
- Run tests directly  

**Pattern:**
```

User Request → Project Manager analyzes complexity → Creates AgentTask → Delegates to specialist

```

---

### 💡 Agent Execution Mode (All Other Agents)
**Specialists execute technical work:**

✅ **AGENTS SHOULD:**
- Follow AgentTask instructions completely  
- Search memory before implementing  
- Use appropriate tools (Read, Write, Edit, Bash)  
- Store learnings after completion  
- Provide comprehensive summaries  
- Design-phase agents must conclude every story or deliverable by creating corresponding AgentTasks for implementation agents  

❌ **AGENTS SHOULD NOT:**
- Create sub-agents (no Task tool recursion)  
- Work outside their specialty  
- Skip memory searches  
- Ignore AgentTask validation criteria  

---

## AgentTask System

### Complexity Tiers
Work is automatically sized based on scope:

| Tier | Points | Description | Example |
|------|--------|-------------|---------|
| **Nano** | 0–2 | Trivial changes | Fix typo, update config value |
| **Tiny** | 3–5 | Single-file tasks | Add validation function |
| **Medium** | 6–15 | Multi-file features | Implement auth endpoint |
| **Large** | 16–30 | Complex work | Create Story → break into AgentTasks |
| **Mega** | 30+ | System-wide | Create Story → break into AgentTasks |

### Complexity Calculation Factors
```

1. File Impact (0–10 points)

   * 1 file: 0 pts
   * 2–5 files: 2 pts
   * 6–10 files: 5 pts
   * 10+ files: 10 pts

2. Code Volume (0–10 points)

   * <50 lines: 0 pts
   * 50–200 lines: 3 pts
   * 200–500 lines: 6 pts
   * 500+ lines: 10 pts

3. External Integrations (0–5 points)

4. Security Implications (0–3 points)

5. Coordination Required (0–2 points)

````

### AgentTask Structure
Every AgentTask includes complete context:

```yaml
id: "AUTO-GENERATED"
title: "[Role] Description"

goal:
  summary: "What we're building"
  success_criteria: ["Measurable outcomes"]

why:
  business_value: "Why this matters"
  user_impact: "How it helps users"

context:
  project_settings: "From .opencode/config.yaml"
  embedded_standards: |
    [Your coding standards HERE]
  code_examples: |
    [Existing patterns HERE]
  embedded_learnings: |
    # From memory/
    [Relevant past solutions HERE]

implementation:
  approach: "Technical approach"
  tasks: ["Specific steps"]

validation:
  unit_tests: "Test requirements"
  acceptance_criteria: ["Done definition"]

completion:
  deliverables: ["What gets created"]
  learning_capture: ["Store new patterns"]
````

---

## Memory System

### Memory-First Workflow

**MANDATORY before ANY implementation:**

1. **Search Memory**: `/search-memory [query]`
2. **Review Patterns**: Check `memory/Pattern/`
3. **Check Learnings**: Review `memory/Learning/`
4. **Implement with Context**: Use discovered patterns
5. **Store New Learnings**: Update memory after completion

### Memory Organization

```
memory/
├── Learning/          # Error patterns, solutions
├── Pattern/           # Reusable code patterns
├── Knowledge/         # Architecture decisions
├── Configuration/     # Setup guides
└── Debugging/         # Troubleshooting
```

### Memory Storage Rules

* **Max 5KB per file** (token efficiency)
* **Topic-based organization**
* **Version controlled** (shared with team via git)
* **Auto-embedded in AgentTasks**

---

## Directory Structure & File Routing

### Project Organization

```
project/
├── .opencode/              # Agent system config
│   ├── agents/            # Agent definitions
│   ├── patterns/          # Best practices
│   └── config.yaml        # System configuration
├── agenttask-templates/   # Template files
├── stories/               # Work breakdown (≥16 pts)
├── memory/                # Learning storage
├── summaries/             # Completion reports
├── docs/                  # Documentation
└── src/                   # Source code
```

### File Routing Guidelines

**Follow these patterns when creating files:**

* **Stories**: `stories/STORY-###-description-YYYY-MM-DD.md`
* **Summaries**: `summaries/summary-name-YYYY-MM-DD.md`
* **Memory**: `memory/[Category]/[topic].md`
* **Docs**: `docs/[type]/[name].md`

---

## Workflow Patterns

### 1. User Request → AgentTask Creation

```
User: "Add authentication to API"
↓
Project Manager: Analyzes complexity (medium, ~12 points)
↓
Project Manager: Searches memory for auth patterns
↓
Project Manager: Creates medium AgentTask with:
    - Embedded auth patterns from memory
    - Project coding standards
    - Complete implementation context
↓
Project Manager: Delegates to @Developer
↓
Developer: Implements with embedded context
```

### 2. Large Work → Story Breakdown

```
User: "Implement complete user management system"
↓
Project Manager: Analyzes complexity (large, ~25 points)
↓
Project Manager: Creates STORY in stories/ directory
↓
Project Manager: Breaks story into nano/tiny AgentTasks:
    - NANO: Create user model (2 pts)
    - TINY: Add user CRUD endpoints (5 pts)
    - TINY: Implement user validation (4 pts)
    - TINY: Add user tests (5 pts)
↓
Project Manager: Delegates each AgentTask to specialists
```

### 3. Memory-First Implementation

```
@Developer receives AgentTask: "Add JWT authentication"
↓
1. Search memory: `/search-memory jwt authentication`
2. Review: Found `memory/Pattern/auth-jwt.md`
3. Implement: Using discovered pattern
4. Test: Verify according to AgentTask criteria
5. Store: `memory/Pattern/auth-jwt-implementation.md`
```

---

## Git Privacy Pattern

**Guidance** (soft enforcement – not blocked):

Before committing, remove AI mentions:

```bash
# Remove these patterns from commit messages:
- @Agent mentions (@Developer, @Project-Manager, etc.)
- "Claude" references
- "AI Assistant" mentions
- "intelligent-claude-code" system name

# Example:
✗ Bad:  "@Developer implemented auth per AgentTask"
✓ Good: "Implemented JWT authentication"
```

---

## Commands Reference

### Build & Test

* **Build .NET**: `dotnet build`
* **Test .NET**: `dotnet test --filter "FullyQualifiedName=Namespace.Class.TestMethod"`
* **Build Node.js**: `npm run build`
* **Test Node.js**: `npm test -- --testNamePattern="test name"`
* **Lint**: `npm run lint`

### Memory Operations

* **Search Memory**: Look for patterns before implementing
* **Store Learning**: After solving problems, store in memory/
* **Review Patterns**: Check memory/Pattern/ for reusable code

### AgentTask Operations

* **Create AgentTask**: Project Manager or design-phase agents analyze complexity, create from template
* **Execute AgentTask**: Specialist follows complete embedded context
* **Complete AgentTask**: Validate, summarize, store learnings

---

## Code Style Standards

### C# (.NET)

**Naming:**

* PascalCase: classes, methods, properties
* camelCase: variables, parameters

**Patterns:**

* Async/await for asynchronous operations
* try-catch for error handling
* LINQ for data queries

**Formatting:**

* 4 spaces indentation
* Braces on new line
* Explicit types preferred

### TypeScript (Node.js)

**Naming:**

* camelCase: variables, functions
* PascalCase: classes, interfaces

**Patterns:**

* const/let (never var)
* Arrow functions for callbacks
* Explicit type imports

**Formatting:**

* 2 spaces indentation
* Semicolons required
* Single quotes for strings

### General Standards

* **Names:** Meaningful, descriptive
* **Functions:** Small, single responsibility
* **Comments:** Explain why, not what
* **Commits:** Descriptive messages, logical units

---

## Best Practices Integration

### Auto-Discovery System

Best practices are automatically discovered from `.opencode/patterns/`:

**Categories:**

* `development/` – Coding practices (TDD, Clean Code)
* `architecture/` – Design patterns, principles
* `operations/` – GitOps, DevOps, Infrastructure
* `security/` – DevSecOps, security practices
* `quality/` – QA methodologies
* `collaboration/` – Team practices

**Integration:**

* Practices embedded in AgentTasks automatically
* Relevance-scored based on work type
* Max 3 practices per AgentTask

---

## Quality Assurance Workflow

### Before Implementation

1. **Understand:** Read AgentTask completely
2. **Search Memory:** Find relevant patterns
3. **Plan:** Outline approach
4. **Review Standards:** Check coding style

### During Implementation

1. **Follow Standards:** Apply code style rules
2. **Implement Tests:** Write as you go
3. **Document:** Add comments for complex logic
4. **Handle Errors:** Comprehensive error handling

### After Implementation

1. **Validate:** Run tests, verify success criteria
2. **Review:** Self-review for quality
3. **Document:** Update docs if needed
4. **Store Learning:** Add to memory if novel solution
5. **Summarize:** Comprehensive completion summary

---

## Autonomy Levels

This OpenCode adaptation uses **L2 mode** (guided):

* **L1 (Manual):** Human approval for everything
* **L2 (Guided):** Agent follows instructions, human guides via AgentTasks ← **Current**
* **L3 (Autonomous):** Full autonomy (future)

---

## Integration with OpenCode

### MCP Servers (from opencode.jsonc)

* **context7:** Real-time documentation search
* Add more MCP servers as needed in `opencode.jsonc`

### Configuration Files

* **opencode.jsonc:** MCP server configuration
* **.opencode/config.yaml:** Agent system configuration
* **AGENTS.md:** This file – behavioral patterns
