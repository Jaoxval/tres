# Tres

> Identity Intelligence Engine

Tres is an open-source engine that transforms publicly available information into structured identity insights.

Instead of assigning a "risk score" to a person, Tres focuses on collecting evidence, identifying signals, and generating transparent reports that help analysts make informed decisions.

## Vision

Analysts often spend valuable time searching across multiple public sources to verify identity information.

Tres aims to automate that process by:

- Collecting information from multiple public sources.
- Structuring findings into a common format.
- Detecting consistency and inconsistencies.
- Generating human-readable reports.
- Remaining transparent and explainable.

## Project Status

🚧 Early development (MVP)

Current goal:

- [ ] Analyze an email address.
- [ ] Produce structured findings.
- [ ] Generate a simple console report.

## Planned Architecture

```
Input
   │
   ▼
Connectors
   │
   ▼
Findings
   │
   ▼
Analysis Engine
   │
   ▼
Report
```

## Long-term Roadmap

- Email analysis
- Domain analysis
- DNS inspection
- WHOIS lookup
- GitHub connector
- Identity consistency engine
- AI-generated summaries
- Web interface
- Public API

## Principles

- Explainability over black-box scoring.
- Evidence before conclusions.
- Modular architecture.
- Privacy-first design.
- Open source.

## License

MIT