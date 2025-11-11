#!/usr/bin/env python3
"""
OpenCode Agent Generator
Generates standardized agent markdown files from YAML specifications.
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import yaml
from jinja2 import Environment, FileSystemLoader, Template
import re


class StandardValidator:
    """Validates agents against OpenCode Agent Standard."""
    
    REQUIRED_SECTIONS = [
        "## Overview",
        "## Core Responsibilities",
        "## Behavioral Guidelines",
        "## Workflow",
        "## Memory Integration",
        "## Quality Standards",
        "## Success Criteria"
    ]
    
    SUBAGENT_ENFORCEMENT_MARKERS = [
        "MANDATORY WORKFLOW STEPS",
        "BLOCKING PATTERNS",
        "EXECUTION VALIDATION",
        "ENFORCEMENT RULE"
    ]
    
    def validate_agent_content(self, content: str, mode: str) -> Tuple[bool, List[str]]:
        """
        Validate generated agent content against standard.
        
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # Check YAML frontmatter
        if not content.startswith("---"):
            errors.append("Missing YAML frontmatter")
        else:
            # Extract frontmatter
            parts = content.split("---", 2)
            if len(parts) < 3:
                errors.append("Invalid YAML frontmatter structure")
            else:
                try:
                    frontmatter = yaml.safe_load(parts[1])
                    
                    # Check required fields
                    if "description" not in frontmatter:
                        errors.append("Missing 'description' in frontmatter")
                    elif len(frontmatter["description"]) < 60:
                        errors.append(f"Description too short: {len(frontmatter['description'])} chars (minimum 60)")
                    elif len(frontmatter["description"]) > 150:
                        errors.append(f"Description too long: {len(frontmatter['description'])} chars (maximum 150)")
                    
                    if "mode" not in frontmatter:
                        errors.append("Missing 'mode' in frontmatter")
                    elif frontmatter["mode"] not in ["primary", "subagent"]:
                        errors.append(f"Invalid mode: {frontmatter['mode']} (must be 'primary' or 'subagent')")
                        
                except yaml.YAMLError as e:
                    errors.append(f"Invalid YAML in frontmatter: {e}")
        
        # Check required sections
        for section in self.REQUIRED_SECTIONS:
            if section not in content:
                errors.append(f"Missing required section: {section}")
        
        # Check enforcement patterns for subagent mode
        if mode == "subagent":
            for marker in self.SUBAGENT_ENFORCEMENT_MARKERS:
                if marker not in content:
                    errors.append(f"Missing enforcement marker: {marker}")
        
        # Check for placeholders
        placeholder_patterns = [
            r"\[TODO\]",
            r"\[FILL IN\]",
            r"\[PLACEHOLDER\]",
            r"\[ADD CONTENT\]",
            r"\{TODO\}",
            r"\{FILL IN\}"
        ]
        
        for pattern in placeholder_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                errors.append(f"Found placeholder pattern: {pattern}")
        
        return (len(errors) == 0, errors)


