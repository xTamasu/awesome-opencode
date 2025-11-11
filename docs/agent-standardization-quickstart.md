# Agent Standardization Quick Start Guide

**For**: New contributors, reviewers, or anyone resuming this work  
**Last Updated**: 2025-11-11  
**Project Status**: Phase 1 Complete (25%)

---

## What Is This Project?

We're standardizing OpenCode agents to align with [intelligent-claude-code](https://github.com/intelligentcode-ai/intelligent-claude-code) best practices while maintaining full OpenCode compatibility.

**Goal**: Create a consistent, well-documented, generator-ready agent system.

---

## Where We Are Now

### ✅ Phase 1: Format Standardization (COMPLETE)

**What We Did**:
- Updated 2 agents (`pm.md`, `developer.md`) with hybrid YAML format
- Added Claude Code compatibility fields (`name`, `tools`)
- Maintained OpenCode required fields (`description`, `mode`)
- 100% backward compatible, zero breaking changes

**Result**: Agents now work in OpenCode AND follow Claude Code conventions.

### 📋 Phase 2: Enforcement Patterns (NEXT)

**What We'll Do**:
- Add MANDATORY WORKFLOW STEPS sections
- Add BLOCKING PATTERNS for common shortcuts
- Add EXECUTION VALIDATION checklists
- Strengthen language (SHOULD → MUST)

**Why**: Provides stronger guidance to prevent agents from skipping critical steps.

---

## Essential Documents (Read These First)

### 1. **Overview & Context** (15 min read)
📄 `docs/agent-system-review.md`
- How intelligent-claude-code works
- What we learned from their system
- Gap analysis with our implementation
- Recommendations

### 2. **The Standard** (30 min read)
📄 `docs/opencode-agent-standard.md`
- **THE DEFINITIVE SPEC** for OpenCode agents
- Required sections (7)
- Optional sections
- Enforcement patterns
- Agent generation specification

### 3. **Compatibility Analysis** (20 min read)
📄 `docs/agent-format-compatibility.md`
- OpenCode vs Claude Code format comparison
- Hybrid format recommendation
- Compatibility matrix
- Decision rationale

### 4. **What We've Done** (10 min read)
📄 `docs/phase1-implementation-summary.md`
- Phase 1 implementation details
- Changes made to agents
- Benefits achieved
- Next steps

### 5. **Where We're Going** (15 min read)
📄 `docs/phase2-enforcement-patterns-plan.md`
- Phase 2 detailed plan
- Enforcement pattern specifications
- Implementation steps
- Success criteria

### 6. **Progress Tracker** (5 min read)
📄 `docs/agent-standardization-tracker.md`
- Current status dashboard
- Phase checklist
- Risks and mitigations
- Timeline

---

## File Structure

```
awesome-opencode/
├── .opencode/
│   └── agent/
│       ├── pm.md              # ✅ Updated (Phase 1)
│       └── developer.md       # ✅ Updated (Phase 1)
├── docs/
│   ├── agent-system-review.md                    # ✅ Analysis
│   ├── opencode-agent-standard.md                # ✅ Specification
│   ├── agent-format-compatibility.md             # ✅ Compatibility
│   ├── phase1-implementation-summary.md          # ✅ Phase 1 complete
│   ├── phase2-enforcement-patterns-plan.md       # ✅ Phase 2 plan
│   ├── agent-standardization-tracker.md          # ✅ Progress tracker
│   └── agent-standardization-quickstart.md       # ✅ This file
├── AGENTS.md                  # Behavioral patterns & code standards
└── README.md                  # Project overview
```

---

## Quick Reference: Agent Format

### Current Hybrid Format (After Phase 1)

```yaml
---
# OpenCode required fields
description: {Role description with expertise areas (60-150 chars)}
mode: {primary|subagent}

# Optional Claude Code compatibility
name: {agent-identifier}
tools: Edit, MultiEdit, Read, Write, Bash, Grep, Glob, LS
---

## Overview
...

## Core Responsibilities
...

## Behavioral Guidelines
...

## Workflow
...

## Memory Integration
...

## Quality Standards
...

## Success Criteria
...
```

### 7 Required Sections (Every Agent Must Have)

1. **Overview** - Brief role introduction
2. **Core Responsibilities** - Detailed duties
3. **Behavioral Guidelines** - Dos and don'ts
4. **Workflow** - Before/During/After steps
5. **Memory Integration** - Memory search/storage patterns
6. **Quality Standards** - Quality criteria and checklists
7. **Success Criteria** - What success looks like

---

## How to Continue This Work

### If Implementing Phase 2 (Enforcement Patterns)

1. **Read the plan**: `docs/phase2-enforcement-patterns-plan.md`
2. **Update pm.md**:
   - Add "Mandatory Workflow Completion" section
   - Add MANDATORY WORKFLOW STEPS (6+ items)
   - Add BLOCKING PATTERNS (5+ items)
   - Add EXECUTION VALIDATION checklist
   - Strengthen language in Behavioral Guidelines
3. **Update developer.md**:
   - Same structure as pm.md
   - Developer-specific steps and patterns
4. **Test**: Try giving agents tasks, observe if patterns guide behavior
5. **Document**: Create `docs/phase2-enforcement-patterns-summary.md`

