from tres.connector import Connector
from tres.models import AnalysisInput, Finding


KNOWN_PROVIDERS = {
    "gmail.com": "Gmail",
    "googlemail.com": "Gmail",

    "outlook.com": "Outlook",
    "hotmail.com": "Outlook",
    "live.com": "Outlook",
    "msn.com": "Outlook",

    "icloud.com": "Apple",

    "yahoo.com": "Yahoo",

    "proton.me": "Proton",
    "protonmail.com": "Proton",
}


class EmailProviderConnector(Connector):

    def collect(self, analysis_input: AnalysisInput) -> list[Finding]:

        if analysis_input.email is None:
            return []

        domain = analysis_input.email.split("@")[-1].lower()

        provider = KNOWN_PROVIDERS.get(domain, "Unknown")

        confidence = 1.0 if provider != "Unknown" else 0.5

        return [
            Finding(
                source="email",
                category="provider",
                key="provider",
                value=provider,
                confidence=confidence,
                evidence={
                    "domain": domain,
                },
            )
        ]