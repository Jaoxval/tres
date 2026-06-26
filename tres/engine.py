from tres.connectors import FakeEmailConnector
from tres.models import Finding


class AnalysisEngine:
    def __init__(self):
        self.connectors = [
            FakeEmailConnector(),
        ]

    def collect(self, email: str) -> list[Finding]:
        findings = []

        for connector in self.connectors:
            findings.extend(connector.collect(email))

        return findings