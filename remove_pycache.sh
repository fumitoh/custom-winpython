#!/usr/bin/env bash
set -euo pipefail

# Usage: ./clean-bytecode.sh WPy64-31020
#    or: ./clean-bytecode.sh /full/path/to/WPy64-31020

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <dir-name-or-full-path>" >&2
  exit 1
fi

BASE="${HOME}/customwinpy-work"
ARG="$1"

# If ARG looks like a path (absolute, relative, ~, Windows drive, or contains a slash/backslash),
# use it as-is; otherwise treat it as a leaf under $BASE.
case "$ARG" in
  /*|~*|.*|[A-Za-z]:*|*/*|*\\*)
    TARGET="$ARG"
    ;;
  *)
    TARGET="${BASE}/${ARG}"
    ;;
esac

if [[ ! -d "$TARGET" ]]; then
  echo "Error: directory not found: $TARGET" >&2
  exit 1
fi

cd "$TARGET"

echo "=== DRY RUN (nothing will be deleted) ==="
echo "[Dirs to remove]"
find . -type d -name '__pycache__' -prune -print

echo
echo "[Files to remove]"
find . -type f \( -name '*.pyc' -o -name '*.pyo' \) -print

echo
read -r -p "Proceed with deletion? [y/N] " reply
case "$reply" in
  [yY]|[yY][eE][sS])
    echo "Deleting..."
    # Remove __pycache__ directories (avoid descending into them)
    find . -type d -name '__pycache__' -prune -exec rm -rf {} +
    # Remove compiled Python artifacts
    find . -type f \( -name '*.pyc' -o -name '*.pyo' \) -delete
    echo "Done."
    ;;
  *)
    echo "Aborted."
    ;;
esac
