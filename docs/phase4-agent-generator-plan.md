# Phase 4: Agent Generator - Implementation Plan

**Date**: 2025-11-11  
**Phase**: 4 of 4 (Agent Generator)  
**Status**: 📋 IN PROGRESS  
**Estimated Duration**: 4-8 hours

---

## Objective

Build an automated agent generator tool to create remaining specialist agents following the OpenCode Agent Standard, enabling "agent to define agents" capability.

---

## Success Criteria

✅ **Must Have**:
- [ ] Generator accepts YAML input specifications
- [ ] Generates agents with hybrid YAML frontmatter
- [ ] All 7 required sections included in output
- [ ] Enforcement patterns automatically injected
- [ ] Validation against OpenCode Agent Standard
- [ ] 10+ specialist agents generated successfully

📋 **Nice to Have**:
- [ ] Template selection (primary vs subagent)
- [ ] Section customization options
- [ ] Batch generation support
- [ ] Generated agent testing suite

---

## Implementation Approach

### Option Selected: **Python Generator**

**Rationale**:
- Rich YAML/Jinja2 template libraries (`pyyaml`, `jinja2`)
- Easy validation and testing
- Cross-platform compatibility
- Clear, maintainable code
- Fast development time

**Alternatives Considered**:
- ❌ Node.js: Adds dependency, less mature YAML libraries
- ❌ Manual templates: No validation, error-prone, slow

---

## Architecture

### Components

```
.opencode/generator/
├── agent_generator.py         # Core generator logic
├── templates/
│   ├── primary-agent.j2       # Jinja2 template for primary agent
│   └── subagent.j2           # Jinja2 template for subagent
├── schemas/
│   └── agent_spec_schema.yaml # Input validation schema
├── validators/
│   └── standard_validator.py  # OpenCode Standard validation
└── specs/
    ├── architect.yaml         # Agent specifications (10+ files)
    ├── ai-engineer.yaml
    ├── database-engineer.yaml
    ├── devops-engineer.yaml
    ├── system-engineer.yaml
    ├── security-engineer.yaml
    ├── qa-engineer.yaml
    ├── backend-tester.yaml
    ├── web-designer.yaml
    └── requirements-engineer.yaml
```

### Data Flow

```
agent_spec.yaml (input)
  ↓
agent_generator.py validates input
  ↓
Selects template (primary vs subagent)
  ↓
Renders Jinja2 template with spec data
  ↓
Injects enforcement patterns
  ↓
Validates against OpenCode Standard
  ↓
Outputs agent .md file
  ↓
Validation report generated
```

---

## Input Schema Design

### Agent Specification Format

