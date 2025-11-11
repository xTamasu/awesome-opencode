# Agent Format Compatibility Analysis

**Date**: 2025-11-11  
**Purpose**: Cross-check intelligent-claude-code agents with OpenCode requirements and recommend standardization approach

---

## Format Comparison

### Current OpenCode Format

```yaml
---
description: Project management and coordination specialist with expertise in story breakdown, work delegation, and team coordination
mode: primary
---
```

**Fields**:
- `description`: Role description with expertise areas
- `mode`: Operation mode (`primary` or `subagent`)

### intelligent-claude-code Format (Claude Code Native)

```yaml
---
name: pm
description: Project management and coordination specialist with expertise in story breakdown, work delegation, and team coordination
tools: Edit, MultiEdit, Read, Write, Bash, Grep, Glob, LS
---
```

**Fields**:
- `name`: Agent identifier (lowercase, hyphenated)
- `description`: Role description
- `tools`: Available tools for the agent

### Comparison Matrix

| Field | OpenCode | Claude Code | Required By | Purpose |
|-------|----------|-------------|-------------|---------|
| `name` | ❌ | ✅ | Claude Code | Agent identifier for invocation |
| `description` | ✅ | ✅ | Both | Role and expertise description |
| `mode` | ✅ | ❌ | OpenCode | Distinguishes primary vs subagent |
| `tools` | ❌ | ✅ | Claude Code | Tool access restrictions |

---

## Compatibility Assessment

### What Works ✅

1. **Description Field**: Both use same field, compatible format
2. **Markdown Content**: Both use markdown for behavioral patterns
3. **Section Structure**: Compatible approach (Overview, Responsibilities, Workflow)
4. **Memory Integration**: Both support memory-first patterns
5. **AgentTask System**: Compatible AgentTask execution model

### What Differs ⚠️

1. **Agent Identification**:
   - Claude Code uses `name` field for explicit identification
   - OpenCode infers from filename

2. **Operation Mode**:
   - OpenCode uses `mode` to distinguish primary/subagent
   - Claude Code doesn't have this concept (all are subagents invoked by Task tool)

3. **Tool Access**:
   - Claude Code explicitly lists tools per agent
   - OpenCode gives full tool access, relies on behavioral guidance

### What's Incompatible ❌

1. **Tool Restrictions**:
   - Claude Code: Hard enforcement via `tools` field
   - OpenCode: No tool restrictions, behavioral guidance only

2. **Enforcement Mechanisms**:
   - Claude Code: Hook system with hard blocks
   - OpenCode: Behavioral patterns with soft guidance

---

## Proposed Hybrid Format

### Option 1: Minimal Compatibility (Recommended)

Add Claude Code fields as optional, keep OpenCode fields:

```yaml
---
# OpenCode required fields
description: Project management and coordination specialist with expertise in story breakdown, work delegation, and team coordination
mode: primary

# Optional Claude Code compatibility
name: pm
tools: Edit, MultiEdit, Read, Write, Bash, Grep, Glob, LS
---
```

**Pros**:
- Maximum compatibility
- Works in both systems
- Explicit tool documentation (even if not enforced)
- Clear agent identification

**Cons**:
- More verbose
- Redundant information (name in filename and frontmatter)

### Option 2: OpenCode-Only (Current)

Keep current format, no changes:

```yaml
---
description: Project management and coordination specialist with expertise in story breakdown, work delegation, and team coordination
mode: primary
---
```

**Pros**:
- Simpler, cleaner
- No redundancy
- Works for OpenCode

**Cons**:
- Not compatible with Claude Code native format
- Missing explicit agent identification
- No tool documentation

### Option 3: Claude Code Native

Adopt Claude Code format, drop OpenCode-specific fields:

```yaml
---
name: pm
description: Project management and coordination specialist with expertise in story breakdown, work delegation, and team coordination
tools: Edit, MultiEdit, Read, Write, Bash, Grep, Glob, LS
---
```

**Pros**:
- Claude Code compatible
- Explicit tool listing
- Standard format

**Cons**:
- Loses `mode` distinction
- Requires OpenCode to support this format
- May not work with current OpenCode implementation

---

## Behavioral Pattern Compatibility

