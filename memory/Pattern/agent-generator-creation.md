# Pattern: Agent-Generator Agent Creation

**Category**: Agent System Design  
**Created**: 2025-11-11  
**Context**: Phase 4 - Agent Generator Implementation

---

## Pattern Overview

Successfully created an **Agent-Generator Agent** - a meta-agent that can create other agents from YAML specifications following the OpenCode Agent Standard.

---

## Key Design Decisions

### 1. Agent Mode: Subagent
- **Rationale**: Agent-Generator is a specialist tool invoked by PM
- **Not Primary**: PM remains the coordination agent
- **Implication**: Uses subagent enforcement patterns (9 mandatory workflow steps)

### 2. Python + Jinja2 Approach
- **Tools**: PyYAML for parsing, Jinja2 for templating
- **Validation**: jsonschema for input validation
- **Output**: StandardValidator for OpenCode Standard compliance

### 3. Enforcement Pattern Injection
- **Automatic**: Enforcement patterns injected during generation (not manual)
- **Mode-Specific**: Different patterns for primary vs subagent
- **Location**: Injected after "## Workflow" section, before "## Memory Integration"

### 4. Two-Template System
- **primary-agent.j2**: For PM-style coordination agents
- **subagent.j2**: For specialist execution agents
- **Selection**: Based on `agent.mode` field in specification

---

## Agent Structure

### 7 Required Sections ✅
1. ✅ **Overview**: Role as agent creator and validator
2. ✅ **Core Responsibilities**: Generation, validation, template management, library management
3. ✅ **Behavioral Guidelines**: What to do (validate, test, inject) / What NOT to do (skip validation, use placeholders)
4. ✅ **Workflow**: Before (validate spec) → During (render, inject, validate) → After (save, report, store)
5. ✅ **Memory Integration**: Search for agent patterns before generation, store successful approaches after
6. ✅ **Quality Standards**: Input validation, output validation, no placeholders, standard compliance
7. ✅ **Success Criteria**: 100% validation pass, all sections present, batch generation works

### Enforcement Patterns ✅
- **MANDATORY WORKFLOW STEPS**: 9 steps (Specification → Memory → Validation → Template → Render → Inject → Validate → Save → Store)
- **BLOCKING PATTERNS**: 8 patterns (skip validation, skip memory, use placeholders, no enforcement, no testing, etc.)
- **EXECUTION VALIDATION**: 9 checklist items
- **ENFORCEMENT RULE**: Blocks incomplete execution

### Optional Sections ✅
- **Agent Generation Tools**: Python libraries, generator components, file operations
- **Input Specification Format**: Complete YAML schema documentation
- **Template Structure**: Jinja2 template examples
- **Enforcement Pattern Injection**: Detailed injection logic
- **Validation Workflow**: Python validation code examples
- **Batch Generation**: Batch processing workflow
- **Collaboration**: With PM, Developer, Architect
- **Common Commands**: Generation and validation commands

---

## Workflow Pattern

```
User Request: "Generate DevOps Engineer agent"
  ↓
PM: Delegates to @Agent-Generator
  ↓
Agent-Generator:
  1. Search memory for similar agent patterns
  2. Validate devops-engineer.yaml against schema
  3. Select subagent.j2 template
  4. Render template with spec data
  5. Inject subagent enforcement patterns
  6. Validate output against OpenCode Standard
  7. Save to .opencode/agent/devops-engineer.md
  8. Generate validation report
  9. Store generation patterns in memory
  ↓
Report to PM: "DevOps Engineer agent generated and validated"
```

---

## Input Specification Format

### Minimal Valid Spec

