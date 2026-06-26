from tres.models import Finding


class FakeEmailConnector:
    def collect(self, email: str) -> list[Finding]:
        return [
            Finding(
                source="email",
                category="provider",
                key="email_provider",
                value="gmail",
                confidence=1.0,
            )
        ]