### Compatible Patterns ✅

These patterns work in both systems:

1. **Memory-First Workflow**
   ```markdown
   **MANDATORY before ANY implementation**:
   1. Search memory for relevant patterns
   2. Review similar past solutions
   3. Implement with discovered context
   4. Store new learnings after completion
   ```

2. **AgentTask-Driven Development**
   ```markdown
   **MANDATORY**: All work follows AgentTask execution patterns:
   - Execute complete AgentTasks with embedded context
   - No work outside AgentTask framework
   - Follow all success criteria and execution checklists
   ```

3. **Quality Standards**
   ```markdown
   ### Quality Checklist
   Before completing AgentTask:
   - [ ] Code follows standards
   - [ ] All tests passing
   - [ ] Documentation updated
   - [ ] Memory updated
   ```

### System-Specific Patterns

#### OpenCode-Specific

**Main Scope Pattern** (primary/subagent distinction):
```markdown
## Main Scope Mode

**PM operates in coordination-only mode:**
- PM creates AgentTasks
- PM delegates to specialists
- Technical work is blocked
```

**Why OpenCode-Specific**: Uses `mode` field concept, PM is primary agent

#### Claude Code-Specific

**Tool Restriction Pattern**:
```yaml
tools: Read, Write, Edit  # Limited toolset
```

**Why Claude Code-Specific**: Hard enforcement via tool restrictions, not possible in OpenCode

**Import System**:
```markdown
## Imports
@../behaviors/shared-patterns/git-privacy-patterns.md
```

**Why Claude Code-Specific**: Claude Code has import mechanism, OpenCode doesn't

### Adaptable Patterns

These can work in both with minor adjustments:

1. **Documentation Enforcement**
   - Claude Code: Enforced via hooks
   - OpenCode: Enforced via behavioral blocking patterns
   - **Adaptation**: Keep blocking patterns, rely on agent following instructions

2. **Git Privacy**
   - Claude Code: Auto-strips AI mentions via hook
   - OpenCode: Guidance to remove AI mentions
   - **Adaptation**: Document as "soft enforcement"

3. **Dynamic Specialization**
   - Both support via AgentTask context injection
   - **Adaptation**: No changes needed

---

## Enforcement Approach Comparison

### Claude Code: Hard Enforcement

**Mechanism**: JavaScript hooks intercept operations

```javascript
// Example: PM constraint enforcement
if (isPMRole && isTechnicalCommand) {
  blockOperation("PM must create AgentTasks, not run technical commands");
}
```

**Characteristics**:
- ✅ Guaranteed compliance
- ✅ Immediate feedback
- ✅ Prevents errors before they happen
- ❌ Requires hook system
- ❌ Less flexible
- ❌ Hidden enforcement logic

### OpenCode: Soft Enforcement

**Mechanism**: Behavioral instructions in agent definitions

```markdown
## Behavioral Guidelines

❌ **PM SHOULD NOT:**
- Run technical commands directly
- Edit code files directly
- Execute database operations

**BLOCKING PATTERNS** (FORBIDDEN):
- "No git operations needed" → BLOCKED: Git workflow is mandatory
```

**Characteristics**:
- ✅ Transparent (all rules visible)
- ✅ Flexible (agent can adapt)
- ✅ No special infrastructure
- ❌ Relies on agent compliance
- ❌ Can be ignored
- ❌ No automatic prevention

### Recommendation

**Adopt hybrid approach**:
1. Use **soft enforcement** (behavioral patterns) as primary
2. Add **strong language** to make violations clear
3. Consider **validation tools** (linters, pre-commit hooks) as supplementary
4. Document **compliance expectations** clearly

---

## Structural Compatibility

### Section Mapping