class AgentGenerator:
    """Generates agents from YAML specifications."""
    
    def __init__(self, template_dir: Path, output_dir: Path):
        """
        Initialize generator.
        
        Args:
            template_dir: Directory containing Jinja2 templates
            output_dir: Directory to save generated agents
        """
        self.template_dir = template_dir
        self.output_dir = output_dir
        self.validator = StandardValidator()
        
        # Setup Jinja2 environment
        self.jinja_env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True
        )
    
    def load_spec(self, spec_path: Path) -> Dict:
        """Load and parse YAML specification."""
        try:
            with open(spec_path, 'r') as f:
                spec = yaml.safe_load(f)
            return spec
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML in {spec_path}: {e}")
        except FileNotFoundError:
            raise FileNotFoundError(f"Specification file not found: {spec_path}")
    
    def validate_spec(self, spec: Dict) -> Tuple[bool, List[str]]:
        """
        Validate specification against input schema.
        
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # Check top-level structure
        if "agent" not in spec:
            errors.append("Missing 'agent' root key")
            return (False, errors)
        
        agent = spec["agent"]
        
        # Required fields
        required_fields = ["name", "display_name", "mode", "description", "role", 
                          "responsibilities", "behavioral_guidelines", "workflow",
                          "memory_integration", "quality_standards", "success_criteria"]
        
        for field in required_fields:
            if field not in agent:
                errors.append(f"Missing required field: agent.{field}")
        
        # Validate field types and constraints
        if "name" in agent:
            name = agent["name"]
            if not re.match(r"^[a-z][a-z0-9-]*$", name):
                errors.append(f"Invalid name format: {name} (must be lowercase, hyphen-separated)")
        
        if "mode" in agent and agent["mode"] not in ["primary", "subagent"]:
            errors.append(f"Invalid mode: {agent['mode']} (must be 'primary' or 'subagent')")
        
        if "description" in agent:
            desc = agent["description"]
            if "short" not in desc:
                errors.append("Missing 'description.short' field")
            elif len(desc["short"]) < 60:
                errors.append(f"Description too short: {len(desc['short'])} chars (minimum 60)")
            elif len(desc["short"]) > 150:
                errors.append(f"Description too long: {len(desc['short'])} chars (maximum 150)")
        
        return (len(errors) == 0, errors)
    
    def select_template(self, mode: str) -> str:
        """Select appropriate template based on agent mode."""
        if mode == "primary":
            return "primary-agent.j2"
        elif mode == "subagent":
            return "subagent.j2"
        else:
            raise ValueError(f"Unknown mode: {mode}")
    
    def render_agent(self, spec: Dict) -> str:
        """
        Render agent markdown from specification.
        
        Args:
            spec: Agent specification dictionary
            
        Returns:
            Rendered agent markdown content
        """
        agent = spec["agent"]
        mode = agent["mode"]
        
        # Select template
        template_name = self.select_template(mode)
        template = self.jinja_env.get_template(template_name)
        
        # Render template
        content = template.render(agent=agent)
        
        # Inject enforcement patterns
        content = self._inject_enforcement_patterns(content, mode)
        
        return content
    
    def _inject_enforcement_patterns(self, content: str, mode: str) -> str:
        """
        Inject appropriate enforcement patterns into content.
        
        Injection point: After "## Workflow" section, before "## Memory Integration"
        """
        if mode == "subagent":
            enforcement_section = self._get_subagent_enforcement()
        elif mode == "primary":
            enforcement_section = self._get_primary_enforcement()
        else:
            return content
        
        # Find injection point
        pattern = r"(## Workflow.*?)(---\s*\n\s*)(## Memory Integration)"
        replacement = r"\1\2" + enforcement_section + r"\n\n\3"
        
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        return content
    
    def _get_subagent_enforcement(self) -> str:
        """Get enforcement patterns for subagent mode."""
        return """## Mandatory Workflow Completion

### Complete AgentTask Execution Enforcement
**CRITICAL**: ALL workflow steps MUST be completed before marking AgentTask as complete.

**MANDATORY WORKFLOW STEPS**:
1. **AgentTask Reading**: Read the COMPLETE AgentTask before starting any work - understand goal, requirements, success criteria, validation steps
2. **Memory Search**: Search memory for similar patterns, known issues, and past solutions BEFORE implementation (ALWAYS MANDATORY)
3. **Context Review**: Review ALL embedded standards, code examples, and learnings provided in AgentTask
4. **Implementation Planning**: Outline approach, identify potential issues, plan testing strategy
5. **Code Implementation**: Follow AgentTask approach, apply standards from AGENTS.md, use discovered patterns
6. **Test Development**: Write unit tests covering happy path, edge cases, and error conditions as you implement
7. **Documentation**: Add code comments for complex logic, update technical docs, explain non-obvious decisions
8. **Learning Storage**: Store novel solutions, gotchas, and patterns in memory
9. **Comprehensive Summary**: Write detailed completion summary covering what/how/test/follow-up

**BLOCKING PATTERNS** (FORBIDDEN):
- "No memory search needed" → BLOCKED: Memory search is ALWAYS mandatory, no exceptions for "simple" changes
- "Tests not needed for simple change" → BLOCKED: Tests required per AgentTask validation criteria, complexity is irrelevant
- "Skip documentation" → BLOCKED: Documentation is mandatory, even for self-explanatory code
- "Self-documenting code, no comments needed" → BLOCKED: Explicit documentation required for complex logic
- "No learnings to store" → BLOCKED: Must evaluate and document if solution is novel or solves a problem
- "Quick summary sufficient" → BLOCKED: Comprehensive summary required (what/how/test/follow-up sections)
- "Partial AgentTask completion acceptable" → BLOCKED: Complete ALL tasks listed or explicitly flag blocker
- "Skip validation criteria" → BLOCKED: MUST verify ALL success criteria met before completion

