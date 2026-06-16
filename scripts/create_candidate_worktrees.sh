#!/usr/bin/env bash
set -euo pipefail

# create_candidate_worktrees.sh
#
# This is a small helper script for experimenting with the "tree of loops" pattern.
# It creates isolated git worktrees for candidate coding-agent paths.
#
# Usage:
#   ./scripts/create_candidate_worktrees.sh task-name
#
# Example:
#   ./scripts/create_candidate_worktrees.sh fix-auth-flake

TASK_NAME="${1:-candidate-task}"
ROOT_DIR="$(pwd)"
WORKTREE_ROOT="../${TASK_NAME}-worktrees"

mkdir -p "$WORKTREE_ROOT"

CANDIDATES=(
  "minimal-patch"
  "test-first"
  "refactor"
  "performance-first"
  "safety-first"
)

echo "Creating candidate worktrees for: $TASK_NAME"
echo "Root: $WORKTREE_ROOT"

for candidate in "${CANDIDATES[@]}"; do
  branch="candidate/${TASK_NAME}/${candidate}"
  path="${WORKTREE_ROOT}/${candidate}"

  if git rev-parse --verify "$branch" >/dev/null 2>&1; then
    echo "Branch already exists: $branch"
  else
    git branch "$branch"
  fi

  if [ -d "$path" ]; then
    echo "Worktree already exists: $path"
  else
    git worktree add "$path" "$branch"
    echo "Created: $path"
  fi
done

echo
echo "Next step:"
echo "Run a different coding-agent loop inside each worktree, then evaluate candidates externally."
