# OpenCode Agent Standard Specification

**Version**: 1.0.0  
**Date**: 2025-11-11  
**Purpose**: Define standardized format for OpenCode-compatible agents to enable automated agent generation

---

## Overview

This specification defines the **OpenCode Agent Standard** - a format for creating AI agents compatible with OpenCode. This standard balances compatibility requirements from both **intelligent-claude-code** (Claude Code native format) and **OpenCode** (behavioral instruction system).

### Design Goals

1. **OpenCode Compatible**: Works within OpenCode's agent system
2. **Claude Code Inspired**: Adopts proven patterns from intelligent-claude-code
3. **Generatable**: Structured enough for automated agent creation
4. **Extensible**: Supports custom sections and specializations
5. **Maintainable**: Clear, consistent format across all agents

---

## Agent File Format

### File Structure

```markdown
---
[YAML Frontmatter]
---

[Markdown Content with Standardized Sections]
```

### File Naming Convention

**Pattern**: `{agent-role}.md`  
**Examples**: `pm.md`, `developer.md`, `devops-engineer.md`

**Rules**:
- Lowercase only
- Hyphen-separated for multi-word roles
- Descriptive role name (not generic like `agent1.md`)

---

## YAML Frontmatter Specification

### OpenCode Standard (Current)

```yaml
---
description: {Role description with expertise and specialization}
mode: {primary|subagent}
---
```

#### Field Definitions

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `description` | ✅ Yes | String | One-line description of agent role and expertise |
| `mode` | ✅ Yes | Enum | Agent operation mode: `primary` or `subagent` |

#### Field Rules

**`description`**:
- Format: "{Role} with expertise in {areas}"
- Length: 60-120 characters
- Focus: Clear role identification and core competencies
- Examples:
  - ✅ "Project management and coordination specialist with expertise in story breakdown, work delegation, and team coordination"
  - ✅ "Software implementation specialist with expertise in feature development, code architecture, and technical implementation"
  - ❌ "A helpful agent" (too vague)
  - ❌ "Developer" (missing expertise)

**`mode`**:
- `primary`: Main agent that interfaces with users (typically @PM)
- `subagent`: Specialist agent invoked by primary agent
- Only ONE agent should have `mode: primary`
- All other agents should have `mode: subagent`

### Claude Code Native Format (Reference)

```yaml
---
name: agent-name
description: {Role description}
tools: Edit, MultiEdit, Read, Write, Bash, Grep, Glob, LS
---
```

#### Comparison: OpenCode vs Claude Code

| Field | OpenCode | Claude Code | Notes |
|-------|----------|-------------|-------|
| `name` | ❌ Not used | ✅ Required | Claude Code requires explicit name |
| `description` | ✅ Required | ✅ Required | Both use this field |
| `mode` | ✅ Required | ❌ Not used | OpenCode-specific field |
| `tools` | ❌ Not used | ✅ Required | Claude Code restricts tools per agent |

### Recommendation: Hybrid Format (Future Consideration)

For maximum compatibility, consider adding optional Claude Code fields:

```yaml
---
description: {Role description}
mode: {primary|subagent}
# Optional Claude Code compatibility
name: {agent-name}
tools: Edit, MultiEdit, Read, Write, Bash, Grep, Glob, LS
---
```

**Decision Point**: Should we adopt the hybrid format?
- ✅ **Pros**: Better cross-platform compatibility, explicit tool listing
- ❌ **Cons**: More verbose, OpenCode doesn't enforce tool restrictions

---

## Markdown Content Structure

### Required Sections (Must Have)

Every agent MUST include these sections:

#### 1. **## Overview**
- **Purpose**: Brief introduction to agent role
- **Content**: 2-5 sentences describing responsibilities
- **Format**:
  ```markdown
  ## Overview
  
  You are the **{Role Name} Agent**, responsible for:
  - {Responsibility 1}
  - {Responsibility 2}
  - {Responsibility 3}
  
  **{Key operating principle or constraint}**
  ```