**EXECUTION VALIDATION**:
Before claiming AgentTask completion, validate ALL workflow steps completed:
- ☐ AgentTask read completely (all sections: goal, why, context, implementation, validation, completion)
- ☐ Memory searched (at least 1 search performed, patterns found and reviewed)
- ☐ Embedded context applied (standards, examples, learnings incorporated)
- ☐ All implementation tasks completed (every task in AgentTask.implementation.tasks checked off)
- ☐ Tests written and passing (unit tests cover requirements, all tests green)
- ☐ Code documented per standards (complex logic commented, technical docs updated)
- ☐ Novel learnings stored in memory (evaluation performed, patterns stored if applicable)
- ☐ Comprehensive summary written (includes: what was implemented, how it works, how to test/use, follow-up)

**ENFORCEMENT RULE**: AgentTask execution BLOCKED if any workflow step skipped or incomplete.

---"""
    
    def _get_primary_enforcement(self) -> str:
        """Get enforcement patterns for primary mode."""
        return """## Mandatory Workflow Completion

### Complete Coordination Execution Enforcement
**CRITICAL**: ALL workflow steps MUST be completed before marking coordination execution as complete.

**MANDATORY WORKFLOW STEPS**:
1. **Complexity Analysis**: Calculate complexity points (File Impact + Code Volume + Integrations + Security + Coordination) before creating any AgentTask
2. **Memory Search**: Search memory for similar patterns, past solutions, and relevant learnings BEFORE starting AgentTask creation
3. **Context Embedding**: Embed complete context including standards from AGENTS.md, discovered patterns, and code examples - NO PLACEHOLDERS allowed
4. **Specialist Selection**: Choose appropriate specialist agent based on work type (Developer, DevOps, QA, etc.)
5. **AgentTask Creation**: Create AgentTask with all required sections (goal, why, context, implementation, validation, completion)
6. **Explicit Delegation**: Delegate to specialist with clear assignment
7. **Progress Tracking**: Monitor progress and track until completion

**BLOCKING PATTERNS** (FORBIDDEN):
- "Quick AgentTask without memory search" → BLOCKED: Memory search is MANDATORY for every AgentTask
- "Create AgentTask with placeholders" → BLOCKED: Complete context embedding required, no "TODO", "FILL IN", or "[ADD CONTENT]" allowed
- "PM executes technical work directly" → BLOCKED: PM MUST delegate all technical work to specialists
- "Skip complexity calculation" → BLOCKED: Complexity analysis required for proper tier selection
- "Create large AgentTask (>15 pts)" → BLOCKED: MUST create story first and break down into smaller tasks
- "Delegate without complete context" → BLOCKED: Context embedding is mandatory before delegation
- "No specialist assigned" → BLOCKED: Every AgentTask MUST have explicit specialist assignment

**EXECUTION VALIDATION**:
Before claiming coordination task completion, validate ALL workflow steps completed:
- ☐ Complexity calculated and documented (with breakdown: File Impact, Code Volume, etc.)
- ☐ Memory searched for relevant patterns (at least 1 search performed)
- ☐ Complete context embedded (verified no placeholders: "TODO", "FILL IN", "[PLACEHOLDER]")
- ☐ Appropriate specialist selected and named
- ☐ Explicit delegation performed (clear assignment statement)
- ☐ No technical commands executed by PM (no `dotnet`, `npm`, `build`, `test`, etc.)
- ☐ Work tracked until specialist reports completion

**ENFORCEMENT RULE**: Coordination execution BLOCKED if any workflow step skipped or incomplete.

