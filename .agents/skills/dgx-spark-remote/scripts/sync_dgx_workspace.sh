#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-}"
EXPERIMENT="${2:-}"
REMOTE="${REMOTE:-spark-f0a3.local}"
REMOTE_DIR="${REMOTE_DIR:-/home/zvada/ai-research/ai-research-repo}"
LOCAL_DIR="${LOCAL_DIR:-$(pwd)}"

usage() {
  cat <<EOF
Usage:
  $0 code
  $0 results <EXPERIMENT_ID>

Environment:
  REMOTE=${REMOTE}
  REMOTE_DIR=${REMOTE_DIR}
  LOCAL_DIR=${LOCAL_DIR}
EOF
}

case "${MODE}" in
  code)
    ssh "${REMOTE}" "mkdir -p '${REMOTE_DIR}'"
    rsync -az --delete \
      --exclude='.git/' \
      --exclude='.venv/' \
      --exclude='.venv*/' \
      --exclude='src/nac/.git/' \
      --exclude='src/nac/.venv/' \
      --exclude='__pycache__/' \
      --exclude='.pytest_cache/' \
      --exclude='.mypy_cache/' \
      --exclude='artifacts/' \
      --exclude='data/' \
      --exclude='src/nac/data/' \
      --exclude='runs/' \
      --exclude='wandb/' \
      --exclude='checkpoints/' \
      --exclude='*.pyc' \
      "${LOCAL_DIR%/}/" "${REMOTE}:${REMOTE_DIR}/"
    ;;
  results)
    if [[ -z "${EXPERIMENT}" ]]; then
      usage >&2
      exit 2
    fi
    mkdir -p "${LOCAL_DIR%/}/artifacts/${EXPERIMENT}"
    rsync -az \
      "${REMOTE}:${REMOTE_DIR}/artifacts/${EXPERIMENT}/" \
      "${LOCAL_DIR%/}/artifacts/${EXPERIMENT}/"
    ;;
  *)
    usage >&2
    exit 2
    ;;
esac
