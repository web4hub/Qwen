#!/usr/bin/env python3
"""Extract lightweight metadata from a Qwen4 checkpoint repository.

This tool reads local JSON metadata only. It never loads model weights,
so it is safe to run against large sharded checkpoints.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def extract(root: Path) -> dict[str, Any]:
    config = load_json(root / "config.json")
    text = config.get("text_config", config)

    rope = text.get("rope_parameters", {})
    layers = text.get("layer_types", [])

    return {
        "architecture": config.get("architectures", []),
        "model_type": config.get("model_type"),
        "hidden_size": text.get("hidden_size"),
        "num_hidden_layers": text.get("num_hidden_layers"),
        "num_experts": text.get("num_experts"),
        "num_experts_per_tok": text.get("num_experts_per_tok"),
        "vocab_size": text.get("vocab_size"),
        "native_context": rope.get("original_max_position_embeddings"),
        "max_position_embeddings": text.get("max_position_embeddings"),
        "yarn_factor": rope.get("factor"),
        "mtp_num_hidden_layers": text.get("mtp_num_hidden_layers"),
        "vision_config": "vision_config" in config,
        "layer_types": layers,
        "safetensor_shards": len(list(root.glob("*.safetensors"))),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path("."),
        help="checkpoint directory containing config.json",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit machine-readable JSON",
    )
    args = parser.parse_args()

    data = extract(args.root.resolve())

    if args.json:
        print(json.dumps(data, indent=2, sort_keys=True))
        return 0

    for key, value in data.items():
        if key == "layer_types":
            print(f"{key}: {len(value)} layers")
        else:
            print(f"{key}: {value}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