```yaml
# specs/devops-engineer.yaml
agent:
  name: devops-engineer                    # File name: devops-engineer.md
  display_name: DevOps Engineer            # Used in title
  mode: subagent                           # primary | subagent
  
  description:
    short: "CI/CD and deployment automation specialist with expertise in pipelines, infrastructure as code, and release management"
  
  role:
    overview: |
      You are a **DevOps Engineer Agent** responsible for:
      - Designing and maintaining CI/CD pipelines
      - Implementing deployment automation
      - Managing infrastructure as code
      - Optimizing build and release processes
    
    operating_principle: "All deployments follow automated, tested, auditable processes"
  
  responsibilities:
    - category: "CI/CD Pipeline Management"
      duties:
        - "Design GitHub Actions/GitLab CI pipelines"
        - "Implement build automation"
        - "Optimize pipeline performance"
    
    - category: "Deployment Automation"
      duties:
        - "Create deployment scripts"
        - "Implement blue-green deployments"
        - "Manage rollback procedures"
    
    - category: "Infrastructure Management"
      duties:
        - "Write IaC (Terraform, CloudFormation)"
        - "Manage container orchestration"
        - "Monitor infrastructure health"
  
  behavioral_guidelines:
    should_do:
      - category: "Automation Focus"
        actions:
          - "Automate all repetitive deployment tasks"
          - "Use IaC for infrastructure changes"
          - "Implement CI/CD best practices"
      
      - category: "Quality Assurance"
        actions:
          - "Test pipelines before deployment"
          - "Validate IaC changes"
          - "Monitor deployment metrics"
    
    should_not_do:
      - category: "Manual Operations"
        actions:
          - "Perform manual deployments to production"
          - "Make infrastructure changes without IaC"
          - "Skip testing in CI/CD pipeline"
      
      - category: "Security Risks"
        actions:
          - "Commit secrets to repositories"
          - "Use overly permissive IAM roles"
          - "Deploy without approval gates"
    
    workflow_example: |
      User Request: "Deploy new API version"
        ↓
      1. Review deployment requirements
      2. Update pipeline configuration
      3. Test in staging environment
      4. Deploy to production via automation
      5. Monitor deployment health
  
  workflow:
    before_implementation:
      - "Review AgentTask deployment requirements"
      - "Search memory for similar deployment patterns"
      - "Validate current infrastructure state"
      - "Plan rollback strategy"
    
    during_implementation:
      - "Implement IaC changes incrementally"
      - "Test pipeline changes in isolated environment"
      - "Document configuration decisions"
      - "Monitor resource utilization"
    
    after_implementation:
      - "Validate deployment succeeded"
      - "Run smoke tests"
      - "Update deployment documentation"
      - "Store deployment patterns in memory"
  
  memory_integration:
    search_before: "deployment patterns, pipeline configurations, infrastructure templates"
    store_after: "successful deployment strategies, pipeline optimizations, IaC patterns"
    categories:
      - "memory/Pattern/ - Reusable deployment patterns"
      - "memory/Learning/ - Deployment issue resolutions"
      - "memory/Knowledge/ - Infrastructure architecture decisions"
  
  quality_standards:
    standards:
      - "All deployments use automated pipelines"
      - "IaC changes peer-reviewed before merge"
      - "Deployment metrics monitored continuously"
      - "Rollback procedures tested regularly"
    
    checklist:
      - "Pipeline tested in non-production environment"
      - "IaC validated with terraform plan/CloudFormation validate"
      - "Deployment documentation updated"
      - "Monitoring alerts configured"
      - "Rollback strategy documented"
  
  success_criteria:
    - "Deployments complete successfully with zero manual intervention"
    - "Infrastructure changes applied via IaC only"
    - "Pipeline failures detected and reported immediately"
    - "Deployment metrics tracked and improving"
    - "Rollback procedures tested and working"
  
  optional_sections:
    tools_and_commands:
      available_tools:
        - name: "Read"
          purpose: "Read IaC and pipeline files"
        - name: "Write"
          purpose: "Create new pipeline configurations"
        - name: "Edit"
          purpose: "Modify existing IaC files"
        - name: "Bash"
          purpose: "Execute deployment commands"
      
      common_commands:
        - category: "CI/CD"
          commands:
            - "gh workflow run deploy.yml"
            - "gitlab-ci-local .gitlab-ci.yml"
        
        - category: "Infrastructure"
          commands:
            - "terraform plan"
            - "terraform apply"
            - "kubectl apply -f deployment.yaml"
        
        - category: "Container Management"
          commands:
            - "docker build -t app:latest ."
            - "docker-compose up -d"
    
    collaboration_patterns:
      - agent: "@Developer"
        patterns:
          - "Receive build artifacts for deployment"
          - "Coordinate release timing"
          - "Share deployment feedback"
      
      - agent: "@Security-Engineer"
        patterns:
          - "Review deployment security configurations"
          - "Implement security scanning in pipelines"
          - "Coordinate security patching"
```

---

## Generator Implementation

### Core Generator (agent_generator.py)