### If Implementing Phase 3 (Structure Validation)

1. **Create checklist**: Based on 7 required sections
2. **Audit pm.md**: Verify all sections present and complete
3. **Audit developer.md**: Verify all sections present and complete
4. **Fix gaps**: Add any missing sections
5. **Standardize formatting**: Ensure consistency
6. **Document**: Create `docs/phase3-structure-validation-summary.md`

### If Implementing Phase 4 (Agent Generator)

1. **Read spec**: `docs/opencode-agent-standard.md` → "Agent Generation Specification"
2. **Design input schema**: YAML or JSON for agent definitions
3. **Implement generator**: Python or Node.js
4. **Add validation**: Check against standard spec
5. **Test**: Generate test agents, validate output
6. **Generate remaining agents**: 12 agents from intelligent-claude-code
7. **Document**: Create `docs/phase4-agent-generator-summary.md`

---

## Common Questions

### Q: Why hybrid format?
**A**: Maintains OpenCode compatibility while adding Claude Code fields for future-proofing and explicit documentation.

### Q: Will this break existing functionality?
**A**: No. Changes are purely additive. OpenCode ignores the new fields, but they're there if needed later.

### Q: Why enforcement patterns?
**A**: Soft enforcement through strong behavioral patterns guides agents to follow complete workflows without shortcuts.

### Q: Do we need all 14 agents from intelligent-claude-code?
**A**: Not immediately. We start with PM and Developer. Phase 4 will generate the remaining 12 agents.

### Q: Can I modify the standard?
**A**: Yes, but update `docs/opencode-agent-standard.md` and notify the team. The standard evolves with our needs.

### Q: What if OpenCode changes format requirements?
**A**: Hybrid approach is resilient. We can adjust new fields without breaking core functionality.

---

## Key Principles

### 1. **Compatibility First**
Never break OpenCode compatibility. All changes must work with current OpenCode system.

### 2. **Additive Changes**
Add new fields/sections, don't remove or replace existing ones.

### 3. **Document Everything**
Every change gets documented. Every phase gets a summary.

### 4. **Test Thoroughly**
Verify agents still work after changes. Test with real tasks.

### 5. **Follow the Standard**
`docs/opencode-agent-standard.md` is the source of truth.

---

## Tools & Resources

### Validation
- YAML validators: https://www.yamllint.com/
- Markdown linters: https://github.com/DavidAnson/markdownlint

### Reference
- intelligent-claude-code: https://github.com/intelligentcode-ai/intelligent-claude-code
- OpenCode docs: (reference project documentation)

### Templates
- Minimal agent template: In `docs/opencode-agent-standard.md`
- Medium AgentTask template: `agenttask-templates/medium-agenttask-template.yaml`

---

## Success Metrics

### Phase 1 ✅
- [x] 2 agents updated
- [x] 0 breaking changes
- [x] 100% backward compatibility

### Phase 2 📋
- [ ] 14+ enforcement patterns added
- [ ] Strong language implemented
- [ ] Validation checklists created

### Phase 3 📋
- [ ] 7 required sections validated
- [ ] Consistent formatting across agents
- [ ] Complete structure compliance

### Phase 4 📋
- [ ] Generator tool built
- [ ] 12+ new agents generated
- [ ] Automated validation working

---

## Get Help

### Documentation Issues
- Read the full spec: `docs/opencode-agent-standard.md`
- Check compatibility: `docs/agent-format-compatibility.md`
- Review analysis: `docs/agent-system-review.md`

### Implementation Questions
- Check the tracker: `docs/agent-standardization-tracker.md`
- Review phase plans in `docs/`
- Look at completed phases for patterns

### Blocked?
- Document the blocker
- Check if it's a known risk in tracker
- Consider creating a story for resolution

---

## Quick Commands

### View Current Agents
```bash
cat .opencode/agent/pm.md
cat .opencode/agent/developer.md
```

### Validate YAML Frontmatter
```bash
# Extract and validate YAML from agent file
sed -n '/^---$/,/^---$/p' .opencode/agent/pm.md | yamllint -
```

### Check Section Presence
```bash
# Check if all required sections present
grep "^## " .opencode/agent/pm.md
```

### View Documentation
```bash
ls -lh docs/
cat docs/agent-standardization-tracker.md
```

---

## Timeline Summary

| Phase | Status | Duration | Start | End |
|-------|--------|----------|-------|-----|
| Phase 1 | ✅ Complete | 1 hr | 2025-11-11 | 2025-11-11 |
| Phase 2 | 📋 Planned | 2-3 hrs | TBD | TBD |
| Phase 3 | 📋 Planned | 1-2 hrs | TBD | TBD |
| Phase 4 | 📋 Planned | 1-2 days | TBD | TBD |

**Total Estimated**: 2-3 days of work  
**Completion**: 25% (1 of 4 phases)

---

## Next Immediate Steps

1. **Read Phase 2 plan**: `docs/phase2-enforcement-patterns-plan.md`
2. **Implement enforcement patterns** for pm.md
3. **Implement enforcement patterns** for developer.md
4. **Test the patterns** with sample tasks
5. **Document Phase 2 completion**

---

**Prepared By**: PM Agent  
**For**: Future contributors  
**Last Updated**: 2025-11-11  
**Status**: Living document (update as needed)
