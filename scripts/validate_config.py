#!/usr/bin/env python3
"""Validate the lightweight, checked-in Qwen4 configuration metadata.

This intentionally does not download or load model shards.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
config = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
text = config["text_config"]

checks = {
    "architecture": config["architectures"] == ["Qwen4ExpForConditionalGeneration"],
    "model_type": config["model_type"] == "qwen4_exp",
    "hidden_size": text["hidden_size"] == 2560,
    "layers": text["num_hidden_layers"] == 48,
    "experts": text["num_experts"] == 512,
    "experts_per_token": text["num_experts_per_tok"] == 10,
    "vocab_size": text["vocab_size"] == 248320,
    "native_context": text["rope_parameters"]["original_max_position_embeddings"] == 262144,
    "yarn_factor": text["rope_parameters"]["factor"] == 4,
    "max_context": text["max_position_embeddings"] == 1048576,
    "vision_encoder": "vision_config" in config,
    "mtp": text["mtp_num_hidden_layers"] == 1,
    "hybrid_layers": len(text["layer_types"]) == text["num_hidden_layers"],
    "full_attention_every_4": all(
        layer == "full_attention"
        for layer in text["layer_types"][3::4]
    ),
}

failed = [name for name, ok in checks.items() if not ok]

print("Qwen4 configuration validation")
for name, ok in checks.items():
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")

print(f"Checked {len(checks)} invariants.")

if failed:
    raise SystemExit("Validation failed: " + ", ".join(failed))

print("All configuration invariants passed.")
