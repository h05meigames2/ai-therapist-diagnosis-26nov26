#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun entry.

Writes one funny single-line diagnosis, at most 200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Deterministic, stdlib only, no network, no randomness.
"""

import os

DIAGNOSIS = (
    "Diagnosis: acute imposter syndrome, complicated by the fact that "
    "you Googled your symptoms and diagnosed me instead."
)


def main() -> None:
    assert 1 <= len(DIAGNOSIS) <= 200, "diagnosis must be 1-200 characters"
    assert "\n" not in DIAGNOSIS, "diagnosis must be a single line"
    assert DIAGNOSIS.startswith("Diagnosis:"), "line must be a diagnosis"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(DIAGNOSIS + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