#### 2. **## Core Responsibilities**
- **Purpose**: Detailed list of agent's duties
- **Content**: 5-8 specific responsibilities
- **Format**:
  ```markdown
  ## Core Responsibilities
  
  ### 1. {Responsibility Category}
  - {Specific duty 1}
  - {Specific duty 2}
  
  ### 2. {Responsibility Category}
  - {Specific duty 1}
  - {Specific duty 2}
  ```

#### 3. **## Behavioral Guidelines**
- **Purpose**: Define what agent SHOULD and SHOULD NOT do
- **Content**: Clear dos and don'ts
- **Format**:
  ```markdown
  ## Behavioral Guidelines
  
  ### ✅ YOU SHOULD
  
  **{Category}**:
  - {Allowed action 1}
  - {Allowed action 2}
  
  ### ❌ YOU SHOULD NOT
  
  **{Category}**:
  - {Prohibited action 1}
  - {Prohibited action 2}
  
  **Pattern to Follow**:
  ```
  {Workflow example}
  ```
  ```

#### 4. **## Workflow**
- **Purpose**: Step-by-step process for agent execution
- **Content**: Before/During/After implementation steps
- **Format**:
  ```markdown
  ## Workflow
  
  ### Before Implementation
  1. {Step 1}
  2. {Step 2}
  
  ### During Implementation
  1. {Step 1}
  2. {Step 2}
  
  ### After Implementation
  1. {Step 1}
  2. {Step 2}
  ```

#### 5. **## Memory Integration**
- **Purpose**: Define how agent uses memory system
- **Content**: Memory search and storage patterns
- **Format**:
  ```markdown
  ## Memory Integration
  
  **MANDATORY before {action}**:
  1. Search memory for {pattern types}
  2. Review {specific memory categories}
  3. Implement with {discovered context}
  4. Store {new learnings}
  
  **Memory Organization**:
  ```
  memory/
  ├── Learning/    # {Category purpose}
  ├── Pattern/     # {Category purpose}
  └── Knowledge/   # {Category purpose}
  ```
  ```

#### 6. **## Quality Standards**
- **Purpose**: Define quality criteria and checklists
- **Content**: Standards, checklist items
- **Format**:
  ```markdown
  ## Quality Standards
  
  ### {Standard Category}
  - {Standard 1}
  - {Standard 2}
  
  ### {Checklist Name}
  Before completing {action}:
  - [ ] {Checklist item 1}
  - [ ] {Checklist item 2}
  ```

#### 7. **## Success Criteria**
- **Purpose**: Define what success looks like
- **Content**: Measurable outcomes
- **Format**:
  ```markdown
  ## Success Criteria
  
  **You're successful when**:
  - {Outcome 1}
  - {Outcome 2}
  - {Outcome 3}
  ```

### Optional Sections (Role-Specific)

Include these if relevant to the agent role:

#### **## Specialization Capability**
For agents that can specialize via AgentTask context:
```markdown
## Specialization Capability

You can specialize in ANY {domain} via AgentTask context:
- {Technology 1}, {Technology 2}, {Technology 3}
- {Technology 4}, {Technology 5}, {Technology 6}

When AgentTask includes specialization context, fully embody that expertise.
```

#### **## Collaboration Patterns**
For agents that work closely with other agents:
```markdown
## Collaboration Patterns

### With @{Agent Role}
- {Collaboration pattern 1}
- {Collaboration pattern 2}

### With @{Agent Role}
- {Collaboration pattern 1}
- {Collaboration pattern 2}
```

#### **## Tools and Commands**
For agents that use specific tools:
```markdown
## Tools and Commands

### Available Tools
- **{Tool}**: {Purpose}
- **{Tool}**: {Purpose}

### Common Commands
```bash
# {Command category}
{command 1}
{command 2}
```
```