```python
#!/usr/bin/env python3
"""
OpenCode Agent Generator
Generates agent markdown files from YAML specifications
"""

import yaml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import sys
from typing import Dict, Any
import jsonschema

class AgentGenerator:
    """Generate OpenCode-compatible agent files from specifications"""
    
    def __init__(self, template_dir: str = "templates", output_dir: str = ".opencode/agent"):
        self.template_dir = Path(template_dir)
        self.output_dir = Path(output_dir)
        self.env = Environment(loader=FileSystemLoader(self.template_dir))
        self.validator = StandardValidator()
    
    def load_spec(self, spec_path: str) -> Dict[str, Any]:
        """Load agent specification from YAML file"""
        with open(spec_path, 'r') as f:
            spec = yaml.safe_load(f)
        return spec
    
    def validate_spec(self, spec: Dict[str, Any]) -> bool:
        """Validate spec against input schema"""
        # TODO: Implement jsonschema validation
        required_fields = ['agent.name', 'agent.mode', 'agent.description']
        # Simplified validation - expand with jsonschema
        return True
    
    def select_template(self, mode: str) -> str:
        """Select appropriate template based on agent mode"""
        if mode == "primary":
            return "primary-agent.j2"
        elif mode == "subagent":
            return "subagent.j2"
        else:
            raise ValueError(f"Invalid mode: {mode}")
    
    def render_agent(self, spec: Dict[str, Any]) -> str:
        """Render agent markdown from spec"""
        agent_data = spec['agent']
        template_name = self.select_template(agent_data['mode'])
        template = self.env.get_template(template_name)
        
        # Render template with spec data
        rendered = template.render(agent=agent_data)
        
        # Inject enforcement patterns
        rendered = self._inject_enforcement_patterns(rendered, agent_data['mode'])
        
        return rendered
    
    def _inject_enforcement_patterns(self, content: str, mode: str) -> str:
        """Inject mandatory enforcement patterns"""
        # Enforcement patterns differ for primary vs subagent
        if mode == "subagent":
            enforcement_section = self._get_subagent_enforcement()
        else:
            enforcement_section = self._get_primary_enforcement()
        
        # Insert after "## Workflow" section
        # Simplified - in real implementation, use markdown parser
        return content.replace("## Memory Integration", 
                               enforcement_section + "\n\n## Memory Integration")
    
    def _get_subagent_enforcement(self) -> str:
        """Get subagent enforcement patterns"""
        return """## Mandatory Workflow Completion

### Complete AgentTask Execution Enforcement
**CRITICAL**: ALL workflow steps MUST be completed before marking AgentTask as complete.

**MANDATORY WORKFLOW STEPS**:
1. **AgentTask Reading**: Read the COMPLETE AgentTask before starting any work
2. **Memory Search**: Search memory for similar patterns BEFORE implementation (ALWAYS MANDATORY)
3. **Context Review**: Review ALL embedded standards, code examples, and learnings
4. **Implementation Planning**: Outline approach, identify potential issues, plan testing
5. **Implementation**: Follow AgentTask approach, apply standards, use discovered patterns
6. **Testing**: Write and run tests covering requirements
7. **Documentation**: Add comments, update technical docs
8. **Learning Storage**: Store novel solutions and patterns in memory
9. **Comprehensive Summary**: Write detailed completion summary

**BLOCKING PATTERNS** (FORBIDDEN):
- "No memory search needed" → BLOCKED: Memory search ALWAYS mandatory
- "Tests not needed for simple change" → BLOCKED: Tests required per validation criteria
- "Skip documentation" → BLOCKED: Documentation mandatory
- "Quick summary sufficient" → BLOCKED: Comprehensive summary required
- "Partial completion acceptable" → BLOCKED: Complete ALL tasks or flag blocker

**EXECUTION VALIDATION**:
Before claiming completion, validate ALL workflow steps:
- ☐ AgentTask read completely
- ☐ Memory searched
- ☐ Context applied
- ☐ All tasks completed
- ☐ Tests passing
- ☐ Documentation updated
- ☐ Learnings stored
- ☐ Summary written

**ENFORCEMENT RULE**: Execution BLOCKED if any workflow step skipped or incomplete."""
    
    def _get_primary_enforcement(self) -> str:
        """Get primary agent (PM) enforcement patterns"""
        return """## Mandatory Workflow Completion

### Complete Coordination Execution Enforcement
**CRITICAL**: ALL coordination steps MUST be completed before marking task complete.

**MANDATORY WORKFLOW STEPS**:
1. **Complexity Analysis**: Calculate complexity points before creating AgentTask
2. **Memory Search**: Search memory BEFORE starting AgentTask creation (MANDATORY)
3. **Context Embedding**: Embed complete context - NO PLACEHOLDERS allowed
4. **Specialist Selection**: Choose appropriate specialist agent
5. **AgentTask Creation**: Create with all required sections
6. **Explicit Delegation**: Delegate to specialist with clear assignment
7. **Progress Tracking**: Monitor until completion

**BLOCKING PATTERNS** (FORBIDDEN):
- "Quick AgentTask without memory search" → BLOCKED: Memory search MANDATORY
- "Create AgentTask with placeholders" → BLOCKED: Complete context required
- "PM executes technical work directly" → BLOCKED: MUST delegate to specialists
- "Skip complexity calculation" → BLOCKED: Complexity analysis required
- "Create large AgentTask (>15 pts)" → BLOCKED: MUST create story and break down
- "Delegate without complete context" → BLOCKED: Context embedding mandatory
- "No specialist assigned" → BLOCKED: Explicit specialist assignment required

**EXECUTION VALIDATION**:
Before claiming coordination completion, validate:
- ☐ Complexity calculated and documented
- ☐ Memory searched
- ☐ Complete context embedded (no placeholders)
- ☐ Specialist selected and named
- ☐ Delegation performed
- ☐ No technical commands executed by PM
- ☐ Work tracked until completion

**ENFORCEMENT RULE**: Coordination BLOCKED if any step skipped or incomplete."""
    
    def generate(self, spec_path: str) -> str:
        """Generate agent from specification file"""
        # Load and validate spec
        spec = self.load_spec(spec_path)
        if not self.validate_spec(spec):
            raise ValueError(f"Invalid specification: {spec_path}")
        
        # Render agent
        agent_content = self.render_agent(spec)
        
        # Validate output
        if not self.validator.validate_agent_content(agent_content):
            raise ValueError("Generated agent does not meet OpenCode Standard")
        
        # Write to file
        agent_name = spec['agent']['name']
        output_path = self.output_dir / f"{agent_name}.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w') as f:
            f.write(agent_content)
        
        print(f"✅ Generated: {output_path}")
        return str(output_path)
    
    def generate_batch(self, spec_dir: str) -> list[str]:
        """Generate all agents from specs directory"""
        spec_files = Path(spec_dir).glob("*.yaml")
        generated = []
        
        for spec_file in spec_files:
            try:
                output_path = self.generate(str(spec_file))
                generated.append(output_path)
            except Exception as e:
                print(f"❌ Failed to generate {spec_file}: {e}")
        
        return generated


class StandardValidator:
    """Validate generated agents against OpenCode Agent Standard"""
    
    REQUIRED_SECTIONS = [
        "## Overview",
        "## Core Responsibilities",
        "## Behavioral Guidelines",
        "## Workflow",
        "## Memory Integration",
        "## Quality Standards",
        "## Success Criteria"
    ]
    
    def validate_agent_content(self, content: str) -> bool:
        """Validate agent markdown content"""
        # Check all required sections present
        for section in self.REQUIRED_SECTIONS:
            if section not in content:
                print(f"❌ Missing required section: {section}")
                return False
        
        # Check YAML frontmatter
        if not content.startswith("---"):
            print("❌ Missing YAML frontmatter")
            return False
        
        # Check enforcement patterns present (for subagents)
        if "mode: subagent" in content:
            if "MANDATORY WORKFLOW STEPS" not in content:
                print("❌ Missing enforcement patterns for subagent")
                return False
        
        return True


# CLI
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate OpenCode agents from specifications")
    parser.add_argument("spec", help="Path to agent specification YAML file or directory")
    parser.add_argument("--output-dir", default=".opencode/agent", help="Output directory")
    parser.add_argument("--batch", action="store_true", help="Generate all specs in directory")
    
    args = parser.parse_args()
    
    generator = AgentGenerator(output_dir=args.output_dir)
    
    if args.batch:
        print(f"Generating agents from specs in: {args.spec}")
        generated = generator.generate_batch(args.spec)
        print(f"\n✅ Generated {len(generated)} agents")
    else:
        print(f"Generating agent from: {args.spec}")
        output = generator.generate(args.spec)
        print(f"\n✅ Agent generated: {output}")
```

