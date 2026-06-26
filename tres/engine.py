from tres.connectors import FakeEmailConnector
from tres.models import AnalysisInput, Finding


class AnalysisEngine:

    def __init__(self):
        self.connectors = [
            FakeEmailConnector(),
        ]

    def analyze(self, analysis_input: AnalysisInput) -> list[Finding]:
        findings: list[Finding] = []

        for connector in self.connectors:
            findings.extend(
                connector.collect(analysis_input)
            )

        return findings