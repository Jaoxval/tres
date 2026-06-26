from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class Finding:
    source: str              # de dónde viene (dns, email, github, etc.)
    category: str            # tipo de señal (e.g. email_infrastructure)
    key: str                 # qué se encontró (e.g. mx_records)
    value: Any               # valor del hallazgo (e.g. present, list, true/false)
    confidence: float        # 0.0 - 1.0
    evidence: Optional[Dict[str, Any]] = None