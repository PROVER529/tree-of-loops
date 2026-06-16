# Architecture: Tree of Loops

```text
Task
│
├── 1. Task Framing
│   ├── classify task type
│   ├── extract constraints
│   ├── identify risky files
│   └── define success criteria
│
├── 2. Candidate Generation
│   ├── minimal patch
│   ├── test-first patch
│   ├── refactor patch
│   ├── performance-first patch
│   ├── safety-first patch
│   └── compatibility-first patch
│
├── 3. Branch Isolation
│   ├── git worktrees
│   ├── branches
│   ├── containers
│   ├── dependency locks
│   └── sandbox permissions
│
├── 4. Parallel Agent Loops
│   ├── loop A: observe → plan → act → test
│   ├── loop B: observe → plan → act → test
│   ├── loop C: observe → plan → act → test
│   └── loop D: observe → plan → act → test
│
├── 5. Evaluation
│   ├── unit tests
│   ├── integration tests
│   ├── typecheck
│   ├── lint
│   ├── benchmark
│   ├── coverage
│   ├── security scan
│   ├── diff size
│   └── maintainability score
│
├── 6. Comparison
│   ├── rank candidates
│   ├── explain tradeoffs
│   ├── detect overfitting
│   ├── detect excessive rewrites
│   └── identify hidden risk
│
├── 7. Selection
│   ├── choose best candidate
│   ├── merge useful parts
│   ├── reject risky candidates
│   └── request human approval
│
└── 8. Memory
    ├── record failed paths
    ├── record winning strategy
    ├── save evaluation report
    └── update future search heuristics
```

## Design principle

The goal is not to make every branch succeed.

The goal is to make failure cheap enough that the system can explore more honestly.
