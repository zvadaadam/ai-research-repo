#!/usr/bin/env bash
set -euo pipefail

REMOTE="${REMOTE:-spark-f0a3.local}"
IMAGE="${IMAGE:-nvcr.io/nvidia/pytorch:25.06-py3}"
CONFIRM_PULL="${CONFIRM_PULL:-0}"

ssh -o BatchMode=yes -o ConnectTimeout=8 "${REMOTE}" "IMAGE='${IMAGE}' CONFIRM_PULL='${CONFIRM_PULL}' bash -s" <<'REMOTE_SH'
set -euo pipefail

if ! docker image inspect "${IMAGE}" >/dev/null 2>&1; then
  echo "Image not present: ${IMAGE}"
  if [[ "${CONFIRM_PULL}" != "1" ]]; then
    echo "Refusing to pull without CONFIRM_PULL=1. This image may be many GB."
    exit 3
  fi
  docker pull "${IMAGE}"
fi

docker run --rm --gpus all "${IMAGE}" python - <<'PY'
import platform
import torch

print("python", platform.python_version())
print("torch", torch.__version__)
print("cuda_available", torch.cuda.is_available())
if torch.cuda.is_available():
    print("device_count", torch.cuda.device_count())
    print("device_0", torch.cuda.get_device_name(0))
    x = torch.ones((1024, 1024), device="cuda")
    print("cuda_tensor_sum", float((x @ x).sum().item()))
PY
REMOTE_SH
