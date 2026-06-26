from tres.connector import Connector
from tres.models import AnalysisInput, Finding


class FakeEmailConnector(Connector):

    def collect(self, analysis_input: AnalysisInput) -> list[Finding]:
        return [
            Finding(
                source="email",
                category="provider",
                key="email_provider",
                value="gmail",
                confidence=1.0,
            )
        ]