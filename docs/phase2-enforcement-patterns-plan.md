# Phase 2 Implementation Plan: Enforcement Patterns

**Date**: 2025-11-11  
**Status**: 📋 Planned  
**Phase**: Phase 2 of 4 - Enforcement Patterns  
**Priority**: High

---

## Objectives

Strengthen agent behavioral guidance by adding:
1. **MANDATORY WORKFLOW STEPS** - Non-negotiable execution requirements
2. **BLOCKING PATTERNS** - Explicit forbidden shortcuts
3. **EXECUTION VALIDATION** - Pre-completion checklists

Based on intelligent-claude-code v7.3.6+ enforcement patterns.

---

## Background

### Why Enforcement Patterns?

**Problem**: Behavioral guidelines alone may be insufficient for complex workflows
- Agents might skip steps under time pressure
- "Soft" guidance can be interpreted loosely
- No clear consequences for shortcuts

**Solution**: Explicit enforcement patterns with blocking language
- Clear "MUST" vs "SHOULD" language
- Named blocking patterns agents recognize
- Validation checklists before completion

### Enforcement Philosophy

**OpenCode Approach** (Soft Enforcement):
- No technical hooks to block execution
- Relies on strong behavioral patterns
- Agent "chooses" to follow patterns
- Works through instruction clarity

**Claude Code Approach** (Hard Enforcement):
- Hook system technically blocks execution
- Cannot proceed if workflow incomplete
- System-enforced compliance
- Works through technical constraints

**Our Approach**: Hybrid soft enforcement with explicit blocking language
- Clear MANDATORY requirements
- Named BLOCKING PATTERNS
- Validation checklists
- Strong language ("CRITICAL", "BLOCKED", "FORBIDDEN")

---

## Changes Required

### For Both Agents (pm.md, developer.md)

#### 1. Add "Mandatory Workflow Completion" Section

**Location**: After "Workflow" section, before "Memory Integration"

**Content Structure**:
```markdown
---

## Mandatory Workflow Completion

### Complete {AgentTask/Coordination} Execution Enforcement
**CRITICAL**: ALL workflow steps MUST be completed before marking execution as complete:

**MANDATORY WORKFLOW STEPS**:
1. **{Step Name}**: {Description of required step}
2. **{Step Name}**: {Description of required step}
3. **{Step Name}**: {Description of required step}
[... continue for all critical steps]

**BLOCKING PATTERNS** (FORBIDDEN):
- "{Quote pattern}" → BLOCKED: {Explanation of why this is forbidden}
- "{Quote pattern}" → BLOCKED: {Explanation of why this is forbidden}
- "{Quote pattern}" → BLOCKED: {Explanation of why this is forbidden}
[... continue for all common shortcuts]

**EXECUTION VALIDATION**:
Before claiming {action} completion, validate ALL workflow steps completed:
- ☐ {Validation checkpoint 1}
- ☐ {Validation checkpoint 2}
- ☐ {Validation checkpoint 3}
[... continue for all validation points]

**ENFORCEMENT RULE**: {Action} execution BLOCKED if any workflow step skipped or incomplete.

---
```

#### 2. Strengthen Behavioral Guidelines Language

**Changes**:
- ✅ YOU SHOULD → ✅ YOU MUST
- ❌ YOU SHOULD NOT → ❌ YOU MUST NOT / ❌ FORBIDDEN
- Add consequences language

**Example**:
```markdown
### ✅ YOU MUST

**Memory Search** (MANDATORY):
- Search memory BEFORE any implementation
- Review ALL relevant patterns
- Embed discoveries in context
- BLOCKING: "No similar patterns found" → Must search again

### ❌ FORBIDDEN

**Memory Skipping** (BLOCKED):
- ❌ "Skipping memory for simple change" → BLOCKED: Memory search is ALWAYS mandatory
- ❌ "No patterns needed" → BLOCKED: Search first, decide after
- ❌ "Too simple to search" → BLOCKED: No exceptions to memory-first rule
```

