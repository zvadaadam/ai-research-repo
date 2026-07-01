# DGX Spark Setup Options

## Direct SSH + rsync + tmux

Best default for research loops. It is transparent, easy to inspect, and does
not require adopting NVIDIA AI Workbench project structure.

Use when:

- the local repo/notebook is the source of truth;
- training commands are already shell scripts;
- artifacts must sync back into the local evidence graph.

## Docker/NVIDIA Container

Best default for CUDA/PyTorch reproducibility. The DGX Spark is Linux
`aarch64`, so verify the chosen image supports ARM before pulling/building.

Use when:

- bare Python lacks torch;
- CUDA libraries should stay isolated from the host;
- the same container can later run on larger NVIDIA machines.

Minimum acceptance:

- container starts with `--gpus all`;
- `torch.cuda.is_available()` returns true;
- repo imports and one-step training works.

## NVIDIA AI Workbench

Useful when the user wants DGX Dashboard app launching, Workbench project
management, or Workbench sync. The CLI is present at `~/.nvwb/bin/nvwb-cli`.

Use when:

- the user wants UI-backed project management;
- the project should be shared through Workbench;
- a Workbench base environment already matches the task.

Avoid for the first smoke if direct SSH can prove the CUDA path faster.

## Native Python

Use only if the package set is known to support Linux `aarch64`. Native setup
can be convenient but is easier to pollute and harder to reproduce.

For NAC, check Python version constraints before using the host Python. The
observed host Python is `3.12.3`; the Mac NAC environment used Python `3.10`.
