# FAQ

## Is this Evolution Engineering?

Not yet.

This project argues that the direct successor to Loop Engineering is Branch/Search Engineering.

Evolution Engineering would come later, when the system starts improving its own harness, skills, tools, planner, reviewer, memory policy, and evaluation rules across many tasks.

This project focuses on the immediate next step:

```text
one loop → a tree of loops
```

## Is this a working agent framework?

Not yet.

The current version is a conceptual scaffold. It explains the idea, architecture, evaluation rubric, and example workflow.

The next milestone is a toy demo that simulates candidate branches and produces a comparison report.

## What problem does this solve?

Loop-based coding agents often follow one path too early.

They may choose a reasonable-looking approach, spend many steps improving it, and only later discover that a different strategy would have been better.

Branch/Search Engineering tries to reduce this by running several isolated approaches in parallel, then selecting based on external evaluation.

## What is the core idea?

The next step after Loop Engineering is not a longer loop.

It is a tree of loops.

```text
one task
→ multiple candidate loops
→ isolated branches
→ external evaluation
→ selected patch
```

## What is the human role?

The human moves from directly steering every step to defining:

* the search space
* the constraints
* the evaluation criteria
* the acceptable tradeoffs
* the approval gates

The core human skill becomes judgment.