---"""
    
    def generate(self, spec_path: Path, validate_output: bool = True) -> Tuple[bool, Optional[str], List[str]]:
        """
        Generate agent from specification.
        
        Args:
            spec_path: Path to YAML specification
            validate_output: Whether to validate generated content
            
        Returns:
            Tuple of (success, agent_content, errors_or_messages)
        """
        messages = []
        
        # Load specification
        try:
            spec = self.load_spec(spec_path)
            messages.append(f"✓ Loaded specification: {spec_path}")
        except Exception as e:
            return (False, None, [f"✗ Failed to load specification: {e}"])
        
        # Validate specification
        valid, errors = self.validate_spec(spec)
        if not valid:
            return (False, None, [f"✗ Specification validation failed:"] + errors)
        messages.append("✓ Specification validated")
        
        # Render agent
        try:
            content = self.render_agent(spec)
            messages.append("✓ Agent rendered from template")
        except Exception as e:
            return (False, None, messages + [f"✗ Template rendering failed: {e}"])
        
        # Validate output
        if validate_output:
            mode = spec["agent"]["mode"]
            valid, errors = self.validator.validate_agent_content(content, mode)
            if not valid:
                return (False, content, messages + [f"✗ Output validation failed:"] + errors)
            messages.append("✓ Output validated against OpenCode Standard")
        
        # Save agent file
        agent_name = spec["agent"]["name"]
        output_path = self.output_dir / f"{agent_name}.md"
        
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w') as f:
                f.write(content)
            messages.append(f"✓ Agent saved: {output_path}")
        except Exception as e:
            return (False, content, messages + [f"✗ Failed to save agent: {e}"])
        
        return (True, content, messages)
    
    def generate_batch(self, spec_dir: Path) -> Dict[str, Tuple[bool, List[str]]]:
        """
        Generate all agents from specifications directory.
        
        Args:
            spec_dir: Directory containing YAML specifications
            
        Returns:
            Dictionary mapping spec filename to (success, messages)
        """
        results = {}
        
        spec_files = list(spec_dir.glob("*.yaml")) + list(spec_dir.glob("*.yml"))
        
        for spec_file in spec_files:
            print(f"\n{'='*60}")
            print(f"Generating: {spec_file.name}")
            print('='*60)
            
            success, content, messages = self.generate(spec_file)
            
            for msg in messages:
                print(msg)
            
            results[spec_file.name] = (success, messages)
        
        return results
    
    def validate_existing_agent(self, agent_path: Path) -> Tuple[bool, List[str]]:
        """
        Validate an existing agent file.
        
        Args:
            agent_path: Path to agent markdown file
            
        Returns:
            Tuple of (is_valid, list_of_errors_or_messages)
        """
        try:
            with open(agent_path, 'r') as f:
                content = f.read()
            
            # Extract mode from frontmatter
            parts = content.split("---", 2)
            if len(parts) < 3:
                return (False, ["Invalid file structure: missing frontmatter"])
            
            frontmatter = yaml.safe_load(parts[1])
            mode = frontmatter.get("mode", "subagent")
            
            # Validate
            valid, errors = self.validator.validate_agent_content(content, mode)
            
            if valid:
                return (True, [f"✓ Agent valid: {agent_path}"])
            else:
                return (False, [f"✗ Agent validation failed: {agent_path}"] + errors)
                
        except Exception as e:
            return (False, [f"✗ Failed to validate agent: {e}"])


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="OpenCode Agent Generator - Generate standardized agents from YAML specifications"
    )
    
    parser.add_argument(
        "spec",
        type=Path,
        help="Path to YAML specification file or directory (for batch mode)"
    )
    
    parser.add_argument(
        "--batch",
        action="store_true",
        help="Batch mode: generate all specs in directory"
    )
    
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate existing agent file instead of generating"
    )
    
    parser.add_argument(
        "--templates",
        type=Path,
        default=Path(__file__).parent / "templates",
        help="Path to templates directory (default: ./templates)"
    )
    
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parent.parent / "agent",
        help="Path to output directory (default: ../.opencode/agent)"
    )
    
    parser.add_argument(
        "--no-validation",
        action="store_true",
        help="Skip output validation (not recommended)"
    )
    
    args = parser.parse_args()
    
    # Initialize generator
    generator = AgentGenerator(args.templates, args.output)
    
    # Validate mode
    if args.validate:
        if not args.spec.exists():
            print(f"✗ Agent file not found: {args.spec}")
            sys.exit(1)
        
        valid, messages = generator.validate_existing_agent(args.spec)
        
        for msg in messages:
            print(msg)
        
        sys.exit(0 if valid else 1)
    
    # Batch generation mode
    if args.batch:
        if not args.spec.is_dir():
            print(f"✗ Not a directory: {args.spec}")
            sys.exit(1)
        
        print(f"Batch generation from: {args.spec}")
        print(f"Output directory: {args.output}")
        print()
        
        results = generator.generate_batch(args.spec)
        
        # Summary
        print(f"\n{'='*60}")
        print("GENERATION SUMMARY")
        print('='*60)
        
        success_count = sum(1 for success, _ in results.values() if success)
        total_count = len(results)
        
        print(f"✓ Successful: {success_count}/{total_count}")
        print(f"✗ Failed: {total_count - success_count}/{total_count}")
        
        sys.exit(0 if success_count == total_count else 1)
    
    # Single agent generation
    if not args.spec.exists():
        print(f"✗ Specification file not found: {args.spec}")
        sys.exit(1)
    
    print(f"Generating agent from: {args.spec}")
    print(f"Output directory: {args.output}")
    print()
    
    success, content, messages = generator.generate(
        args.spec,
        validate_output=not args.no_validation
    )
    
    for msg in messages:
        print(msg)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