```yaml
agent:
  name: devops-engineer
  display_name: DevOps Engineer
  mode: subagent
  
  description:
    short: "CI/CD specialist with expertise in pipelines and IaC"
  
  role:
    overview: |
      You are a **DevOps Engineer Agent** responsible for:
      - CI/CD pipeline management
      - Deployment automation
      - Infrastructure as code
    operating_principle: "All deployments automated"
  
  responsibilities:
    - category: "CI/CD"
      duties:
        - "Design pipelines"
        - "Optimize builds"
  
  behavioral_guidelines:
    should_do:
      - category: "Automation"
        actions: ["Automate deployments"]
    should_not_do:
      - category: "Manual Work"
        actions: ["Manual production deploys"]
    workflow_example: "Request → Validate → Deploy"
  
  workflow:
    before_implementation: ["Review requirements"]
    during_implementation: ["Test changes"]
    after_implementation: ["Validate deployment"]
  
  memory_integration:
    search_before: "deployment patterns"
    store_after: "successful strategies"
    categories: ["memory/Pattern/"]
  
  quality_standards:
    standards: ["Automated pipelines"]
    checklist: ["Pipeline tested"]
  
  success_criteria:
    - "Deployments succeed"
```

---

## Validation Rules

### Input Validation
1. **Schema Check**: All required fields present
2. **Mode Validation**: Must be "primary" or "subagent"
3. **Description Length**: 60-120 characters
4. **Name Format**: Lowercase, hyphen-separated, no special chars
5. **Consistency**: Display name matches role references

### Output Validation
1. **Section Presence**: All 7 required sections exist
2. **YAML Frontmatter**: Valid YAML with description + mode
3. **Enforcement Patterns**: MANDATORY STEPS + BLOCKING + VALIDATION present
4. **No Placeholders**: No TODO, FILL IN, [PLACEHOLDER] tokens
5. **Heading Hierarchy**: Proper markdown structure

---

## Enforcement Injection Logic

### For Subagent Mode

```python
def _get_subagent_enforcement():
    return """## Mandatory Workflow Completion

### Complete AgentTask Execution Enforcement
**CRITICAL**: ALL workflow steps MUST be completed...

**MANDATORY WORKFLOW STEPS**:
1. **AgentTask Reading**: Read COMPLETE AgentTask...
2. **Memory Search**: Search memory BEFORE implementation...
[9 steps total]

**BLOCKING PATTERNS** (FORBIDDEN):
- "No memory search needed" → BLOCKED: Always mandatory
[8 patterns total]

**EXECUTION VALIDATION**:
- ☐ AgentTask read completely
[9 checklist items]

**ENFORCEMENT RULE**: Execution BLOCKED if incomplete."""
```

### For Primary Mode

```python
def _get_primary_enforcement():
    return """## Mandatory Workflow Completion

### Complete Coordination Execution Enforcement
**CRITICAL**: ALL coordination steps MUST be completed...

**MANDATORY WORKFLOW STEPS**:
1. **Complexity Analysis**: Calculate before AgentTask...
2. **Memory Search**: Search BEFORE creation...
[7 steps total]

**BLOCKING PATTERNS** (FORBIDDEN):
- "Quick AgentTask without memory search" → BLOCKED
[7 patterns total]

**EXECUTION VALIDATION**:
- ☐ Complexity calculated
[7 checklist items]

**ENFORCEMENT RULE**: Coordination BLOCKED if incomplete."""
```

---

## Quality Checklist Pattern

Every generated agent must have comprehensive quality checklist:

```markdown
### Quality Checklist

Before completing {agent-specific-action}:

- [ ] {Agent-specific requirement 1}
- [ ] {Agent-specific requirement 2}
- [ ] Memory patterns searched and applied
- [ ] All {role} standards followed
- [ ] Documentation complete
- [ ] Novel learnings stored in memory
- [ ] Comprehensive summary written
```

---

## Success Metrics

