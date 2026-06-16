# Patch Demo Project

This is a tiny buggy project used to demonstrate a Patch / Worktree-style Tree of Loops workflow.

The task is to fix `normalize_title(text)`.

Expected behavior:

* trim leading and trailing whitespace
* collapse repeated spaces, tabs, and newlines into a single space
* convert the result into title case

Later, the evaluator will:

1. copy this project into isolated temporary workspaces
2. apply different candidate patches
3. run the same tests for each patch
4. rank the candidate patches
5. recommend one patch