| Section | OpenCode | Claude Code | Compatible? | Notes |
|---------|----------|-------------|-------------|-------|
| Overview | ✅ Yes | ✅ Yes | ✅ | Same purpose and format |
| Core Responsibilities | ✅ Yes | ✅ Yes | ✅ | Same purpose and format |
| Behavioral Patterns | ✅ Yes | ✅ Yes | ✅ | Same concept, different enforcement |
| Workflow | ✅ Yes | ✅ Yes | ✅ | Same structure (Before/During/After) |
| Memory Integration | ✅ Yes | ✅ Yes | ✅ | Same concept and patterns |
| Quality Standards | ✅ Yes | ✅ Yes | ✅ | Same purpose and format |
| Specialization Capability | ✅ Yes | ✅ Yes | ✅ | Both support dynamic specialization |
| Collaboration Patterns | ✅ Yes | ✅ Yes | ✅ | Same concept |
| Tools and Commands | ✅ Yes | ✅ Yes | ⚠️ | OpenCode lists, Claude Code restricts |
| File Operations | ✅ Yes | ✅ Yes | ✅ | Same guidance approach |
| Success Criteria | ✅ Yes | ✅ Yes | ✅ | Same concept |
| Imports | ❌ No | ✅ Yes | ❌ | Claude Code-specific feature |

**Compatibility Score**: 10/12 sections compatible (83%)

---

## Recommendations

### Immediate Actions (High Priority)

1. **Adopt Hybrid YAML Format**
   ```yaml
   ---
   description: {description}
   mode: {primary|subagent}
   name: {agent-name}
   tools: Edit, MultiEdit, Read, Write, Bash, Grep, Glob, LS
   ---
   ```
   - Maintains OpenCode functionality
   - Adds Claude Code compatibility
   - Documents tool usage (even if not enforced)

2. **Add Documentation Enforcement Patterns**
   - Add MANDATORY WORKFLOW STEPS section to all agents
   - Add BLOCKING PATTERNS section to all agents
   - Add EXECUTION VALIDATION checklist to all agents
   - This improves quality even without hard enforcement

3. **Standardize Section Structure**
   - Ensure all agents have required sections
   - Use consistent formatting
   - Follow the OpenCode Agent Standard specification

### Short-Term Actions (Medium Priority)

4. **Create Agent Generator**
   - Build tool to generate agents from specification
   - Validate against OpenCode Agent Standard
   - Support both OpenCode and hybrid formats

5. **Add Soft Enforcement Language**
   - Make behavioral guidelines more explicit
   - Use strong language for prohibitions
   - Add "BLOCKED" markers for forbidden patterns

6. **Document Tool Usage**
   - Even without enforcement, document which tools agents use
   - Helps with understanding and debugging
   - Prepares for potential future enforcement

### Long-Term Actions (Low Priority)

7. **Consider Import System**
   - Evaluate need for shared behavioral patterns
   - Could implement as include/template system
   - Not critical for initial standardization

8. **Evaluate Validation Tooling**
   - Pre-commit hooks for agent format validation
   - Linter for AgentTask compliance
   - Could supplement soft enforcement

9. **Cross-Platform Testing**
   - If Claude Code compatibility desired, test agents in both systems
   - Identify any edge cases or incompatibilities

---

## Implementation Plan

### Phase 1: Format Standardization (Week 1)

**Goal**: Standardize YAML frontmatter across all agents

**Tasks**:
1. Update `pm.md` with hybrid format:
   ```yaml
   ---
   description: Project management and coordination specialist with expertise in story breakdown, work delegation, and team coordination
   mode: primary
   name: pm
   tools: Edit, MultiEdit, Read, Write, Bash, Grep, Glob, LS
   ---
   ```

2. Update `developer.md` with hybrid format:
   ```yaml
   ---
   description: Software implementation specialist with expertise in feature development, code architecture, and technical implementation
   mode: subagent
   name: developer
   tools: Edit, MultiEdit, Read, Write, Bash, Grep, Glob, LS
   ---
   ```

3. Test OpenCode compatibility with new format

**Success Criteria**:
- [ ] All agents have hybrid YAML format
- [ ] OpenCode still loads agents correctly
- [ ] No breaking changes

### Phase 2: Enforcement Patterns (Week 2)

**Goal**: Add documentation enforcement patterns to all agents

**Tasks**:
1. Add to all agents:
   - MANDATORY WORKFLOW STEPS section
   - BLOCKING PATTERNS section
   - EXECUTION VALIDATION checklist

2. Review and update behavioral guidelines:
   - Strengthen language for prohibitions
   - Add clear examples of violations
   - Document expected behavior explicitly

