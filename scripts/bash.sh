vllm serve Qwen4/Qwen3.8-Flash-Next \
  --media-io-kwargs '{"video": {"video_backend": "opencv_dynamic", "num_frames": -1}}' \
  --mm-processor-guide '{"longest_edge": 469762048, "shortest_edge": 4096}'
