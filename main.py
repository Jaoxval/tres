from tres.engine import AnalysisEngine
from tres.models import AnalysisInput


def main():
    print("Tres v0.1")
    print("Identity Intelligence Engine")
    print()

    email = input("Email: ")

    analysis_input = AnalysisInput(email=email)

    engine = AnalysisEngine()

    findings = engine.analyze(analysis_input)

    for finding in findings:
        print(
            f"[{finding.source}] "
            f"{finding.key}: {finding.value} "
            f"(confidence={finding.confidence})"
        )


if __name__ == "__main__":
    main()