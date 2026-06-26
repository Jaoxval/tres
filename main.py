from tres.engine import AnalysisEngine
from tres.models import AnalysisInput


def main():
    print("Tres v0.1")
    print("Identity Intelligence Engine")
    print()

    analysis_input = AnalysisInput(
        email="joao@gmail.com",
    )

    engine = AnalysisEngine()

    findings = engine.analyze(analysis_input)

    for finding in findings:
        print(
            f"[{finding.source}] "
            f"{finding.key}: {finding.value}"
        )


if __name__ == "__main__":
    main()