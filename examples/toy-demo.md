# Toy Demo

This toy demo shows the smallest possible version of a Tree of Loops workflow.

It does not run real agents yet.
It only creates candidate folders that represent isolated candidate loops.

## Run

From the repository root, first generate candidate folders:

```bash
python scripts/generate_demo_candidates.py
```

Then run the evaluator:

```bash
python scripts/evaluate_demo_candidates.py
```

## Output

The script creates:

```text
demo_runs/
├── candidate_a_minimal_patch/
├── candidate_b_test_first/
├── candidate_c_refactor/
└── candidate_d_safety_first/
```

Each folder contains a small `README.md` describing the candidate strategy.

## Why this matters

This demo turns the idea from a pure concept into a visible workflow:

```text
one task
→ multiple candidate folders
→ different strategies
→ later evaluation
→ selected candidate
```

The next step is to add a simple evaluator that scores each candidate.