### Jinja2 Template (subagent.j2)

```jinja2
---
# OpenCode required fields
description: {{ agent.description.short }}
mode: {{ agent.mode }}

# Optional Claude Code compatibility
name: {{ agent.name }}
tools: Edit, MultiEdit, Read, Write, Bash, Grep, Glob, LS
---

## Overview

{{ agent.role.overview }}

**{{ agent.role.operating_principle }}**

---

## Core Responsibilities

{% for responsibility in agent.responsibilities %}
### {{ loop.index }}. {{ responsibility.category }}
{% for duty in responsibility.duties %}
- {{ duty }}
{% endfor %}

{% endfor %}
---

## Behavioral Guidelines

### ✅ YOU SHOULD

{% for guideline in agent.behavioral_guidelines.should_do %}
**{{ guideline.category }}**:
{% for action in guideline.actions %}
- {{ action }}
{% endfor %}

{% endfor %}
### ❌ YOU SHOULD NOT

{% for guideline in agent.behavioral_guidelines.should_not_do %}
**{{ guideline.category }}**:
{% for action in guideline.actions %}
- {{ action }}
{% endfor %}

{% endfor %}
**Pattern to Follow:**
```
{{ agent.behavioral_guidelines.workflow_example }}
```

---

## Workflow

### Before Implementation

{% for step in agent.workflow.before_implementation %}
{{ loop.index }}. {{ step }}
{% endfor %}

### During Implementation

{% for step in agent.workflow.during_implementation %}
{{ loop.index }}. {{ step }}
{% endfor %}

### After Implementation

{% for step in agent.workflow.after_implementation %}
{{ loop.index }}. {{ step }}
{% endfor %}

---

## Memory Integration

### Before Implementation
Search for:
- {{ agent.memory_integration.search_before }}

### After Implementation
Store if novel:
- {{ agent.memory_integration.store_after }}

**Storage Location:**
{% for category in agent.memory_integration.categories %}
- {{ category }}
{% endfor %}

---

## Quality Standards

### Standards
{% for standard in agent.quality_standards.standards %}
- {{ standard }}
{% endfor %}

### Quality Checklist
Before completing AgentTask:

{% for item in agent.quality_standards.checklist %}
- [ ] {{ item }}
{% endfor %}

---

{% if agent.optional_sections.collaboration_patterns %}
## Collaboration

{% for collab in agent.optional_sections.collaboration_patterns %}
### With {{ collab.agent }}
{% for pattern in collab.patterns %}
- {{ pattern }}
{% endfor %}

{% endfor %}
---

{% endif %}
{% if agent.optional_sections.tools_and_commands %}
## Tools and Commands

### Available Tools
{% for tool in agent.optional_sections.tools_and_commands.available_tools %}
- **{{ tool.name }}**: {{ tool.purpose }}
{% endfor %}

### Common Commands
{% for category in agent.optional_sections.tools_and_commands.common_commands %}
```bash
# {{ category.category }}
{% for cmd in category.commands %}
{{ cmd }}
{% endfor %}
```

{% endfor %}
---

{% endif %}
## Success Criteria

**You're successful when:**
{% for criterion in agent.success_criteria %}
- {{ criterion }}
{% endfor %}

---

**Remember**: {{ agent.role.operating_principle }}
```

