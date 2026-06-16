from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path("demo_runs")

SCORING_RULES = {
"Minimal patch strategy": {
"tests": 8,
"risk": 5,
"clarity": 6,
"notes": "Small patch, but root cause is not fully explained.",
},
"Test-first strategy": {
"tests": 10,
"risk": 9,
"clarity": 9,
"notes": "Adds a regression test and keeps the fix small.",
},
"Refactor strategy": {
"tests": 8,
"risk": 4,
"clarity": 7,
"notes": "Useful direction, but too large for this task.",
},
"Safety-first strategy": {
"tests": 7,
"risk": 6,
"clarity": 6,
"notes": "Safer than a blind patch, but may still hide the real issue.",
},
}

@dataclass
class CandidateResult:
name: str
strategy: str
tests: int
risk: int
clarity: int
notes: str

```
@property
def total(self) -> int:
    return self.tests + self.risk + self.clarity
```

def read_strategy(candidate_dir: Path) -> str:
readme_path = candidate_dir / "README.md"

```
if not readme_path.exists():
    return "Unknown strategy"

for line in readme_path.read_text(encoding="utf-8").splitlines():
    if line.startswith("Strategy:"):
        return line.replace("Strategy:", "").strip()

return "Unknown strategy"
```

def evaluate_candidate(candidate_dir: Path) -> CandidateResult:
strategy = read_strategy(candidate_dir)
rule = SCORING_RULES.get(
strategy,
{
"tests": 0,
"risk": 0,
"clarity": 0,
"notes": "No scoring rule found for this strategy.",
},
)

```
return CandidateResult(
    name=candidate_dir.name,
    strategy=strategy,
    tests=rule["tests"],
    risk=rule["risk"],
    clarity=rule["clarity"],
    notes=rule["notes"],
)
```

def main() -> None:
if not BASE_DIR.exists():
raise SystemExit(
"No demo_runs/ folder found. "
"Run `python scripts/generate_demo_candidates.py` first."
)

```
candidate_dirs = sorted(path for path in BASE_DIR.iterdir() if path.is_dir())

if not candidate_dirs:
    raise SystemExit(
        "No candidate folders found under demo_runs/. "
        "Run `python scripts/generate_demo_candidates.py` first."
    )

results = [evaluate_candidate(candidate_dir) for candidate_dir in candidate_dirs]
ranked = sorted(results, key=lambda result: result.total, reverse=True)

print("# Demo Candidate Evaluation\n")
print("| Candidate | Strategy | Tests | Risk | Clarity | Total | Notes |")
print("|---|---|---:|---:|---:|---:|---|")

for result in ranked:
    print(
        f"| {result.name} | {result.strategy} | {result.tests} | "
        f"{result.risk} | {result.clarity} | {result.total} | {result.notes} |"
    )

winner = ranked[0]

print("\n## Recommendation\n")
print(f"Select `{winner.name}`: {winner.strategy}.")
print(
    "This candidate has the highest score based on the current toy rubric."
)
```

if **name** == "**main**":
main()