**Success Criteria**:
- [ ] All agents have enforcement sections
- [ ] Language is clear and strong
- [ ] Patterns are consistent across agents

### Phase 3: Structure Validation (Week 3)

**Goal**: Ensure all agents follow standard structure

**Tasks**:
1. Validate all agents have required sections
2. Ensure consistent formatting
3. Add missing sections where needed
4. Document any agent-specific variations

**Success Criteria**:
- [ ] All agents have required sections
- [ ] Formatting is consistent
- [ ] Agents follow OpenCode Agent Standard

### Phase 4: Documentation & Generator (Week 4)

**Goal**: Document standard and create generator

**Tasks**:
1. Finalize OpenCode Agent Standard specification ✅ (Done)
2. Create agent generator tool
3. Add validation capabilities to generator
4. Document usage and examples

**Success Criteria**:
- [ ] Standard specification complete and documented
- [ ] Generator can create valid agents
- [ ] Validation catches format errors
- [ ] Documentation explains usage

---

## Decision Matrix

### Should We Adopt Hybrid Format?

| Criteria | Score | Weight | Notes |
|----------|-------|--------|-------|
| **OpenCode Compatibility** | 10/10 | High | Must work with OpenCode |
| **Claude Code Compatibility** | 8/10 | Medium | Nice to have, not critical |
| **Simplicity** | 6/10 | Medium | More fields = more complexity |
| **Documentation Value** | 9/10 | Medium | Explicit tool listing is helpful |
| **Future-Proofing** | 9/10 | High | Prepares for potential changes |
| **Maintainability** | 7/10 | High | More fields = more maintenance |

**Weighted Score**: 8.1/10

**Recommendation**: ✅ **Adopt hybrid format**

**Rationale**:
- High compatibility with OpenCode (required)
- Good documentation value (helpful even without enforcement)
- Strong future-proofing (prepares for potential format evolution)
- Minimal complexity increase (just 2 additional fields)

### Should We Add Hard Enforcement?

| Criteria | Score | Weight | Notes |
|----------|-------|--------|-------|
| **Quality Improvement** | 10/10 | High | Would guarantee compliance |
| **Implementation Effort** | 2/10 | High | Requires hook system or tooling |
| **Flexibility** | 3/10 | Medium | Reduces agent adaptability |
| **Transparency** | 5/10 | Medium | May hide enforcement logic |
| **OpenCode Support** | 0/10 | Critical | Not supported by OpenCode |

**Weighted Score**: 4.0/10

**Recommendation**: ❌ **Do not add hard enforcement** (at this time)

**Rationale**:
- OpenCode doesn't support hook system
- Would require significant custom tooling
- Soft enforcement with strong language is sufficient
- Can revisit if OpenCode adds hook support

---

## Conclusion

### Key Findings

1. **Format Compatibility**: 83% structural compatibility between systems
2. **Main Difference**: Enforcement mechanism (hard vs soft)
3. **Best Path Forward**: Hybrid format with soft enforcement
4. **Quality Approach**: Strong behavioral patterns + validation tooling

### Recommended Standard

**YAML Format**:
```yaml
---
description: {Role} with expertise in {areas}
mode: {primary|subagent}
name: {agent-name}
tools: Edit, MultiEdit, Read, Write, Bash, Grep, Glob, LS
---
```

**Content Structure**:
- 7 required sections (Overview, Responsibilities, Behavioral Guidelines, Workflow, Memory Integration, Quality Standards, Success Criteria)
- Optional role-specific sections
- Enforcement patterns (MANDATORY WORKFLOW STEPS, BLOCKING PATTERNS, EXECUTION VALIDATION)
- Strong behavioral language

**Enforcement Approach**:
- Soft enforcement via behavioral patterns
- Strong language for prohibitions
- Clear blocking pattern documentation
- Supplementary validation tooling (future)

### Next Steps

1. ✅ Review completed - this document
2. ⏭️ Update agents with hybrid format (Phase 1)
3. ⏭️ Add enforcement patterns (Phase 2)
4. ⏭️ Validate structure (Phase 3)
5. ⏭️ Create generator (Phase 4)

---

**Document Status**: Complete  
**Recommendation**: Adopt hybrid format with phased implementation  
**Priority**: High - foundational for agent system standardization
