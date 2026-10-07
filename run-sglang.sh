#!/bin/bash
docker run --rm --gpus all --ipc=host \
  -p 30000:30000 \
  lmsysorg/sglang:latest \
  sglang serve MODEL_PATH --host 0.0.0.0 --port 30000
pip install -U openai

# Set the following accordingly
export OPENAI_BASE_URL="http://localhost:8000/v1"
export OPENAI_API_KEY="EMPTY"
