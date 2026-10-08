pip install -U openai
export OPENAI_BASE_URL="http://localhost:8000/v1"  # Or your Qwen Cloud endpoint
export OPENAI_API_KEY="your-api-key-here"

vllm serve Qwen4/Qwen3.8-Flash-Next \
  --media-io-kwargs '{"video": {"video_backend": "opencv_dynamic", "num_frames": -1}}' \
  --mm-processor-guide '{"longest_edge": 469762048, "shortest_edge": 4096}'

curl http://localhost:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MODEL_PATH",
    "messages": [
      {"role": "user", "content": "What is the capital of France?"}
    ]
  }'
man git-clone https://github.com/web4hub/Qwen4.git
cd Qwen4

python -m venv .venv
source .venv/bin/activate

pip install -U pip
pip install -U "transformers>=5.8.0.dev0" torch accelerate safetensors
python - <<'PY'
import json

with open("config.json") as f:
    c = json.load(f)

t = c["text_config"]

assert t["hidden_act"] == "gelu_pytorch_tanh"
assert t["max_position_embeddings"] == 1048576

r = t["rope_parameters"]
assert r["rope_type"] == "yarn"
assert r["rope_theta"] == 50000000
assert r["factor"] == 4.0
assert r["original_max_position_embeddings"] == 262144
assert r["partial_rotary_factor"] == 0.25
assert r["mrope_interleaved"] is True
assert r["mrope_section"] == [11, 11, 10]

assert len(t["layer_types"]) == 48

print("✅ Qwen4 config validated")
print("   GELU: gelu_pytorch_tanh")
print("   Context: 1,048,576")
print("   YaRN factor: 4x")
print("   Native context: 262,144")
print("   Layers: 48")
PY

# install doc-builder (if not done already)
pip install hf-doc-builder

# you may also need to install some extra dependencies
pip install black watchdog

# run `doc-builder preview` cmd
doc-builder preview hub {YOUR_PATH}/hub-docs/docs/hub/ --not_python_module


uv pip install sglang sglang-kernel \
  --extra-index-url https://sgl-project.github.io/whl/cu130/ \
  --extra-index-url https://download.pytorch.org/whl/cu130 \
  --index-strategy unsafe-best-match

curl -X GET \
     "https://datasets-server.huggingface.co/rows?dataset=openai%2Fgsm8k&config=main&split=train&offset=0&length=100"
     curl -X GET \
     "https://datasets-server.huggingface.co/splits?dataset=openai%2Fgsm8k"
     curl -X GET \
     "https://huggingface.co/api/datasets/openai/gsm8k/parquet/main/train"