---

## Specific Implementations

### PM Agent Enforcement Patterns

#### MANDATORY WORKFLOW STEPS:
1. **Complexity Analysis**: Calculate complexity points before creating AgentTask
2. **Memory Search**: Search for similar patterns and past solutions
3. **Context Embedding**: Embed complete context (no placeholders)
4. **Specialist Selection**: Choose appropriate agent based on work type
5. **Delegation**: Explicitly delegate to specialist agent
6. **Progress Tracking**: Monitor progress until completion

#### BLOCKING PATTERNS:
- "Quick AgentTask without memory search" → BLOCKED: Memory search is mandatory
- "Create AgentTask with placeholders" → BLOCKED: Complete context required
- "PM executes technical work directly" → BLOCKED: Must delegate to specialist
- "Skip complexity calculation" → BLOCKED: Complexity analysis required
- "Create large AgentTask (>15 pts)" → BLOCKED: Must create story and break down
- "Delegate without complete context" → BLOCKED: Context embedding mandatory

#### EXECUTION VALIDATION:
- ☐ Complexity calculated and documented
- ☐ Memory searched for relevant patterns
- ☐ Complete context embedded (no "TODO", "FILL IN", placeholders)
- ☐ Appropriate specialist selected
- ☐ Explicit delegation performed
- ☐ No technical commands executed by PM

### Developer Agent Enforcement Patterns

#### MANDATORY WORKFLOW STEPS:
1. **AgentTask Reading**: Read complete AgentTask before starting
2. **Memory Search**: Search memory for patterns and solutions
3. **Context Review**: Review embedded standards and examples
4. **Implementation**: Follow AgentTask approach and tasks
5. **Testing**: Write and run tests per validation criteria
6. **Documentation**: Update code comments and technical docs
7. **Learning Storage**: Store novel solutions in memory
8. **Summary Creation**: Write comprehensive completion summary

#### BLOCKING PATTERNS:
- "No memory search needed" → BLOCKED: Memory search is ALWAYS mandatory
- "Tests not needed for simple change" → BLOCKED: Tests required per AgentTask
- "Skip documentation" → BLOCKED: Documentation is mandatory
- "Self-documenting code" → BLOCKED: Explicit documentation required
- "No learnings to store" → BLOCKED: Must evaluate for novel patterns
- "Quick summary" → BLOCKED: Comprehensive summary required
- "Partial AgentTask completion" → BLOCKED: Complete ALL tasks or flag blocker

#### EXECUTION VALIDATION:
- ☐ AgentTask read completely
- ☐ Memory searched (patterns found and reviewed)
- ☐ Embedded context applied
- ☐ All implementation tasks completed
- ☐ Tests written and passing
- ☐ Code documented per standards
- ☐ Novel learnings stored in memory
- ☐ Comprehensive summary written

---

## Implementation Steps

### Step 1: Update PM Agent
1. Open `.opencode/agent/pm.md`
2. Add "Mandatory Workflow Completion" section after "Workflow"
3. Strengthen language in "Behavioral Guidelines"
4. Add enforcement rule at bottom
5. Validate formatting

### Step 2: Update Developer Agent
1. Open `.opencode/agent/developer.md`
2. Add "Mandatory Workflow Completion" section after "Workflow"
3. Strengthen language in "Behavioral Guidelines"
4. Add enforcement rule at bottom
5. Validate formatting

### Step 3: Validate Both Agents
1. Check all MANDATORY steps listed
2. Verify BLOCKING PATTERNS cover common shortcuts
3. Ensure EXECUTION VALIDATION is complete
4. Confirm language is strong ("MUST", "CRITICAL", "BLOCKED")

### Step 4: Test in Practice
1. Give PM agent a test task
2. Observe if enforcement patterns guide behavior
3. Check if blocking patterns prevent shortcuts
4. Adjust language if needed