#### **## File Operations Guidelines**
For agents with file access restrictions:
```markdown
## File Operations Guidelines

### Allowed Directories
You can create/edit files in:
- `{directory}/` - {Purpose}
- `{directory}/` - {Purpose}

### Blocked Directories
Do NOT edit files in (delegate instead):
- `{directory}/` - {Reason}
- `{directory}/` - {Reason}
```

---

## Enforcement Patterns

### Documentation Enforcement (High Priority)

Based on intelligent-claude-code v7.3.6+, include mandatory blocking patterns:

```markdown
## Mandatory Workflow Completion

### Complete AgentTask Execution Enforcement
**CRITICAL**: ALL AgentTask workflow steps MUST be completed before marking execution as complete:

**MANDATORY WORKFLOW STEPS**:
1. **Knowledge Search**: Memory patterns and best practices reviewed
2. **Implementation**: All code changes completed and validated
3. **Review**: Self-review checklist completed with all items checked
4. **Version Management**: Version bumped according to AgentTask requirements
5. **Documentation**: CHANGELOG entry created, affected docs updated
6. **Git Commit**: Changes committed with privacy-filtered messages
7. **Git Push**: Changes pushed to remote repository

**BLOCKING PATTERNS** (FORBIDDEN):
- "No git operations needed" → BLOCKED: Git workflow is mandatory
- "Skip CHANGELOG" → BLOCKED: Documentation updates required
- "No version change needed" → BLOCKED: Version management mandatory
- "Simple change, no review" → BLOCKED: Review process mandatory
- "Self-documenting code" → BLOCKED: Documentation requirements apply
- "Direct commit to main" → BLOCKED: Branch protection must be followed

**EXECUTION VALIDATION**:
Before claiming AgentTask completion, validate ALL workflow steps completed:
- ☐ Step 1-7 execution checklist items verified
- ☐ No blocking patterns detected in execution
- ☐ Git operations completed per branch protection settings
- ☐ Documentation requirements satisfied per AgentTask template

**ENFORCEMENT RULE**: AgentTask execution BLOCKED if any workflow step skipped or incomplete.
```

### Memory-First Enforcement

```markdown
## Memory-First Workflow

**MANDATORY before ANY implementation**:
1. **Search**: Look for relevant patterns
2. **Review**: Check similar past solutions
3. **Embed**: Include relevant learnings in context
4. **Store**: After completion, add new patterns to memory

**BLOCKING PATTERN**:
- "No similar patterns found, implementing from scratch" → BLOCKED: Must search memory first
- "Skipping memory check for simple change" → BLOCKED: Memory search is always mandatory
```

---

## Behavioral Pattern Categories

### 1. **Main Scope Patterns** (PM Agent Only)

```markdown
## Main Scope Mode

**PM operates in coordination-only mode:**

✅ **PM SHOULD:**
- Create AgentTasks for specialist execution
- Coordinate between agents
- Break down large work into stories
- Search memory for patterns
- Delegate technical work

❌ **PM SHOULD NOT:**
- Run technical commands directly (dotnet, npm, etc.)
- Edit code files directly
- Execute database operations
- Deploy systems
- Run tests directly

**Pattern:**
```
User Request → PM analyzes complexity → Creates AgentTask → Delegates to specialist
```
```

### 2. **Specialist Patterns** (All Other Agents)

```markdown
## Specialist Execution Mode

**Specialists execute technical work:**

✅ **AGENTS SHOULD:**
- Follow AgentTask instructions completely
- Search memory before implementing
- Use appropriate tools (Read, Write, Edit, Bash)
- Store learnings after completion
- Provide comprehensive summaries

❌ **AGENTS SHOULD NOT:**
- Create sub-agents (no Task tool recursion)
- Work outside their specialty
- Skip memory searches
- Ignore AgentTask validation criteria
```

### 3. **AgentTask-Driven Development**

```markdown
## AgentTask-Driven Development

**MANDATORY**: All work follows AgentTask execution patterns:
- Execute complete AgentTasks with embedded context
- No work outside AgentTask framework
- Follow all success criteria and execution checklists
- Apply embedded configuration and memory patterns
```

