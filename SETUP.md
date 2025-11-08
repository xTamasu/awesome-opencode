# OpenCode Setup Guide
# Intelligent-Claude-Code Adaptation for OpenCode

## Quick Start

```bash
# 1. Repository is already set up with structure
# 2. Review configuration
cat .opencode/config.yaml
cat AGENTS.md

# 3. Create your first AgentTask
# See examples in agenttask-templates/

# 4. Start using agents
@PM help
@Developer implement [feature]
```

## What's Included

This repository includes an adapted version of [intelligent-claude-code](https://github.com/intelligentcode-ai/intelligent-claude-code) for OpenCode:

✅ **14 Specialist Agents** (PM, Architect, Developer, etc.)  
✅ **AgentTask System** (Nano/Tiny/Medium/Large/Mega templates)  
✅ **Memory System** (Pattern/Learning/Knowledge storage)  
✅ **Behavioral Patterns** (Guidance without hooks)  
✅ **Best Practices** (Auto-discovery system)

## Directory Structure

```
project/
├── .opencode/
│   ├── agents/              # Agent definitions
│   │   ├── pm.md           # Project Manager
│   │   ├── developer.md    # Developer
│   │   └── ...             # More agents
│   ├── patterns/           # Best practices (add your own)
│   └── config.yaml         # System configuration
│
├── agenttask-templates/
│   ├── nano-agenttask-template.yaml      # 0-2 points
│   ├── tiny-agenttask-template.yaml      # 3-5 points
│   ├── medium-agenttask-template.yaml    # 6-15 points
│   ├── large-agenttask-template.yaml     # 16-30 points
│   └── mega-agenttask-template.yaml      # 30+ points
│
├── memory/                 # Learning storage
│   ├── Pattern/           # Reusable patterns
│   ├── Learning/          # Problem solutions
│   ├── Knowledge/         # Architecture decisions
│   └── Debugging/         # Troubleshooting
│
├── stories/               # User stories (≥16 pts)
├── summaries/             # Completion reports
├── docs/                  # Documentation
│
├── opencode.jsonc         # OpenCode + MCP config
├── AGENTS.md              # Agent behavioral guide
├── ADAPTATION_GUIDE.md    # What changed from Claude Code
└── SETUP.md              # This file
```

## Installation Steps

### 1. OpenCode Configuration

The `opencode.jsonc` file configures MCP servers:

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

**To add more MCP servers:**
```jsonc
{
  "mcp": {
    "context7": { ... },
    "filesystem": {
      "type": "local",
      "command": ["node", "path/to/filesystem-server.js"],
      "enabled": true
    }
  }
}
```

### 2. Agent System Configuration

Review and customize `.opencode/config.yaml`:

```yaml
# Enable/disable agents
agent_system:
  specialists:
    pm: { enabled: true }
    developer: { enabled: true }
    # ...

# Complexity thresholds
agenttask_system:
  complexity_tiers:
    nano: { points: "0-2" }
    tiny: { points: "3-5" }
    # ...

# Memory configuration
memory_system:
  directory: memory
  auto_search_before_implementation: true
```

### 3. Behavioral Patterns

`AGENTS.md` contains all behavioral patterns:

- Agent responsibilities
- Workflow patterns
- Code standards
- Quality checklists

**To customize:**
```bash
# Edit behavioral patterns
nano AGENTS.md

# Add project-specific standards
# Update code style rules
# Add quality gates
```

### 4. Best Practices

Add project-specific best practices to `.opencode/patterns/`:

```bash
# Create category directories
mkdir -p .opencode/patterns/{development,architecture,operations,security}

# Add practice files
cat > .opencode/patterns/development/tdd-practices.md << 'EOF'
# Test-Driven Development

**Type:** development
**Applies To:** tiny, medium, large
**Keywords:** testing, tdd, unit-tests

## Description
Write tests before implementation

## Implementation
1. Write failing test
2. Implement minimal code
3. Refactor

## Quality Gates
- [ ] Test written first
- [ ] Test fails initially
- [ ] Implementation passes test
EOF
```

### 5. Memory System

Initialize memory directories:

```bash
# Directories already created
ls memory/

# Add your first pattern
cat > memory/Pattern/example.md << 'EOF'
# Example Pattern

## Context
When you need to do X

## Solution
Use approach Y

## Example
```code
// Example implementation
```
## Gotchas
- Watch out for Z
EOF
```

## Usage Patterns

### 1. User Request → AgentTask

```
User: "Add authentication to the API"
  ↓
@PM analyze and create AgentTask
  ↓
PM: Analyzes complexity (12 points = Medium)
PM: Searches memory for auth patterns
PM: Creates medium-agenttask.yaml with complete context
PM: @Developer execute AgentTask
  ↓
Developer: Implements following embedded context
Developer: Provides comprehensive summary
```

### 2. Large Work → Story Breakdown

```
User: "Build complete user management system"
  ↓
@PM break down into story
  ↓
PM: Analyzes (25 points = Large)
PM: Creates STORY-001-user-management.md
PM: Breaks into smaller AgentTasks:
    - NANO: Setup user model (2 pts)
    - TINY: CRUD endpoints (5 pts)
    - TINY: Validation (4 pts)
    - TINY: Tests (5 pts)
PM: Delegates each to specialists
```

### 3. Memory-First Implementation

```
@Developer implement JWT auth
  ↓
Developer: Searches memory
Developer: Finds memory/Pattern/auth-jwt.md
Developer: Implements using pattern
Developer: Adds tests
Developer: Stores gotchas in memory/Learning/
```

## Customization

### Adding New Agents

Create new agent definition in `.opencode/agents/`:

```markdown
# Custom Agent

**Role**: [Role description]
**Specialization**: [What they specialize in]

## Overview
[Agent description]

## Responsibilities
- [Responsibility 1]
- [Responsibility 2]

## Workflow
[How they work]

## Standards
[Quality standards]
```

Then add to `.opencode/config.yaml`:

```yaml
agent_system:
  specialists:
    custom-agent:
      enabled: true
      priority: 3
      role: "Custom specialist"
```

### Customizing AgentTask Templates

Copy and modify templates:

```bash
cp agenttask-templates/medium-agenttask-template.yaml \
   agenttask-templates/custom-template.yaml

# Edit for your needs
nano agenttask-templates/custom-template.yaml
```

### Adding Code Standards

Update `AGENTS.md`:

```markdown
## Code Standards

### Your Language
**Naming:**
- YourConvention: classes

**Patterns:**
- Your patterns here

**Formatting:**
- Your rules
```

## Differences from Claude Code

This OpenCode adaptation differs from the original:

### ❌ Removed
- Hook system (PreToolUse/PostToolUse enforcement)
- Ansible playbooks (complex installation)
- Hard enforcement mechanisms
- Tool restrictions on agents

### ✅ Changed to
- Behavioral guidance (soft enforcement)
- Manual setup (simple installation)
- Agent instructions (guidance patterns)
- Full tool access (guided by behavior)

### ✅ Preserved
- 14 specialist agents
- AgentTask system
- Memory system
- Complexity tiers
- Best practices auto-discovery

See `ADAPTATION_GUIDE.md` for complete details.

## Troubleshooting

### Agents Not Following Patterns

**Issue**: Agents not following behavioral guidelines  
**Solution**: 
- Make patterns more explicit in AGENTS.md
- Add examples of correct behavior
- Include failure examples to avoid

### Memory Not Being Used

**Issue**: Patterns in memory/ not being applied  
**Solution**:
- Emphasize memory-first in agent definitions
- Add memory search to AgentTask templates
- Make memory location explicit

### AgentTasks Missing Context

**Issue**: AgentTasks lack needed information  
**Solution**:
- Use templates completely
- Replace all {PLACEHOLDERS}
- Embed standards from AGENTS.md
- Include memory search results

### Complexity Calculation Unclear

**Issue**: Unclear how to score work  
**Solution**: Use calculation formula:
```
File Impact (0-10) + 
Code Volume (0-10) + 
Integrations (0-5) + 
Security (0-3) + 
Coordination (0-2) = 
Total (0-30)
```

## Best Practices

### 1. Keep AGENTS.md Updated
- Update when patterns change
- Add new learnings
- Remove outdated guidance

### 2. Use Memory Actively
- Search before implementing
- Store novel solutions
- Share team learnings

### 3. Create Complete AgentTasks
- No placeholders
- Embedded context
- Clear success criteria

### 4. Follow Git Privacy
- Remove AI mentions from commits
- Clean commit messages
- Descriptive not mechanical

### 5. Build Best Practices Library
- Add to .opencode/patterns/
- Organize by category
- Make discoverable

## Getting Help

### Resources
- **Adaptation Guide**: `ADAPTATION_GUIDE.md`
- **Agent Patterns**: `AGENTS.md`
- **Configuration**: `.opencode/config.yaml`
- **Templates**: `agenttask-templates/`
- **Original Project**: https://github.com/intelligentcode-ai/intelligent-claude-code

### Common Questions

**Q: How do I enforce patterns without hooks?**  
A: Make them explicit in agent definitions. Use examples. Emphasize in instructions.

**Q: Can I add hook-like enforcement?**  
A: Yes, via custom MCP server or git pre-commit hooks (not included).

**Q: How do I share memory with team?**  
A: Commit memory/ directory to git. Team gets shared patterns.

**Q: What if agents ignore instructions?**  
A: Make instructions more explicit. Add examples. Emphasize MUST/MUST NOT.

## Next Steps

1. ✅ Review AGENTS.md behavioral patterns
2. ✅ Customize .opencode/config.yaml for your project
3. ✅ Add project-specific best practices to .opencode/patterns/
4. ✅ Start with simple AgentTask to test system
5. ✅ Build memory/ with your patterns
6. ✅ Iterate and improve based on what works

## Examples

See `ADAPTATION_GUIDE.md` for examples of:
- AgentTask creation
- Memory storage
- Agent communication
- Story breakdown

---

**Ready to start?** Try:
```
@PM help
@PM create AgentTask for [simple task]
```
