# OpenCode Agent-Based Development System

**Adapted from [intelligent-claude-code](https://github.com/intelligentcode-ai/intelligent-claude-code) for OpenCode**

Transform your OpenCode workspace into a 14-agent virtual development team with structured AgentTask execution, memory-first operations, and complexity-based work breakdown.

---

## 🚀 Quick Start

```bash
# 1. Review the setup
cat SETUP.md

# 2. Read behavioral patterns
cat AGENTS.md

# 3. Start using agents
@PM help
@PM create AgentTask for [your task]
@Developer implement [feature]
```

---

## ✨ What You Get

### 14 Specialist Agents
- **Leadership**: @PM, @Architect
- **Development**: @Developer, @AI-Engineer, @Database-Engineer
- **Operations**: @DevOps-Engineer, @System-Engineer
- **Quality**: @QA-Engineer, @Security-Engineer, @Backend-Tester
- **Design**: @Web-Designer, @Requirements-Engineer

### AgentTask System
- **Auto-Sizing**: Nano (0-2) → Tiny (3-5) → Medium (6-15) → Large (16-30) → Mega (30+)
- **Complete Context**: Embedded standards, patterns, examples
- **Memory-First**: Search before implement, store after solve
- **Quality Built-In**: Tests, validation, documentation required

### Memory System
- **Pattern Storage**: Reusable code patterns
- **Learning Capture**: Problem solutions
- **Knowledge Base**: Architecture decisions
- **Team Sharing**: Version-controlled via git

### Behavioral Patterns
- **Main Scope = Coordination**: PM creates AgentTasks
- **Specialists Execute**: Technical work delegated
- **Memory-First**: Always search before implementing
- **Quality Gates**: Comprehensive validation

---

## 📁 Repository Structure

```
.
├── .opencode/
│   ├── agents/           # 14 agent definitions
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
@PM analyzes complexity
  ↓
PM: 12 points = Medium AgentTask
PM: Searches memory for auth patterns
PM: Creates AgentTask with complete context
PM: @Developer execute AgentTask
  ↓
Developer: Implements using embedded patterns
Developer: Runs tests, provides summary
```

### 2. Large Work → Story Breakdown

```
User: "Build user management system"
  ↓
@PM breaks down work
  ↓
PM: 25 points = Large → Create Story
PM: Breaks into smaller AgentTasks:
    - Setup (2 pts) → @Developer
    - CRUD (5 pts) → @Developer
    - Tests (4 pts) → @QA-Engineer
PM: Coordinates execution
```

### 3. Memory-First Implementation

```
@Developer implement feature X
  ↓
Developer: Searches memory/Pattern/
Developer: Finds similar implementation
Developer: Applies pattern with context
Developer: Stores novel solution back to memory
```

---

## 🔧 Key Features

### Complexity-Based Sizing
Work is automatically categorized:

| Tier | Points | Description | Action |
|------|--------|-------------|--------|
| **Nano** | 0-2 | Trivial changes | Direct execution |
| **Tiny** | 3-5 | Simple tasks | Direct execution |
| **Medium** | 6-15 | Standard features | Direct execution |
| **Large** | 16-30 | Complex work | Create Story first |
| **Mega** | 30+ | System-wide | Create Story first |

### AgentTask Structure
Every AgentTask includes:
- **Goal**: What we're building
- **Why**: Business value
- **Context**: Complete embedded information
- **Implementation**: Step-by-step approach
- **Validation**: Success criteria and tests
- **Completion**: Deliverables and learnings

### Memory System
- **Before**: Search for patterns
- **During**: Apply discovered solutions
- **After**: Store new learnings
- **Share**: Via git with team

---

## 🎨 Adaptation from Claude Code

### What Changed
- **No Hooks**: Behavioral guidance instead of enforcement
- **Simpler Setup**: Manual instead of Ansible
- **Soft Enforcement**: Instructions instead of blocks
- **Full Tool Access**: Agents guided by patterns

### What Stayed
- **14 Agents**: All specialists preserved
- **AgentTask System**: Complete workflow
- **Memory System**: Pattern storage
- **Complexity Tiers**: Auto-sizing
- **Best Practices**: Auto-discovery

See `ADAPTATION_GUIDE.md` for complete details.

---

## 📚 Documentation

### Core Guides
- **[SETUP.md](SETUP.md)** - Installation and configuration
- **[AGENTS.md](AGENTS.md)** - Agent behavioral patterns and standards
- **[ADAPTATION_GUIDE.md](ADAPTATION_GUIDE.md)** - Changes from Claude Code
- **[.opencode/config.yaml](.opencode/config.yaml)** - System configuration

### Agent Standardization Project (In Progress)
- **[docs/agent-standardization-quickstart.md](docs/agent-standardization-quickstart.md)** - 📍 START HERE - Quick overview
- **[docs/agent-standardization-tracker.md](docs/agent-standardization-tracker.md)** - Progress dashboard (25% complete)
- **[docs/opencode-agent-standard.md](docs/opencode-agent-standard.md)** - Complete specification
- **[docs/agent-system-review.md](docs/agent-system-review.md)** - Analysis of intelligent-claude-code
- **[docs/agent-format-compatibility.md](docs/agent-format-compatibility.md)** - Compatibility analysis
- **[docs/phase1-implementation-summary.md](docs/phase1-implementation-summary.md)** - ✅ Phase 1 complete
- **[docs/phase2-enforcement-patterns-plan.md](docs/phase2-enforcement-patterns-plan.md)** - 📋 Phase 2 plan

---

## 💡 Usage Examples

### Create AgentTask
```
@PM create AgentTask to implement JWT authentication
```

### Break Down Story
```
@PM analyze stories/STORY-001.md and create AgentTasks
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
    pm: { enabled: true }
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
- **Consistent Patterns**: Everyone follows same standards
- **Knowledge Sharing**: Memory system captures learnings
- **Clear Roles**: Specialists have defined responsibilities
- **Quality Built-In**: Validation at every step

### For Projects
- **Complexity Management**: Auto-sizing prevents overwhelm
- **Context Preservation**: Everything documented in AgentTasks
- **Pattern Reuse**: Memory system prevents reinvention
- **Progressive Enhancement**: Start simple, scale up

### For Development
- **Memory-First**: Leverage past solutions
- **Complete Context**: Everything needed in AgentTask
- **Structured Work**: Templates guide execution
- **Quality Gates**: Tests and validation required

---

## 🔄 Workflow

### Daily Usage
```
1. User requests feature
2. @PM analyzes and creates AgentTask
3. @PM delegates to specialist
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
→ Emphasize memory-first in agent definitions

**AgentTasks missing context?**
→ Use templates completely, replace all placeholders

**Unclear complexity scoring?**
→ See calculation formula in AGENTS.md

---

## 📖 Learn More

- **Original Project**: [intelligent-claude-code](https://github.com/intelligentcode-ai/intelligent-claude-code)
- **OpenCode**: [opencode.ai](https://opencode.ai)
- **MCP Servers**: [modelcontextprotocol.io](https://modelcontextprotocol.io)

---

## 🤝 Contributing

This is an adaptation for your project. Customize:
- Add agents to `.opencode/agents/`
- Create practices in `.opencode/patterns/`
- Build memory in `memory/`
- Share improvements

---

## 📄 License

Based on [intelligent-claude-code](https://github.com/intelligentcode-ai/intelligent-claude-code)  
Adapted for OpenCode

---

## 🎯 Next Steps

1. Read [SETUP.md](SETUP.md) for installation
2. Review [AGENTS.md](AGENTS.md) for patterns
3. Try creating your first AgentTask
4. Build your memory/ with patterns
5. Customize for your workflow

---

**Ready to start?**
```
@PM help
@PM create AgentTask for [your first task]
```

---

**Version**: 1.0.0  
**Based on**: intelligent-claude-code v8.20.68  
**Adapted for**: OpenCode  
**Date**: 2025-11-08
