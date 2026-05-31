# Pits Architecture

## Overview

Pits is composed of three main layers:

1. **Agent Layer** - Multi-agent orchestration
2. **Capability Layer** - LLM, parsing, templates, retrieval
3. **Data Layer** - Knowledge base, templates, compliance rules

## Agent Orchestration Flow

```
User Input → Orchestrator → RequirementAgent → WriterAgent → ComplianceAgent → FormatterAgent → Export
```

Each agent specializes in one phase of bid document generation.