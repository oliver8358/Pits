# Pits API Reference

## Core Modules

### Orchestrator
- `Orchestrator.register_agent(agent, stage)` - Register an agent for a workflow stage
- `Orchestrator.run(initial_input)` - Execute the full workflow

### Agents
- `RequirementAgent()` - Parse bid requirements
- `WriterAgent()` - Generate bid content
- `ComplianceAgent()` - Validate compliance
- `FormatterAgent()` - Format document

## Capabilities
- `DocumentParser.parse(path)` - Parse PDF/Word/TXT
- `TemplateEngine.render(name, context)` - Render bid template
- `LLMClient.chat(messages)` - Call LLM
- `KnowledgeRetriever.search(query)` - Search knowledge base