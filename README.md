# Tree of Loops

> The next step after Loop Engineering is not a longer loop.  
> It is a tree of loops.

This repository is a small conceptual project about the next engineering layer after loop-based coding agents.

It is not a prediction about AGI.  
It is not a claim that coding agents should be fully autonomous.  
It is a narrower argument:

**Loop Engineering made coding agents useful by giving them time. Branch/Search Engineering makes them stronger by giving them alternatives.**

Today, many coding agents operate as a loop:

```text
observe → plan → act → test → observe
```

This is powerful, but it is still a single path through the solution space.  
A loop can retry, reflect, and repair, but it often commits to early assumptions too soon.

The natural successor is to run multiple isolated loops in parallel:

```text
task
├── loop A: minimal patch
├── loop B: test-first patch
├── loop C: refactor patch
├── loop D: performance-first patch
└── loop E: safety-first patch
        ↓
external evaluation
        ↓
selected candidate
```

The core shift is from:

```text
one task → one loop → one patch
```

to:

```text
one task → many candidate loops → external evaluation → selected patch
```

## Why coding is the right domain

Coding has properties that make Branch/Search Engineering practical:

- code can be copied
- branches can be isolated
- worktrees can run independently
- tests can provide external feedback
- diffs can be compared
- failed paths can be discarded
- selected patches can be reviewed before merge

This makes coding one of the first domains where a "tree of loops" can become a real engineering pattern rather than a metaphor.

## Repository structure

```text
.
├── README.md
├── docs/
│   └── beyond-loop-engineering.md
├── architecture/
│   └── tree-of-loops.md
├── examples/
│   └── candidate-branches.md
├── configs/
│   └── evaluation-rubric.yaml
├── scripts/
│   └── create_candidate_worktrees.sh
└── .github/
    └── workflows/
        └── validate-docs.yml
```

## Core idea

Loop Engineering gives an agent time.  
Branch/Search Engineering gives it alternatives.

The bottleneck shifts from generation to evaluation.

The future coding engineer may write less code directly, but will need to become better at defining:

- the search space
- the constraints
- the evaluation function
- the acceptable tradeoffs
- the approval gates

## Suggested title for an essay or post

**Beyond Loop Engineering: The Tree of Loops**

## License

MIT