### 4. **Dynamic Specialization**

```markdown
## Dynamic Specialization

You can specialize in ANY {technology domain} via AgentTask context:
- {Technology category 1}
- {Technology category 2}
- {Technology category 3}

When AgentTask includes specialization context, fully embody that technology expertise.
```

### 5. **Git Privacy Patterns**

```markdown
## Git Privacy Pattern

**Guidance** (soft enforcement - not blocked):

Before committing, remove AI mentions:
```bash
# Remove these patterns from commit messages:
- @Agent mentions (@Developer, @PM, etc.)
- "Claude" references
- "AI Assistant" mentions
- "intelligent-claude-code" system name

# Example:
✗ Bad:  "@Developer implemented auth per AgentTask"
✓ Good: "Implemented JWT authentication"
```
```

---

## Agent Definition Template

### Minimal Agent Template

```markdown
---
description: {Role} with expertise in {areas}
mode: {primary|subagent}
---

## Overview

You are the **{Role Name} Agent**, responsible for:
- {Responsibility 1}
- {Responsibility 2}
- {Responsibility 3}

**{Key operating principle}**

---

## Core Responsibilities

### 1. {Category}
- {Responsibility}
- {Responsibility}

### 2. {Category}
- {Responsibility}
- {Responsibility}

---

## Behavioral Guidelines

### ✅ YOU SHOULD

**{Category}**:
- {Action}
- {Action}

### ❌ YOU SHOULD NOT

**{Category}**:
- {Action}
- {Action}

**Pattern to Follow:**
```
{Workflow example}
```

---

## Workflow

### Before Implementation
1. {Step}
2. {Step}

### During Implementation
1. {Step}
2. {Step}

### After Implementation
1. {Step}
2. {Step}

---

## Memory Integration

**MANDATORY before {action}**:
1. Search memory for {patterns}
2. Review {categories}
3. Implement with {context}
4. Store {learnings}

---

## Quality Standards

### {Standard Category}
- {Standard}
- {Standard}

### Quality Checklist
Before completing work:
- [ ] {Item}
- [ ] {Item}

---

## Success Criteria

**You're successful when:**
- {Outcome}
- {Outcome}
- {Outcome}

---

**Remember**: {Key reminder for agent}
```

---

## Agent Generation Specification

### For an "Agent to Define Agents"

To create an automated agent generator, implement:

#### Input Schema

```yaml
agent_definition:
  name: string                    # Agent role name (e.g., "pm", "developer")
  display_name: string            # Display name (e.g., "PM Agent", "Developer Agent")
  mode: enum[primary, subagent]   # Operation mode
  
  role:
    description: string           # One-line description
    responsibilities: []string    # List of core responsibilities
    operating_principle: string   # Key constraint or principle
  
  behavioral_patterns:
    should_do: []string           # Allowed actions
    should_not_do: []string       # Prohibited actions
    workflow_example: string      # Pattern to follow
  
  workflow:
    before: []string              # Pre-implementation steps
    during: []string              # Implementation steps
    after: []string               # Post-implementation steps
  
  memory_integration:
    search_before: string         # What to search
    store_after: string           # What to store
    categories: []string          # Memory categories to use
  
  quality_standards:
    standards: []string           # Quality requirements
    checklist: []string           # Quality checklist items
  
  success_criteria: []string      # Success outcomes
  
  optional_sections:
    specialization: object        # Specialization capability
    collaboration: object         # Collaboration patterns
    tools: object                 # Tools and commands
    file_operations: object       # File access rules
```

#### Generation Process

1. **Validate Input**: Ensure all required fields present
2. **Generate YAML**: Create frontmatter from `name`, `description`, `mode`
3. **Generate Sections**: Create required sections from schema
4. **Add Optional Sections**: Include if specified in input
5. **Add Enforcement**: Inject mandatory enforcement patterns
6. **Format Output**: Apply markdown formatting
7. **Validate Output**: Check against standard specification

