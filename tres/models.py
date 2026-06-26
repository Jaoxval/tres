from dataclasses import dataclass, field
from typing import Any


@dataclass
class AnalysisInput:
    email: str | None = None


@dataclass
class Finding:
    source: str
    category: str
    key: str
    value: Any
    confidence: float
    evidence: dict[str, Any] = field(default_factory=dict)