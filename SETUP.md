# SETUP.md

# Setup Guide – Start Fast

This guide shows the minimal steps required to install, configure, and begin using the multi-agent system.

No explanations.
No theory.
Just the fastest way to get running.

---

## 1. Install OpenCode

```bash
npm install -g opencode
```

Or update:

```bash
opencode upgrade
```

---

## 2. Clone Your Repository

```bash
git clone <your-repo-url>
cd <your-repo>
```

---

## 3. Review the Required Files

Make sure these exist:

```
AGENTS.md
.opencode/
  agents/
  system/
  agenttasks-templates/
  agenttasks/
  memory/
  skills/
```

If the structure is missing, copy the template from your starter repository.

---

## 4. Check MCP Configuration (Optional)

If using MCP servers:

```bash
cat opencode.jsonc
```

Enable or disable MCP integrations as needed.

---

## 5. Start OpenCode in Your Project

```bash
opencode .
```

This loads:

* all agents
* agent definitions
* Skills
* Memory
* workflows
* AgentTask templates

---

## 6. Verify Agent Availability

Inside OpenCode:

```bash
@Project-Manager help
```

If you see the help text, everything works.

---

## 7. Create Your First AgentTask

Example:

```bash
@Project-Manager Lets build something cool!
```

This will:

1. analyze complexity
2. create the task file under `.opencode/agenttasks/`
3. embed relevant Skills
4. reference Memory if available
5. assign it to the correct agent

---

## 8. Execute a Task

Once an AgentTask is created:

```bash
@Developer implement .opencode/agenttasks/<task-file>.md
```

Developer will:

1. read the task
2. search Memory
3. load required Skills
4. implement deliverables
5. run validations
6. produce a completion summary

---

## 9. Add a New Skill (Optional)

Create a new folder:

```
.opencode/skills/<skill-name>/
```

Add:

* `metadata.yaml`
* `overview.md`
* `patterns/` (optional)
* `workflows/` (optional)

The system picks it up automatically.

---

## 10. Add a Memory Entry (When Required)

Memory entries are created automatically when AgentTasks require it.

To add manually:

```
.opencode/memory/<category>/<entry>.md
```

Follow the schema in `MEMORY.md`.