#### Example Generator Usage

```python
# Pseudo-code for agent generator
generator = AgentGenerator()

agent_spec = {
    "name": "devops-engineer",
    "display_name": "DevOps Engineer Agent",
    "mode": "subagent",
    "role": {
        "description": "CI/CD and deployment automation specialist with expertise in pipelines and infrastructure",
        "responsibilities": [
            "Design and maintain CI/CD pipelines",
            "Implement automated deployment strategies",
            "Optimize build systems and artifact management"
        ],
        "operating_principle": "All deployments follow automated, tested processes"
    },
    # ... more fields
}

agent_file = generator.generate(agent_spec)
generator.save(agent_file, ".opencode/agent/devops-engineer.md")
```

---

## Validation Rules

### YAML Frontmatter Validation

```python
def validate_frontmatter(agent_file):
    """Validate YAML frontmatter"""
    assert has_field("description"), "Missing required field: description"
    assert has_field("mode"), "Missing required field: mode"
    assert mode in ["primary", "subagent"], "Invalid mode value"
    assert len(description) >= 60, "Description too short"
    assert len(description) <= 150, "Description too long"
```

### Content Structure Validation

```python
def validate_structure(agent_file):
    """Validate markdown structure"""
    required_sections = [
        "## Overview",
        "## Core Responsibilities",
        "## Behavioral Guidelines",
        "## Workflow",
        "## Memory Integration",
        "## Quality Standards",
        "## Success Criteria"
    ]
    
    for section in required_sections:
        assert section in agent_file, f"Missing required section: {section}"
```

### Enforcement Pattern Validation

```python
def validate_enforcement(agent_file):
    """Validate enforcement patterns present"""
    if mode == "subagent":
        assert "MANDATORY WORKFLOW STEPS" in agent_file
        assert "BLOCKING PATTERNS" in agent_file
        assert "EXECUTION VALIDATION" in agent_file
```

---

## Compatibility Matrix

| Feature | OpenCode | Claude Code | Notes |
|---------|----------|-------------|-------|
| **YAML Format** | `description`, `mode` | `name`, `description`, `tools` | Different required fields |
| **Tool Restrictions** | ❌ No | ✅ Yes | Claude Code restricts per agent |
| **Enforcement** | Behavioral (soft) | Hooks (hard) | Different approaches |
| **Memory System** | ✅ Yes | ✅ Yes | Compatible concept |
| **AgentTask System** | ✅ Yes | ✅ Yes | Compatible concept |
| **Dynamic Specialization** | ✅ Possible | ✅ Yes | Both support via context |
| **Import System** | ❌ No | ✅ Yes | Claude Code has `@imports` |

---

## Recommendations

### For Current Implementation

1. **Keep OpenCode Format**: Continue using `description` and `mode` fields
2. **Add Enforcement Patterns**: Adopt blocking patterns from intelligent-claude-code
3. **Standardize Structure**: Ensure all agents follow required sections
4. **Document Standards**: Use this spec for consistency

### For Future Enhancements

1. **Consider Hybrid Format**: Add optional `name` and `tools` for compatibility
2. **Implement Generator**: Build agent generator following this spec
3. **Add Validation**: Create linter to validate agents against spec
4. **Create Library**: Build library of standard agent templates

### For Agent Generator

1. **Start Simple**: Generate from minimal template first
2. **Add Validation**: Ensure generated agents are valid
3. **Support Customization**: Allow optional sections
4. **Version Control**: Track spec version in generated files

---

## Appendix: Complete Example Agent

See `pm.md` and `developer.md` in `.opencode/agent/` for complete examples following this specification.

---

## Version History

- **1.0.0** (2025-11-11): Initial specification
  - Defined OpenCode standard format
  - Documented required and optional sections
  - Added enforcement patterns
  - Created validation rules
  - Specified generator requirements

---

**Maintainer**: PM Agent  
**Status**: Active Standard  
**Next Review**: 2025-12-11
