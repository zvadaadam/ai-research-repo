#!/usr/bin/env bash
set -euo pipefail

REMOTE="${REMOTE:-spark-f0a3.local}"

ssh -o BatchMode=yes -o ConnectTimeout=8 "${REMOTE}" '
set -u
echo "--- identity"
whoami
hostname
pwd
uname -a
echo "--- gpu"
command -v nvidia-smi >/dev/null && nvidia-smi || echo "missing nvidia-smi"
echo "--- cuda/container tools"
command -v nvcc >/dev/null && nvcc --version || true
command -v nvidia-container-cli >/dev/null && nvidia-container-cli --version || true
command -v docker >/dev/null && docker --version || true
echo "--- python"
command -v python3 || true
python3 --version || true
python3 - <<'"'"'PY'"'"' || true
try:
    import torch
    print("torch", torch.__version__)
    print("cuda", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("device", torch.cuda.get_device_name(0))
except Exception as exc:
    print("torch_error", repr(exc))
PY
echo "--- workbench"
test -x ~/.nvwb/bin/nvwb-cli && ~/.nvwb/bin/nvwb-cli version 2>/dev/null || true
echo "--- storage"
df -h / /home 2>/dev/null || df -h /
free -h || true
echo "--- docker state"
docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Status}}" 2>&1 | sed -n "1,40p" || true
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}" 2>&1 | sed -n "1,80p" || true
'
