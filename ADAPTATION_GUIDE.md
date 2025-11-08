# OpenCode Adaptation Guide

## Overview
This repository adapts the [intelligent-claude-code](https://github.com/intelligentcode-ai/intelligent-claude-code) system from Claude Code to OpenCode. This guide explains the key differences and adaptations.

## Key Differences: Claude Code vs OpenCode

### 1. **Hook System**
- **Claude Code**: Extensive PreToolUse/PostToolUse hook system with 15+ hooks for enforcement
- **OpenCode**: No hook system - relies on agent behavioral patterns and instructions
- **Adaptation**: Convert enforcement hooks to behavioral guidance in agent prompts

### 2. **Agent System**
- **Claude Code**: Native subagent system with tool restrictions (Read, Write, Edit, Bash, Grep, Glob)
- **OpenCode**: Agent system with full tool access, focus on behavioral instructions
- **Adaptation**: Remove tool restrictions, embed behavioral guidance in agent definitions

### 3. **Configuration Structure**
- **Claude Code**: CLAUDE.md with complex nested YAML, .claude/ directory structure
- **OpenCode**: opencode.jsonc for configuration, simpler structure
- **Adaptation**: Simplified config focused on MCP and agent definitions

### 4. **Installation**
- **Claude Code**: Ansible playbooks for complex multi-file deployment
- **OpenCode**: Direct file placement in project, simpler setup
- **Adaptation**: Manual setup guide, no automation needed

### 5. **Enforcement Mechanisms**
- **Claude Code**: Hard enforcement via hooks (PM constraints, directory routing, etc.)
- **OpenCode**: Soft enforcement via agent instructions and best practices
- **Adaptation**: Convert blocking hooks to guidance patterns

## What Was Preserved

### ✅ Core Concepts Kept
1. **14 Specialist Agents**: PM, Architect, Developer, AI-Engineer, Database-Engineer, etc.
2. **AgentTask System**: Product Requirement Blueprints for structured work
3. **Memory System**: Topic-based learning storage and retrieval
4. **Complexity Tiers**: Nano/Tiny/Medium/Large/Mega based on scope
5. **Best Practices Auto-Discovery**: Dynamic injection of project standards

### ✅ Behavioral Patterns
1. **Main Scope = Coordination Only**: PM creates AgentTasks, agents execute
2. **File Location Standards**: Stories/bugs/memory/docs directory structure
3. **Git Privacy**: Strip AI mentions from commits
4. **Work Breakdown**: Large tasks → Stories → AgentTasks

## What Was Changed

### 🔄 Major Adaptations

#### 1. No Hook System
**Before (Claude Code)**:
```javascript
// src/hooks/pm-constraints-enforcement.js
// Blocks PM from running technical commands
if (isPMRole && isTechnicalCommand) {
  blockOperation("PM must create AgentTasks");
}
```

**After (OpenCode)**:
```markdown
# In agent definitions
## PM Role Constraints
You operate in coordination-only mode:
- ❌ DO NOT run technical commands directly
- ✅ DO create AgentTasks for specialists
- ✅ DO coordinate between agents
```

#### 2. Agent Tool Access
**Before (Claude Code)**:
```markdown
---
tools: Read, Write, Edit, Bash, Grep, Glob, LS
---
```

**After (OpenCode)**:
```markdown
# Agents have full tool access, guided by behavioral patterns
## Tool Usage Guidelines
- Use Read/Write/Edit for file operations
- Use Bash for system commands
- Check memory before implementation
```

#### 3. Configuration
**Before (Claude Code)**:
```yaml
# CLAUDE.md
agent_configuration:
  specialist_creation: true
  expertise_threshold: "when_needed"
workflow_settings:
  tiny:
    version_bump: true
    pr_required: false
```

**After (OpenCode)**:
```jsonc
// opencode.jsonc
{
  "agents": {
    "pm": { "enabled": true },
    "developer": { "enabled": true }
  },
  "workflow": {
    "complexity_thresholds": {
      "tiny": 5,
      "medium": 15
    }
  }
}
```

#### 4. Installation
**Before (Claude Code)**:
```bash
make install  # Ansible playbook deploys to ~/.claude/
```

**After (OpenCode)**:
```bash
# Manual setup
cp agents/*.md .opencode/agents/
cp opencode.jsonc ./
# Update AGENTS.md with patterns
```

## Architecture Changes

### Directory Structure

**Claude Code**:
```
~/.claude/                    # Global installation
├── modes/
├── agents/                   # 14 agent definitions
├── behaviors/                # 50+ behavioral patterns
├── hooks/                    # 15+ enforcement hooks
├── agenttask-templates/      # 5 template files
└── settings.json             # Hook registration

project/
├── CLAUDE.md                 # Project config
├── memory/                   # Learning storage
└── .claude/prbs/             # Generated AgentTasks
```

**OpenCode**:
```
project/
├── opencode.jsonc            # Project config
├── AGENTS.md                 # Agent behavioral guide
├── .opencode/
│   ├── agents/               # Agent definitions
│   └── patterns/             # Behavioral patterns
├── memory/                   # Learning storage
├── agenttask-templates/      # Templates
└── stories/                  # Work breakdown
```

### Agent Communication

**Claude Code**:
```
User → PM (main scope)
  ↓
PM creates AgentTask
  ↓
PM invokes: Task tool → @Developer (subagent)
  ↓
Developer executes with enforced tool restrictions
  ↓
Hooks enforce: directory routing, PM constraints, etc.
```

**OpenCode**:
```
User → PM agent
  ↓
PM creates AgentTask
  ↓
PM delegates to @Developer agent
  ↓
Developer executes following behavioral guidance
  ↓
Self-enforced: directory standards, constraints via instructions
```

## Migration Path

### For Users Migrating from Claude Code

1. **Export Memory**: Copy your `memory/` directory
2. **Review AgentTasks**: Existing .yaml files work with minor updates
3. **Adapt Workflows**: Hook-enforced behaviors become documented patterns
4. **Update Config**: Convert CLAUDE.md → opencode.jsonc + AGENTS.md

### For New OpenCode Users

1. **Start Fresh**: Clone this adapted repository
2. **Configure**: Edit opencode.jsonc for your project
3. **Customize Agents**: Adjust agent definitions in .opencode/agents/
4. **Build Memory**: Create memory/ with your patterns

## Behavioral Pattern Translation

### Main Scope Enforcement
**Claude Code** (Hook): Blocks non-coordination commands in PM role
**OpenCode** (Pattern): Agent instructions emphasize coordination-only

### Directory Routing  
**Claude Code** (Hook): Automatically routes files to correct directories
**OpenCode** (Pattern): File location standards in documentation

### Git Privacy
**Claude Code** (Hook): Strips AI mentions from commits
**OpenCode** (Pattern): Pre-commit reminder in documentation

### PM Constraints
**Claude Code** (Hook): Prevents PM from technical operations
**OpenCode** (Pattern): PM agent definition emphasizes delegation

## Benefits of OpenCode Adaptation

### ✅ Advantages
1. **Simpler Setup**: No Ansible, no complex installation
2. **More Flexible**: Agents can adapt behavior without hook changes
3. **Easier Debugging**: No hidden hook enforcement, clear instructions
4. **Portable**: Works across different environments without installation
5. **Transparent**: All behavior is documented and visible

### ⚠️ Trade-offs
1. **Softer Enforcement**: Relies on agent following instructions
2. **No Hard Blocks**: Can't prevent operations, only guide
3. **More Manual**: Some automation (like directory routing) becomes guidance
4. **Requires Discipline**: Team must follow documented patterns

## Best Practices for OpenCode Version

### 1. Clear Agent Instructions
Make behavioral patterns explicit in agent definitions:
```markdown
## You MUST Always
- Check memory before implementing new patterns
- Follow file location standards (stories/, memory/, docs/)
- Create AgentTasks for complexity > 5 points

## You MUST NEVER
- Implement without searching memory first
- Create files outside designated directories
- Execute work assigned to other specialist roles
```

### 2. Documentation Over Enforcement
Since we can't enforce via hooks, documentation is critical:
- Keep AGENTS.md updated with patterns
- Document file location rules clearly
- Provide examples of correct behavior

### 3. Memory-First Culture
Emphasize memory usage in every agent:
```markdown
## Before ANY Implementation
1. Search memory for existing patterns
2. Review similar past solutions
3. Check for known issues or gotchas
4. Store new learnings after completion
```

### 4. AgentTask Discipline
Maintain structured work even without enforcement:
- Use templates for consistency
- Embed complete context
- Include validation criteria
- Document completion

## Future Enhancements

### Potential OpenCode Features
1. **MCP-based Enforcement**: Custom MCP server for validation
2. **Pre-commit Hooks**: Local git hooks for pattern enforcement
3. **Linting Tools**: Static analysis for AgentTask compliance
4. **Agent Metrics**: Track adherence to behavioral patterns

### Community Contributions
- Share memory patterns
- Improve agent definitions
- Create domain-specific specialists
- Build OpenCode-native tools

## Support and Resources

- **Original Project**: https://github.com/intelligentcode-ai/intelligent-claude-code
- **OpenCode Docs**: https://opencode.ai/docs
- **Issues/Discussions**: See repository

---

**Version**: 1.0.0  
**Last Updated**: 2025-11-08  
**Based on**: intelligent-claude-code v8.20.68