### Agent-Generator Agent Success
- ✅ **7 Required Sections**: All present and complete
- ✅ **YAML Frontmatter**: Valid with description, mode, name, tools
- ✅ **Enforcement Patterns**: 4 occurrences (MANDATORY, BLOCKING, VALIDATION, RULE)
- ✅ **Behavioral Guidelines**: Clear ✅ SHOULD / ❌ SHOULD NOT sections
- ✅ **Workflow**: Before/During/After structure with 4+ steps each
- ✅ **Memory Integration**: Search before, store after patterns
- ✅ **Quality Standards**: Standards list + comprehensive checklist
- ✅ **Success Criteria**: 7+ measurable outcomes
- ✅ **Optional Sections**: Tools, Input Format, Templates, Validation, Batch, Collaboration, Commands

---

## Next Steps Pattern

### Immediate (Phase 4.2)
1. Create YAML specifications for 10+ specialist agents
2. Use DevOps Engineer spec (from phase4-agent-generator-plan.md) as template
3. Create specs for: Architect, AI Engineer, Database Engineer, System Engineer, Security Engineer, QA Engineer, Backend Tester, Web Designer, Requirements Engineer

### After Specs Created (Phase 4.3)
1. Implement Python generator tool (agent_generator.py)
2. Create Jinja2 templates (primary-agent.j2, subagent.j2)
3. Test generation with single agent
4. Batch generate all 10+ agents
5. Validate all generated agents

### Validation (Phase 4.4)
1. Run StandardValidator on all generated agents
2. Manual review of first generated agent
3. Compare generated agents to hand-crafted pm.md/developer.md
4. Document any deviations or improvements

---

## Key Learnings

### 1. Meta-Agent Design
- **Insight**: Agent that creates agents needs both generation AND validation capabilities
- **Application**: Combined generator + validator responsibilities
- **Pattern**: Single agent handles end-to-end workflow (spec → generate → validate → save)

### 2. Enforcement as Code
- **Insight**: Enforcement patterns can be automatically injected during generation
- **Application**: Template rendering + post-processing injection step
- **Pattern**: Mode-specific enforcement (primary coordination vs subagent execution)

### 3. Validation-First Generation
- **Insight**: Validate input before generation, validate output before save
- **Application**: Input schema validation + output standard validation
- **Pattern**: Fail fast - reject invalid input, don't save invalid output

### 4. Template Flexibility
- **Insight**: Two templates (primary vs subagent) cover all agent types
- **Application**: Mode field determines template selection
- **Pattern**: Optional sections provide customization without template proliferation

---

## Reusable Patterns

### Pattern 1: Agent Definition Structure
```markdown
---
description: {Role} with expertise in {areas}
mode: {primary|subagent}
name: {agent-name}
tools: Edit, MultiEdit, Read, Write, Bash, Grep, Glob, LS
---

## Overview
You are a **{Role} Agent** responsible for:
- {Responsibility 1}
- {Responsibility 2}

**{Operating Principle}**

[6 more required sections...]
```

### Pattern 2: Enforcement Injection
```python
def inject_enforcement(content, mode):
    enforcement = get_enforcement_for_mode(mode)
    # Insert after Workflow, before Memory Integration
    return content.replace("## Memory Integration", 
                          enforcement + "\n\n## Memory Integration")
```

### Pattern 3: Validation Chain
```python
def generate_agent(spec_path):
    spec = load_spec(spec_path)
    validate_input(spec)              # Fail fast on bad input
    content = render_template(spec)   # Generate content
    validate_output(content)          # Fail fast on bad output
    save_agent(content)               # Only save if valid
    return validation_report
```

---

## Storage Location

- **This Pattern**: `memory/Pattern/agent-generator-creation.md`
- **Related Learnings**: `memory/Learning/` (future generation issues)
- **Agent File**: `.opencode/agent/agent-generator.md`
- **Phase Plan**: `docs/phase4-agent-generator-plan.md`

---

## References

- **OpenCode Agent Standard**: `docs/opencode-agent-standard.md`
- **Phase 4 Plan**: `docs/phase4-agent-generator-plan.md`
- **Validated Agents**: `pm.md`, `developer.md`
- **Tracker**: `docs/agent-standardization-tracker.md`
