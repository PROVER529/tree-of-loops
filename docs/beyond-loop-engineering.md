# Beyond Loop Engineering: The Tree of Loops

This is not a prediction about the distant future of AI.

It is a narrower claim about coding agents.

Today’s coding agents are mostly loop-based. They observe the repository, form a plan, edit files, run tests, observe the result, and repeat. This is already a meaningful abstraction shift. The human no longer writes every line or even every step. The human gives the system a goal, and the agent spends time trying to reach it.

But a loop has a structural limitation.

It is still one path through the solution space.

A loop can be long, careful, and reflective. It can retry after failure. It can inspect logs, rewrite code, and run tests again. But unless it explicitly branches, it is still making a sequence of local decisions. Early assumptions tend to compound. A bad first framing can lead to a long and competent search in the wrong direction.

This is especially visible in coding.

For any non-trivial bug or feature, there are usually several plausible approaches: a minimal patch, a test-first fix, a local refactor, a deeper architectural change, a compatibility-preserving version, or a performance-oriented rewrite. A human engineer often considers these possibilities informally before choosing one. A loop-based agent usually chooses one path and proceeds.

If inference becomes cheaper, the natural next step is not to make the loop merely longer. It is to run multiple loops.

The next paradigm after Loop Engineering is **Branch/Search Engineering**: turning a single agent loop into a tree of isolated, testable candidate loops.

In this model, one task produces several candidate branches. Each branch runs its own agent loop in an isolated worktree or sandbox. One branch tries the minimal patch. Another writes a regression test first. Another attempts a refactor. Another optimizes for performance or safety. These branches are then evaluated against external criteria: tests, type checks, linting, benchmarks, diff size, API compatibility, security scans, and human review.

The important change is not that the model becomes more “creative.” The important change is that the system stops committing to a single trajectory too early.

Loop Engineering gives the agent time.

Branch/Search Engineering gives it alternatives.

This distinction matters because the bottleneck in coding agents is shifting. Code generation is becoming cheaper. The harder problem is evaluation: deciding which patch is actually better, which refactor is worth the complexity, which passing test suite is misleading, and which small change will be easier for future engineers to understand.

In other words, the next generation of coding agents will not just be better at writing code. They will be embedded in systems that can generate, isolate, compare, and select among multiple possible changes.

The engineer’s role changes accordingly.

In a loop-based system, the human mostly gives the goal and watches the agent work. In a branch/search-based system, the human defines the search space and the evaluation function: which files may be touched, which constraints are non-negotiable, which metrics matter, which tradeoffs are acceptable, and when human approval is required.

This is a more powerful abstraction, but also a more dangerous one. If the evaluation function is weak, the system will learn to produce patches that look good rather than patches that are good. It may overfit to visible tests, avoid necessary refactors, or prefer small diffs even when the architecture needs deeper repair.

So the core skill does not disappear. It moves upward.

The future coding engineer may write less code directly, but will need to become much better at specifying what counts as a good change.

The next step after a loop is not a longer loop.

It is a tree of loops.

## The pattern

Loop Engineering:

```text
one task
→ one agent loop
→ one final patch
```

Branch/Search Engineering:

```text
one task
→ multiple candidate loops
→ isolated branches
→ external evaluation
→ selected patch
```

## What has to exist for this to work

A tree of loops needs more than a model. It needs a harness around the model:

1. **Candidate generation**  
   The system must deliberately create different approaches rather than small variations of the same idea.

2. **Isolation**  
   Each candidate should run in a separate branch, worktree, container, or sandbox.

3. **External evaluation**  
   The candidates must be judged by tests, type checks, linting, benchmarks, security scans, diff review, and human judgment.

4. **Comparison**  
   The system should explain the tradeoffs between candidates, not just select the one with the highest score.

5. **Memory**  
   Failed paths should be recorded. A rejected approach is still useful information.

## Why this is not Evolution Engineering yet

Evolution Engineering would mean improving the agent system itself over many tasks and many generations: its skills, prompts, tools, planner, reviewer, memory policy, and evaluation rules.

That may come later.

But the direct successor to Loop Engineering is simpler and more immediate:

```text
branch → run → evaluate → select
```

It is not yet about evolving the agent.

It is about refusing to let one early path dominate the search.

## Final claim

The next useful abstraction in AI coding agents is not autonomous magic.

It is a controlled search system:

```text
multiple isolated loops
+ external evaluation
+ human-defined constraints
+ explicit tradeoff comparison
```

A better coding agent is not merely an agent that loops longer.

It is a system that knows when to branch.
