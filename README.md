# OpenCode Agent-Based Development System

**Adapted from [intelligent-claude-code](https://github.com/intelligentcode-ai/intelligent-claude-code) for OpenCode**

Transform your OpenCode workspace into a **13-agent virtual development team** with structured AgentTask execution, memory-first operations, and complexity-based work breakdown.

---

## 🚀 Quick Start

```bash
# 1. Review the setup
cat SETUP.md

# 2. Read behavioral patterns
cat AGENTS.md

# 3. Start using agents
@Project-Manager Lets create a todo app!

---

## ✨ What You Get

### 13 Specialist Agents

* **Leadership**: @Project-Manager, @Architect
* **Design & Requirements**: @Product-Manager, @Requirements-Engineer, @Designer
* **Development**: @Developer, @AI-Engineer, @Database-Engineer
* **Operations**: @DevOps-Engineer, @System-Engineer
* **Quality & Security**: @QA-Engineer, @Security-Engineer, @Tester, @User

### AgentTask System

* **Auto-Sizing**: Nano (0–2) → Tiny (3–5) → Medium (6–15) → Large (16–30) → Mega (30+)
* **Complete Context**: Embedded standards, patterns, examples
* **Memory-First**: Search before implement, store after solve
* **Quality Built-In**: Tests, validation, and documentation required

### Memory System

* **Pattern Storage**: Reusable code and design patterns
* **Learning Capture**: Problem–solution knowledge
* **Knowledge Base**: Architecture and system design decisions
* **Team Sharing**: Version-controlled via git

### Behavioral Patterns

* **Main Scope = Coordination**: Project Manager creates AgentTasks
* **Design-to-Execution Bridge**: Product Manager, Requirements Engineer, Designer, and Architect convert user stories into executable tasks
* **Specialists Execute**: Implementation agents handle delivery
* **Memory-First**: Always search before implementing
* **Quality Gates**: Validation, documentation, and testing required

---

## 📁 Repository Structure

```
.
├── .opencode/
│   ├── agents/           # 13 agent definitions
│   ├── patterns/         # Best practices (add your own)
│   └── config.yaml       # System configuration
│
├── agenttask-templates/  # 5 complexity tier templates
├── memory/               # Pattern/Learning/Knowledge storage
├── stories/              # Work breakdown (≥16 pts)
├── summaries/            # Completion reports
│
├── opencode.jsonc        # OpenCode + MCP config
├── AGENTS.md             # Behavioral patterns & standards
├── ADAPTATION_GUIDE.md   # What changed from Claude Code
├── SETUP.md              # Installation & usage guide
└── README.md             # This file
```

---

## 🎯 How It Works

### 1. User Request → AgentTask Creation

```
User: "Add authentication to the API"
↓
Project Manager analyzes complexity
↓
12 points = Medium AgentTask
Project Manager searches memory for auth patterns
Creates AgentTask with complete context
Delegates to @Developer
↓
Developer implements using embedded patterns
Developer runs tests and provides summary
```

### 2. Large Work → Story Breakdown

```
User: "Build user management system"
↓
Project Manager breaks down work
↓
25 points = Large → Create Story
Breaks into smaller AgentTasks:
    - Setup (2 pts) → @Developer
    - CRUD (5 pts) → @Developer
    - Tests (4 pts) → @QA-Engineer
Coordinates execution across agents
```

### 3. Memory-First Implementation

```
@Developer implement feature X
↓
Search memory/Pattern/
Find similar implementation
Apply pattern with context
Store novel solution back to memory
```

---

## 🔧 Key Features

### Complexity-Based Sizing

| Tier       | Points | Description       | Action             |
| ---------- | ------ | ----------------- | ------------------ |
| **Nano**   | 0–2    | Trivial changes   | Direct execution   |
| **Tiny**   | 3–5    | Simple tasks      | Direct execution   |
| **Medium** | 6–15   | Standard features | Direct execution   |
| **Large**  | 16–30  | Complex work      | Create Story first |
| **Mega**   | 30+    | System-wide       | Create Story first |

### AgentTask Structure

Each AgentTask includes:

* **Goal** — What’s being built
* **Why** — Business value and user impact
* **Context** — Standards, patterns, examples
* **Implementation** — Technical approach and steps
* **Validation** — Acceptance criteria and tests
* **Completion** — Deliverables and learnings

### Memory System

* **Before:** Search for patterns
* **During:** Apply discovered solutions
* **After:** Store new learnings
* **Share:** Version-controlled via git

---

## 🎨 Adaptation from Claude Code

### What Changed

* **13 Agents** (instead of 14): Backend-Tester replaced by dual testing roles — @Tester (White-Box) and @User (Black-Box)
* **Separated Roles:** Project Manager coordinates; Product Manager defines user stories
* **Expanded Design Phase:** Architect and Designer now produce documentation and specifications as outputs
* **Behavioral Clarifications:** Design-to-Execution workflow explicitly defined
* **Simpler Setup:** Soft enforcement instead of hooks

### What Stayed

* **AgentTask System:** Context-driven, memory-first workflow
* **Complexity Tiers:** Nano → Mega auto-sizing
* **Memory System:** Pattern and knowledge retention
* **Best Practices:** Auto-discovery integration

See `ADAPTATION_GUIDE.md` for detailed differences.

---

## 📚 Documentation

### Core Guides

* **[SETUP.md](SETUP.md)** — Installation and configuration
* **[AGENTS.md](AGENTS.md)** — Agent behavioral patterns and standards
* **[ADAPTATION_GUIDE.md](ADAPTATION_GUIDE.md)** — Changes from Claude Code
* **[.opencode/config.yaml](.opencode/config.yaml)** — System configuration

### Agent Standardization Project (In Progress)

* **[docs/agent-standardization-quickstart.md](docs/agent-standardization-quickstart.md)** — 📍 START HERE — Quick overview
* **[docs/agent-standardization-tracker.md](docs/agent-standardization-tracker.md)** — Progress dashboard (25% complete)
* **[docs/opencode-agent-standard.md](docs/opencode-agent-standard.md)** — Full specification
* **[docs/agent-system-review.md](docs/agent-system-review.md)** — Analysis of Claude Code
* **[docs/agent-format-compatibility.md](docs/agent-format-compatibility.md)** — Compatibility analysis
* **[docs/phase1-implementation-summary.md](docs/phase1-implementation-summary.md)** — ✅ Phase 1 complete
* **[docs/phase2-enforcement-patterns-plan.md](docs/phase2-enforcement-patterns-plan.md)** — 📋 Phase 2 plan

---

## 💡 Usage Examples

### Create AgentTask

```
@Project-Manager create AgentTask to implement JWT authentication
```

### Break Down Story

```
@Project-Manager analyze stories/STORY-001.md and create AgentTasks
```

### Implement Feature

```
@Developer implement agenttasks/AGENTTASK-001.yaml
```

### Search Memory

```
@Developer search memory for authentication patterns
```

### Add to Memory

```
@Developer store this JWT implementation pattern in memory
```

---

## ⚙️ Configuration

### OpenCode MCP Servers

Edit `opencode.jsonc`:

```jsonc
{
  "mcp": {
    "context7": {
      "type": "local",
      "command": ["npx", "-y", "@upstash/context7-mcp"],
      "enabled": true
    }
  }
}
```

### Agent System

Edit `.opencode/config.yaml`:

```yaml
agent_system:
  specialists:
    project-manager: { enabled: true }
    product-manager: { enabled: true }
    developer: { enabled: true }
    # ...
agenttask_system:
  complexity_tiers:
    medium: { min: 6, max: 15 }
```

### Behavioral Patterns

Edit `AGENTS.md`:

```markdown
## Code Standards
- Your conventions
- Your patterns
- Your quality gates
```

---

## 🌟 Benefits

### For Teams

* **Consistent Patterns:** Shared standards across roles
* **Knowledge Sharing:** Memory captures learnings
* **Clear Roles:** Project Manager vs Product Manager separation
* **Quality Built-In:** Validation and documentation enforced

### For Projects

* **Complexity Management:** Auto-sizing prevents overload
* **Context Preservation:** Full traceability in AgentTasks
* **Pattern Reuse:** Memory system prevents reinvention
* **Progressive Scaling:** Start small, grow safely

### For Development

* **Memory-First:** Leverage past solutions
* **Complete Context:** Everything embedded in tasks
* **Structured Workflow:** Templates ensure consistency
* **Quality Gates:** Testing and validation mandatory

---

## 🔄 Workflow

### Daily Usage

```
1. User requests feature
2. @Project-Manager analyzes and creates AgentTask
3. @Project-Manager delegates to specialist
4. Specialist searches memory
5. Specialist implements with context
6. Specialist validates and tests
7. Specialist stores learnings
8. Specialist provides summary
```

### Team Collaboration

```
1. Patterns stored in memory/
2. Committed to git
3. Pulled by team members
4. Reused in future work
5. Enhanced over time
```

---

## 🚧 Troubleshooting

**Agents not following patterns?**
→ Make instructions more explicit in AGENTS.md

**Memory not being used?**
→ Emphasize Memory-First workflow in agent definitions

**AgentTasks missing context?**
→ Use the full template, replace all placeholders

**Unclear complexity scoring?**
→ See calculation table in AGENTS.md

---

## 📖 Learn More

* **Original Project:** [intelligent-claude-code](https://github.com/intelligentcode-ai/intelligent-claude-code)
* **OpenCode:** [opencode.ai](https://opencode.ai)
* **MCP Servers:** [modelcontextprotocol.io](https://modelcontextprotocol.io)

---

## 🤝 Contributing

This is an adaptation for your project. Customize:

* Add agents to `.opencode/agents/`
* Create practices in `.opencode/patterns/`
* Build memory in `memory/`
* Share improvements with your team

---

## 📄 License

Based on [intelligent-claude-code](https://github.com/intelligentcode-ai/intelligent-claude-code)
Adapted for OpenCode

---

## 🎯 Next Steps

1. Read [SETUP.md](SETUP.md) for installation
2. Review [AGENTS.md](AGENTS.md) for behavioral patterns
3. Create your first AgentTask
4. Build your memory/ library
5. Customize for your team workflow

---

**Ready to start?**

```
@Project-Manager help
@Project-Manager create AgentTask for [your first task]
```