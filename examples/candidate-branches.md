# Example: Candidate Branches

Suppose a coding agent is asked to fix a flaky authentication test.

A loop-based agent may choose one path:

```text
inspect failing test → edit auth/session.ts → rerun test → fix again
```

A Branch/Search system creates several candidate loops:

| Candidate | Strategy | Risk |
|---|---|---|
| A | Minimal patch to timing logic | May hide deeper race condition |
| B | Add regression test first | Slower but safer |
| C | Refactor session state machine | Larger diff, higher long-term upside |
| D | Add retry behavior | May mask real bug |
| E | Improve test isolation | Could fix test but not production issue |

Each candidate runs independently.

Then the system evaluates:

```text
tests pass?
typecheck pass?
lint pass?
benchmark unchanged?
diff small enough?
public API unchanged?
reviewer agent approves?
human approves?
```

The final output is not just a patch.

It is a comparison report:

```text
Candidate B is recommended.

Why:
- It adds a regression test that fails before the fix.
- It changes only the session boundary condition.
- It does not alter public API behavior.
- It avoids the broader refactor risk in Candidate C.

Rejected:
- Candidate A passed tests but did not explain the root cause.
- Candidate D introduced retry behavior that may hide production failures.
- Candidate C may be worth a separate refactor PR, but is too large for this bug fix.
```
