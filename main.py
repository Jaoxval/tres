from tres.engine import AnalysisEngine


def main():
    print("Tres v0.1")
    print("Identity Intelligence Engine")
    print()

    engine = AnalysisEngine()

    findings = engine.collect("joao@gmail.com")

    for finding in findings:
        print(
            f"[{finding.source}] "
            f"{finding.key}: {finding.value}"
        )


if __name__ == "__main__":
    main()