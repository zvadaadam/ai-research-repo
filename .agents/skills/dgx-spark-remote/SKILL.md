---
name: dgx-spark-remote
description: Remote CUDA development workflow for the local NVIDIA DGX Spark at spark-f0a3.local. Use when Codex needs to probe the DGX Spark, choose a developer experience, mirror a research workspace with rsync, run CUDA/PyTorch/NAC/Le-WM training remotely while the agent stays on the Mac, use tmux/screen, manage TensorBoard tunnels, sync artifacts back, or decide between direct SSH, Docker, NVIDIA AI Workbench, and native Python setup.
---

# DGX Spark Remote

## Operating Model

Keep the Mac workspace as the source of truth. Treat the DGX Spark as a remote
compute worker.

```text
Mac Codex workspace
  -> rsync selected code/data/checkpoints
  -> ssh spark-f0a3.local
  -> run training in tmux/screen on DGX
  -> stream logs/TensorBoard
  -> rsync summaries/checkpoints back
```

Default device facts from the first probe:

- Host: `spark-f0a3.local`
- SSH user: `zvada`
- OS: Ubuntu Linux `aarch64`
- GPU: `NVIDIA GB10`, driver `580.142`, CUDA driver API `13.0`
- RAM: about `121 GiB`
- Free disk: about `3.3 TiB`
- Docker and NVIDIA container runtime are installed.
- NVIDIA AI Workbench CLI exists at `~/.nvwb/bin/nvwb-cli`.
- Bare `/usr/bin/python3` is Python `3.12.3` and does not have `torch`.

Use `spark-f0a3.local`, not plain `spark-f0a3`, unless SSH config has been
fixed. Plain `spark-f0a3` may select the wrong local username.

## First Probe

Before setup or training, run the read-only probe:

```bash
.agents/skills/dgx-spark-remote/scripts/probe_dgx.sh
```

Confirm:

- SSH works without password prompts.
- `nvidia-smi` sees `NVIDIA GB10`.
- Docker is available.
- There is enough disk and memory.
- A Python/CUDA environment already exists or must be created.

Do not install packages, pull Docker images, or copy large datasets during the
probe.

## Developer Experience Choice

Prefer this order:

1. **Direct SSH + rsync + tmux** for fastest research iteration and smallest
   moving parts.
2. **Docker/NVIDIA container** for reproducible CUDA/PyTorch training once a
   compatible `aarch64` image is chosen.
3. **NVIDIA AI Workbench** when the user wants the DGX Dashboard/app workflow
   or project-level Workbench synchronization.
4. **Native Python venv** only when required packages have compatible
   `aarch64` wheels or are known to build cleanly.

For NAC/Le-WM research, direct SSH plus a container is usually the best route:
the agent stays local, training survives disconnects in tmux, and the repo
notebook remains on the Mac.

## Workspace Mirror

Use a remote mirror path:

```bash
REMOTE=spark-f0a3.local
REMOTE_DIR=/home/zvada/ai-research/ai-research-repo
```

Sync code separately from bulky artifacts:

```bash
.agents/skills/dgx-spark-remote/scripts/sync_dgx_workspace.sh code
```

Then sync only required training inputs, for example:

```bash
rsync -az --mkpath src/nac/data/robomimic/mt4_N800.zarr/ \
  spark-f0a3.local:/home/zvada/ai-research/ai-research-repo/src/nac/data/robomimic/mt4_N800.zarr/

rsync -az --mkpath artifacts/E057/run_001_mt4_nactok_continue_25000/checkpoints/latest.ckpt \
  spark-f0a3.local:/home/zvada/ai-research/ai-research-repo/artifacts/E057/run_001_mt4_nactok_continue_25000/checkpoints/latest.ckpt
```

Do not use `--delete` on broad artifact directories. Use `--delete` only for
the code mirror, where bulky/generated paths are excluded.

## Remote Training Pattern

Run jobs in a remote terminal multiplexer:

```bash
ssh spark-f0a3.local
cd /home/zvada/ai-research/ai-research-repo
tmux new -s e091
```

Record exact commands in the experiment run record before or immediately after
launching. Prefer writing logs to:

```text
artifacts/<EXPERIMENT>/<run-name>/launch.log
artifacts/<EXPERIMENT>/<run-name>/logs.json
artifacts/<EXPERIMENT>/<run-name>/exit_code.txt
```

## TensorBoard

Run TensorBoard remotely and tunnel it back:

```bash
ssh -L 6007:127.0.0.1:6006 spark-f0a3.local
```

Then open:

```text
http://127.0.0.1:6007
```

If a local TensorBoard is already using `6006`, use `6007` or another local
port.

## Sync Results Back

Copy back only durable evidence, summaries, logs, and selected checkpoints:

```bash
.agents/skills/dgx-spark-remote/scripts/sync_dgx_workspace.sh results E091
```

After syncing results, update the local research workspace files and run:

```bash
python3 tools/validate_research_workspace.py .
```

## Installation Discipline

Treat installation as a separate, explicit mutation. Before installing on the
DGX, report:

- chosen setup route: Docker, Workbench, or native venv;
- disk cost and expected install time;
- whether the image/env supports Linux `aarch64`;
- a one-step CUDA/PyTorch smoke command;
- rollback or cleanup command.

`nvcr.io/nvidia/pytorch:25.06-py3` was checked with `docker manifest inspect`
and advertises both `linux/amd64` and `linux/arm64`, so it is the first
candidate image for this DGX Spark.

For Docker, verify GPU access inside the container before NAC setup. Use the
guarded smoke script:

```bash
.agents/skills/dgx-spark-remote/scripts/docker_torch_smoke.sh
```

If the image is not already present, the script exits before pulling. To allow
the large pull explicitly:

```bash
CONFIRM_PULL=1 .agents/skills/dgx-spark-remote/scripts/docker_torch_smoke.sh
```

Equivalent manual command:

```bash
docker run --rm --gpus all nvcr.io/nvidia/pytorch:25.06-py3 \
  python - <<'PY'
import torch
print(torch.__version__)
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else None)
PY
```

Do not start a long training run until a small import/data/checkpoint/training
smoke passes.

## Smoke Before Real Training

For NAC/E091-like work, the first remote CUDA smoke should prove:

1. `torch.cuda.is_available()` is true.
2. The repo imports.
3. The RoboMimic mt4 zarr loads.
4. The E057 tokenizer checkpoint loads.
5. A one-step or very short NAC policy command writes logs and exits.

Only after that should the agent launch default-scale training.
