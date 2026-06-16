from dataclasses import dataclass


@dataclass
class Candidate:
    name: str
    strategy: str
    test_result: str
    risk: str
    score: int


CANDIDATES = [
    Candidate("A", "Minimal patch", "pass", "medium", 72),
    Candidate("B", "Test-first fix", "pass", "low", 91),
    Candidate("C", "Refactor", "pass", "high", 68),
    Candidate("D", "Safety-first patch", "pass", "medium", 80),
]


def main() -> None:
    ranked = sorted(CANDIDATES, key=lambda candidate: candidate.score, reverse=True)

    print("# Demo Candidate Evaluation\n")
    print("| Candidate | Strategy | Tests | Risk | Score |")
    print("|---|---|---|---|---|")

    for candidate in ranked:
        print(
            f"| {candidate.name} | {candidate.strategy} | "
            f"{candidate.test_result} | {candidate.risk} | {candidate.score} |"
        )

    winner = ranked[0]

    print("\n## Recommendation\n")
    print(f"Select Candidate {winner.name}: {winner.strategy}.")
    print(
        "It has the highest score after combining test result, risk, "
        "and implementation strategy."
    )


if __name__ == "__main__":
    main()
