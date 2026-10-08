## 🛠️ Key Architectural Highlights

* Hybrid Attention with QSA: Combines Gated DeltaNet with Qwen Sparse Attention (QSA). QSA works at a micro-block level instead of individual tokens, massively dropping long-context latency for agent workloads.
* Gated Residuals: Uses read/write gates over widened residual streams to fine-tune layer expressiveness while keeping inference lightweight and training stable.
* N-gram Embedding: Adds a unique parameter scaling axis by indexing with short n-grams (bigrams/trigrams at layer 2), making scaling highly efficient for memory-constrained hardware.
* Tailored Training: Uses Muon and AdamW optimizers across specific weight classes and skips traditional batch-size warmups to drastically cut down total training steps.

## 📊 Model Overview & Specifications

* Total Parameters: 125B total with 6B activated per token.
* Additional Weights: Contains a 51B n-gram embedding and 4B Multi-Token Prediction (MTP) capacity.
* Layers: 48 layers organized into a layout of 12 blocks (each featuring 3 Gated DeltaNet → MoE steps and 1 QSA → MoE step).
* Mixture of Experts (MoE): 512 total experts, routing 10 active experts + 1 shared expert per token.
* Native Context Length: 262,144 tokens natively, stretchable to 1 Million tokens using YaRN scaling.

## 💡 Quickstart & API Behavior
By default, the model operates in Thinking Mode. It generates hidden reasoning traces enclosed in <think>...</think> blocks before printing out its final response.

* To keep Thinking Mode enabled (Default): Use higher sampling parameters (e.g., temperature=1.0, top_p=0.95).
* To bypass Thinking Mode: Set "enable_thinking": False in your API extra_body payload and adjust parameters downward (e.g., temperature=0.7, top_p=0.80).
* Preserved Thinking: The model keeps thinking blocks from previous conversational turns by default to maintain decision consistency in complex multi-turn agent tasks. This can be turned off by passing "preserve_thinking": False.



