# OpenCode Agent Generator

Automated agent generation tool that creates standardized agent definitions from YAML specifications.

## Overview

The Agent Generator creates complete, validated agent markdown files following the **OpenCode Agent Standard**. It ensures:
- All 7 required sections present
- Proper enforcement patterns injected
- YAML frontmatter valid
- No placeholders in output
- 100% standard compliance

## Installation

```bash
# Install Python dependencies
pip install -r requirements.txt
```

## Usage

### Generate Single Agent

```bash
# Generate from specification
python agent_generator.py specs/devops-engineer.yaml

# Skip output validation (not recommended)
python agent_generator.py specs/devops-engineer.yaml --no-validation
```

### Batch Generation

```bash
# Generate all agents in specs/ directory
python agent_generator.py specs/ --batch
```

### Validate Existing Agent

```bash
# Validate agent against OpenCode Standard
python agent_generator.py --validate ../.opencode/agent/developer.md
```

### Custom Paths

```bash
# Specify custom template and output directories
python agent_generator.py specs/custom.yaml \
  --templates /path/to/templates \
  --output /path/to/output
```

## Specification Format

### Minimal Specification

```yaml
agent:
  name: "agent-name"                 # Lowercase, hyphen-separated
  display_name: "Agent Name"         # Title case
  mode: subagent                     # primary or subagent
  
  description:
    short: "Role with expertise in areas (60-120 chars)"
  
  role:
    overview: |
      Multi-line description of agent role and purpose
    operating_principle: "Key constraint or principle"
    key_reminder: "Final reminder message"
  
  responsibilities:
    - category: "Responsibility Category"
      duties:
        - "Specific duty 1"
        - "Specific duty 2"
  
  behavioral_guidelines:
    should_do:
      - category: "Category Name"
        actions:
          - "Allowed action 1"
          - "Allowed action 2"
    should_not_do:
      - category: "Category Name"
        actions:
          - "Prohibited action 1"
          - "Prohibited action 2"
    workflow_example: |
      Pattern example showing workflow
  
  workflow:
    before_implementation:
      - "Step 1: Description"
      - "Step 2: Description"
    during_implementation:
      - "Step 1: Description"
      - "Step 2: Description"
    after_implementation:
      - "Step 1: Description"
      - "Step 2: Description"
  
  memory_integration:
    search_before: "What to search for before work"
    store_after: "What to store after completion"
    categories:
      - "Pattern"
      - "Learning"
      - "Knowledge"
    category_descriptions:
      Pattern: "Reusable code patterns"
      Learning: "Problem solutions"
      Knowledge: "Architecture decisions"
  
  quality_standards:
    standards:
      - "Standard 1"
      - "Standard 2"
    checklist:
      - "Checklist item 1"
      - "Checklist item 2"
  
  success_criteria:
    - "Success outcome 1"
    - "Success outcome 2"
```

### Optional Sections

```yaml
agent:
  # ... required fields ...
  
  optional_sections:
    tools_and_commands:
      tools:
        - name: "Tool Name"
          description: "Tool purpose"
      commands:
        - description: "Command purpose"
          command: "command syntax"
    
    collaboration_patterns:
      - agent: "Agent Role"
        patterns:
          - "Collaboration pattern 1"
          - "Collaboration pattern 2"
```

## Directory Structure

```
.opencode/generator/
├── agent_generator.py       # Main generator script
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── templates/              # Jinja2 templates
│   ├── subagent.j2        # Specialist agent template
│   └── primary-agent.j2   # PM-style agent template
├── schemas/               # Validation schemas
│   └── agent_spec_schema.yaml
└── specs/                 # Agent specifications
    ├── devops-engineer.yaml
    ├── architect.yaml
    └── ...
```

## Validation

The generator performs comprehensive validation:

### Input Validation
- All required fields present
- Field types correct
- Constraints satisfied (name format, description length, etc.)
- Mode is valid (primary or subagent)