---

## Implementation Phases

### Phase 4.1: Generator Core (2-3 hours)
- [x] Design input schema
- [ ] Implement `AgentGenerator` class
- [ ] Create Jinja2 templates (primary + subagent)
- [ ] Implement enforcement pattern injection
- [ ] Add validation logic
- [ ] Write CLI interface
- [ ] Test with single agent spec

### Phase 4.2: Agent Specifications (2-3 hours)
- [ ] Create specifications for 10 agents:
  - [ ] architect.yaml
  - [ ] ai-engineer.yaml
  - [ ] database-engineer.yaml
  - [ ] devops-engineer.yaml
  - [ ] system-engineer.yaml
  - [ ] security-engineer.yaml
  - [ ] qa-engineer.yaml
  - [ ] backend-tester.yaml
  - [ ] web-designer.yaml
  - [ ] requirements-engineer.yaml

### Phase 4.3: Generation & Validation (1-2 hours)
- [ ] Generate all agents using batch mode
- [ ] Validate each generated agent
- [ ] Manual review of generated agents
- [ ] Fix any generation issues
- [ ] Finalize agent library

### Phase 4.4: Documentation (30 min - 1 hour)
- [ ] Write generator usage guide
- [ ] Document input schema
- [ ] Create example specifications
- [ ] Write phase 4 completion summary
- [ ] Update agent standardization tracker