---

## Success Criteria

### Quantitative
- [ ] 2 agents updated with enforcement sections
- [ ] 6+ MANDATORY WORKFLOW STEPS per agent
- [ ] 5+ BLOCKING PATTERNS per agent
- [ ] 5+ EXECUTION VALIDATION items per agent

### Qualitative
- [ ] Clear, unambiguous language ("MUST", not "should")
- [ ] Blocking patterns address common shortcuts
- [ ] Validation checklists are actionable
- [ ] Enforcement rules explicitly stated

---

## Risks & Mitigations

### Risk 1: Too Rigid
**Risk**: Enforcement patterns too strict, prevents agent autonomy
**Mitigation**: Focus on critical steps only, allow flexibility in implementation details

### Risk 2: Pattern Explosion
**Risk**: Too many blocking patterns, becomes overwhelming
**Mitigation**: Limit to 5-7 most common shortcuts per agent

### Risk 3: Agent Confusion
**Risk**: Strong language confuses agent about priorities
**Mitigation**: Clear hierarchy: CRITICAL > MANDATORY > BLOCKING > FORBIDDEN

---

## Language Hierarchy

### Instruction Strength (Strongest to Weakest)

1. **CRITICAL** - Absolutely required, no exceptions
2. **MANDATORY** - Required for all executions
3. **BLOCKED** - Explicitly forbidden, named pattern
4. **FORBIDDEN** - Prohibited action
5. **MUST** - Strong requirement
6. **SHOULD** - Strong recommendation
7. **RECOMMENDED** - Suggested approach

### Usage Guidelines

**CRITICAL**: Reserved for safety/correctness issues
- Example: "CRITICAL: Memory search before implementation"

**MANDATORY**: Required workflow steps
- Example: "MANDATORY WORKFLOW STEPS: 1. Read AgentTask..."

**BLOCKED**: Named forbidden patterns
- Example: "BLOCKED: 'Skip tests for simple change'"

**FORBIDDEN**: General prohibitions
- Example: "FORBIDDEN: PM executing technical commands"

---

## Examples from intelligent-claude-code

### Their Blocking Patterns (v7.3.6+)

```markdown
**BLOCKING PATTERNS** (FORBIDDEN):
- "No git operations needed" → BLOCKED: Git workflow is mandatory
- "Skip CHANGELOG" → BLOCKED: Documentation updates required
- "No version change needed" → BLOCKED: Version management mandatory
- "Simple change, no review" → BLOCKED: Review process mandatory
- "Self-documenting code" → BLOCKED: Documentation requirements apply
- "Direct commit to main" → BLOCKED: Branch protection must be followed
```

### Our Adaptation for OpenCode

We'll adapt these to our context:
- Replace git-specific patterns with memory/AgentTask patterns
- Keep same strong language ("BLOCKED", "FORBIDDEN")
- Maintain same validation checklist approach
- Adjust to OpenCode workflow (no hard hooks)

---

## Next Actions

1. **Review this plan** - Ensure approach makes sense
2. **Implement for PM agent** - Add enforcement section
3. **Implement for Developer agent** - Add enforcement section
4. **Test enforcement** - Try a sample task
5. **Document results** - Create Phase 2 completion summary

---

## Timeline

- **Planning**: 30 minutes (this document)
- **PM Agent Update**: 45 minutes
- **Developer Agent Update**: 45 minutes
- **Validation & Testing**: 30 minutes
- **Documentation**: 30 minutes

**Total Estimated Time**: 2.5-3 hours

---

## References

- **intelligent-claude-code v7.3.6+**: Mandatory workflow enforcement patterns
- **OpenCode Agent Standard**: `docs/opencode-agent-standard.md`
- **Phase 1 Summary**: `docs/phase1-implementation-summary.md`

---

**Prepared By**: PM Agent  
**Status**: Ready for Implementation  
**Next Phase**: Phase 3 - Structure Validation