### Output Validation
- All 7 required sections present
- YAML frontmatter valid
- Enforcement patterns injected (for subagents)
- No placeholders remain
- File saved successfully

## Enforcement Pattern Injection

### Subagent Mode
Automatically injects:
- 9 MANDATORY WORKFLOW STEPS
- 8 BLOCKING PATTERNS
- 8 EXECUTION VALIDATION checklist items
- ENFORCEMENT RULE

### Primary Mode
Automatically injects:
- 7 MANDATORY WORKFLOW STEPS (coordination-focused)
- 7 BLOCKING PATTERNS (delegation-focused)
- 7 EXECUTION VALIDATION checklist items
- ENFORCEMENT RULE

Injection point: After "## Workflow", before "## Memory Integration"

## Examples

### Generate DevOps Engineer Agent

```bash
# Create specification
cat > specs/devops-engineer.yaml <<EOF
agent:
  name: devops-engineer
  display_name: DevOps Engineer
  mode: subagent
  description:
    short: "CI/CD and deployment automation specialist with expertise in pipelines, infrastructure as code, and release management"
  # ... rest of spec
EOF

# Generate agent
python agent_generator.py specs/devops-engineer.yaml

# Output: ../.opencode/agent/devops-engineer.md
```

### Batch Generate All Agents

```bash
# Place all specs in specs/ directory
ls specs/
# architect.yaml
# devops-engineer.yaml
# security-engineer.yaml
# ...

# Generate all
python agent_generator.py specs/ --batch

# Output:
# ===========================================================
# Generating: architect.yaml
# ===========================================================
# ✓ Loaded specification: specs/architect.yaml
# ✓ Specification validated
# ✓ Agent rendered from template
# ✓ Output validated against OpenCode Standard
# ✓ Agent saved: ../.opencode/agent/architect.md
# ...
```

## Error Handling

### Specification Errors
```
✗ Specification validation failed:
- Missing required field: agent.description
- Description too short: 45 chars (minimum 60)
- Invalid mode: agent (must be 'primary' or 'subagent')
```

### Output Validation Errors
```
✗ Output validation failed:
- Missing required section: ## Memory Integration
- Missing enforcement marker: MANDATORY WORKFLOW STEPS
- Found placeholder pattern: [TODO]
```

## Development

### Running Tests

```bash
# Test single agent generation
python agent_generator.py specs/test-agent.yaml

# Validate existing agent
python agent_generator.py --validate ../.opencode/agent/developer.md
```

### Adding New Templates

1. Create template in `templates/`
2. Update `AgentGenerator.select_template()` to recognize new mode
3. Add validation rules if needed

### Extending Validation

1. Add rules to `StandardValidator.validate_agent_content()`
2. Update `REQUIRED_SECTIONS` or `SUBAGENT_ENFORCEMENT_MARKERS`
3. Test against existing agents

## Troubleshooting

### ImportError: No module named 'yaml'
```bash
pip install -r requirements.txt
```

### Template not found
```bash
# Check templates directory
ls templates/
# subagent.j2  primary-agent.j2

# Or specify custom path
python agent_generator.py spec.yaml --templates /path/to/templates
```

### Validation failures
```bash
# Skip validation to see generated output
python agent_generator.py spec.yaml --no-validation

# Then manually review and fix issues
```

## Standards Compliance

Generated agents comply with:
- **OpenCode Agent Standard v1.0.0**
- 7 required sections (Overview, Core Responsibilities, Behavioral Guidelines, Workflow, Memory Integration, Quality Standards, Success Criteria)
- YAML frontmatter format (description, mode, name, tools)
- Enforcement patterns (Phase 2 compliance)
- Memory-first workflow integration

## Version

**Version**: 1.0.0  
**Date**: 2025-11-11  
**Compatible with**: OpenCode Agent Standard v1.0.0

## License

Part of the awesome-opencode project.