---

## Deliverables

### Code Artifacts
- [ ] `.opencode/generator/agent_generator.py` - Core generator
- [ ] `.opencode/generator/templates/subagent.j2` - Subagent template
- [ ] `.opencode/generator/templates/primary-agent.j2` - Primary agent template
- [ ] `.opencode/generator/schemas/agent_spec_schema.yaml` - Input schema
- [ ] `.opencode/generator/validators/standard_validator.py` - Validator

### Specifications
- [ ] `.opencode/generator/specs/*.yaml` - 10+ agent specs

### Generated Agents
- [ ] `.opencode/agent/architect.md`
- [ ] `.opencode/agent/ai-engineer.md`
- [ ] `.opencode/agent/database-engineer.md`
- [ ] `.opencode/agent/devops-engineer.md`
- [ ] `.opencode/agent/system-engineer.md`
- [ ] `.opencode/agent/security-engineer.md`
- [ ] `.opencode/agent/qa-engineer.md`
- [ ] `.opencode/agent/backend-tester.md`
- [ ] `.opencode/agent/web-designer.md`
- [ ] `.opencode/agent/requirements-engineer.md`

### Documentation
- [ ] `docs/agent-generator-guide.md` - Usage documentation
- [ ] `docs/phase4-agent-generator-summary.md` - Completion report
- [ ] Updated `docs/agent-standardization-tracker.md` - 100% complete

---

## Testing Strategy

### Generator Testing
1. **Unit Tests**: Test each component (validator, renderer, injector)
2. **Integration Test**: Generate single agent, validate output
3. **Batch Test**: Generate all agents, validate all outputs
4. **Regression Test**: Ensure existing agents (pm.md, developer.md) remain valid

### Agent Validation
1. **Structure Validation**: All 7 required sections present
2. **Frontmatter Validation**: YAML valid, required fields present
3. **Enforcement Validation**: Mandatory patterns injected correctly
4. **Content Quality**: Sections complete, no placeholders

---

## Risk Mitigation

### Risk: Generated agents don't match quality of hand-crafted agents
**Mitigation**: 
- Start with high-quality templates from validated PM/Developer agents
- Manual review of first generated agent
- Iterate template based on feedback

### Risk: Template complexity makes maintenance difficult
**Mitigation**:
- Keep templates simple and readable
- Document template syntax
- Use includes for common sections

### Risk: Specification format too verbose
**Mitigation**:
- Create minimal spec example
- Support optional sections
- Provide defaults for common values

---

## Next Steps After Phase 4

1. **Integration Testing**: Test agents with real AgentTasks
2. **Agent Library Documentation**: Create comprehensive agent library guide
3. **Best Practices Guide**: Document patterns discovered during generation
4. **Version Control**: Tag release of agent standardization project
5. **Share Knowledge**: Create presentation/demo of agent system

---

**Status**: 📋 Ready to begin implementation  
**Start Date**: 2025-11-11  
**Target Completion**: 2025-11-11 (1 day)
