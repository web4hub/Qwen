### 1. Input → Token Embeddings

The text enters as token IDs:

```text
"Hello world"
      ↓
[tokenizer]
      ↓
[1287, 9821, ...]
      ↓
Embedding
```

Each token ID becomes a dense vector of size `hidden_size`.

Conceptually:

```text
Token IDs
   │
   ▼
Embedding Matrix
   │
   ▼
Hidden States
```

This is the initial representation that flows through the network.

---

### 2. Transformer / Hybrid Layer Stack

This is the big central part of the architecture.

Instead of necessarily making every layer identical, Qwen's newer architecture uses different sequence-processing mechanisms in different layers.

For the Qwen4 configuration we've been working with, the layer pattern is represented by:

```json
"layer_types": [
  ...
]
```

Our validated configuration has:

```text
48 total layers
├── 12 full-attention layers
└── 36 linear-attention layers
```

So conceptually:

```text
        ┌─────────────────────┐
        │      Layer 0        │
        │  Linear Attention   │
        ├─────────────────────┤
        │      Layer 1        │
        │  Linear Attention   │
        ├─────────────────────┤
        │       ...           │
        ├─────────────────────┤
        │      Full Attention │
        ├─────────────────────┤
        │       ...           │
        └─────────────────────┘
                 │
                 ▼
```

That's the key architectural idea: **use expensive global attention selectively instead of paying its full cost at every layer.**

---

### 3. Linear / Gated Sequence-Mixing Blocks

The linear-attention portion is designed to process long sequences more efficiently.

Traditional attention fundamentally involves interactions between many token pairs:

```text
Token 1 ──┬── Token 2
          ├── Token 3
          ├── Token 4
          └── ...
```

The computational burden grows substantially with sequence length.

A linear/recurrent-style sequence mixer instead maintains a compact state:

```text
token₁ → state₁
           ↓
token₂ → state₂
           ↓
token₃ → state₃
           ↓
...
```

That makes these layers particularly useful for long-context processing.

This is why the architecture is interesting alongside our **1M-token context experiment**.

---

### 4. Full Attention Blocks

The full-attention layers provide the model with explicit global token-to-token interaction.

Conceptually:

```text
        Q
        │
        ▼
      QKᵀ
        │
     Softmax
        │
        ▼
       V
        │
        ▼
 Attention Output
```

This is where RoPE/MRoPE becomes particularly important.

For our configuration:

```json
"mrope_interleaved": true,
"mrope_section": [11, 11, 10]
```

The positional representation is incorporated into the attention mechanism.

---

### 5. RoPE / MRoPE

This is the positional-information component.

Instead of simply giving every token an absolute position ID, rotary position embeddings modify the query/key representations according to position.

Simplified:

```text
Q ──┐
    ├── RoPE ──► Q'
K ──┘          K'
                 │
                 ▼
              Attention
```

For multimodal architectures, **MRoPE** extends this concept so different positional dimensions can represent different modalities/axes.

Our configuration contains:

```json
"mrope_interleaved": true,
"mrope_section": [11, 11, 10]
```

---

### 6. YaRN Long-Context Extension

This is the part we changed.

The relevant configuration is:

```json
"rope_parameters": {
  "rope_type": "yarn",
  "rope_theta": 50000000,
  "factor": 4.0,
  "original_max_position_embeddings": 262144,
  "partial_rotary_factor": 0.25,
  "mrope_interleaved": true,
  "mrope_section": [11, 11, 10]
}
```

And:

```json
"max_position_embeddings": 1048576
```

So the intended relationship is:

```text
Native context
256K
  │
  │ YaRN ×4
  ▼
1,048,576 tokens
```

That's **1M-token positional capacity**.

Important: this changes the configured positional range; it does not by itself prove that the model has been empirically validated at 1M tokens.

---

### 7. Normalization

Before/after the major computational blocks, the hidden state goes through normalization.

Conceptually:

```text
Hidden State
     │
     ▼
Normalization
     │
     ▼
Attention / Sequence Mixer
     │
     ▼
Normalization
     │
     ▼
MLP / MoE
```

Modern large language models generally use normalization heavily to keep activations numerically stable during deep computation.

---

### 8. MoE — Mixture of Experts

This is another major component.

Instead of having one enormous dense feed-forward network, the model has many experts.

Our Qwen4 configuration contains:

```text
512 experts
10 experts selected per token
```

Conceptually:

```text
                  ┌── Expert 1
                  ├── Expert 2
Token ── Router ──┼── Expert 3
                  ├── ...
                  └── Expert 512
                       │
                       ▼
                  Combine selected
                     experts
```

The router determines which experts should process each token.

So even though the model contains a huge number of parameters, each token activates only a subset.

That's the basic **sparse-MoE** idea.

---

### 9. Router

The router is effectively the traffic controller.

For a hidden vector `x`:

```text
x
│
▼
Router
│
├── Expert 37   ✓
├── Expert 108  ✓
├── Expert 214  ✓
├── ...
└── Expert 491  ✓
```

The selected expert outputs are then combined.

This gives the network conditional computation:

```text
same model
   │
   ├── token A → experts X,Y,Z
   ├── token B → experts A,C,F
   └── token C → experts M,Q,R
```

---

### 10. GELU / Feed-Forward Activation

This is where our other proposed modification comes in.

You wanted:

```json
"hidden_act": "gelu_pytorch_tanh"
```

That corresponds to PyTorch's tanh approximation of GELU:

```text
x
│
▼
GELU(tanh approximation)
│
▼
activated representation
```

Mathematically:

$$
GELU(x) \approx
\frac{x}{2}
\left[
1+\tanh
\left(
\sqrt{\frac{2}{\pi}}
(x+0.044715x^3)
\right)
\right]
$$

This is separate from RoPE/YaRN. One controls **activation**, the other controls **positional representation**.

---

### 11. Residual Connections

The architecture repeatedly uses residual paths.

Conceptually:

```text
                 ┌──────────────────┐
                 │                  │
Hidden ──────────┼──────────────┐   │
 │               │              │   │
 ▼               │              ▼   │
Norm → Block ────┘          Addition
                                │
                                ▼
                           New Hidden
```

In simplified mathematical form:

$$
x_{next}=x+F(x)
$$

This allows information to flow through many layers without every layer having to completely reconstruct the representation.

---

### 12. Repeated Hybrid Blocks

Putting the pieces together:

```text
                 ┌──────────────────────┐
                 │      Hidden State     │
                 └──────────┬───────────┘
                            │
                            ▼
                       Normalization
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
       Linear Attention             Full Attention
              │                           │
              │                         RoPE
              │                           │
              └─────────────┬─────────────┘
                            ▼
                       Residual Add
                            │
                            ▼
                         MoE Router
                            │
               ┌────────────┼────────────┐
               ▼            ▼            ▼
            Expert       Expert       Expert
               │            │            │
               └────────────┼────────────┘
                            ▼
                         Combine
                            │
                            ▼
                       GELU / FFN
                            │
                            ▼
                       Residual Add
                            │
                            ▼
                       Next Layer
```

And that repeats through the deep network.

---

### 13. Final Normalization → LM Head

After the final transformer block:

```text
Final hidden state
       │
       ▼
Final normalization
       │
       ▼
LM Head
       │
       ▼
Logits
       │
       ▼
Probability distribution
       │
       ▼
Next token
```

For example:

```text
"The capital of Nigeria is"
                       ↓
                model probabilities
                       ↓
                     Abuja
```

The generated token is appended to the sequence and the process repeats.

---

### 14. Autoregressive Generation

The complete inference loop becomes:

```text
Prompt
  │
  ▼
Tokenizer
  │
  ▼
Embeddings
  │
  ▼
┌──────────────────────────────┐
│ Hybrid Transformer           │
│                              │
│ Linear attention             │
│ Full attention + RoPE        │
│ MoE routing                  │
│ Experts                      │
│ GELU / FFN                   │
│ Residual connections         │
└──────────────┬───────────────┘
               │
               ▼
          LM Head
               │
               ▼
          Next token
               │
               └──────► repeat
```

And during generation, the KV/cache mechanism prevents recomputing everything from scratch for every generated token.

---

### The architecture mapped to our Qwen4 work

The really interesting part is how the pieces line up:

```text
Qwen architecture
│
├── Embeddings
│
├── 48-layer hybrid stack
│   ├── 36 × linear-attention
│   └── 12 × full-attention
│
├── MRoPE
│   ├── interleaved = true
│   └── sections = [11,11,10]
│
├── YaRN
│   ├── θ = 50,000,000
│   ├── factor = 4
│   ├── native = 262,144
│   └── target = 1,048,576
│
├── Sparse MoE
│   ├── 512 experts
│   └── 10 experts/token
│
├── Activation
│   └── gelu_pytorch_tanh  ← proposed change
│
└── Output
    └── autoregressive LM head
```

So the **big architectural idea** is not simply “Transformer + bigger context.” It's closer to:

**hybrid sequence modeling + selective global attention + sparse expert computation + multimodal positional encoding + long-context RoPE scaling.** 🚀

`gelu_pytorch_tanh` is the **PyTorch-compatible GELU activation** that uses the tanh approximation.

Mathematically:

$$
\operatorname{GELU}(x)
\approx
\frac{x}{2}
\left(
1+\tanh\left[
\sqrt{\frac{2}{\pi}}
\left(x+0.044715x^3\right)
\right]
\right)
$$

In PyTorch:

```python
import torch
import torch.nn.functional as F

x = torch.tensor([-2., -1., 0., 1., 2.])

y = F.gelu(x, approximate="tanh")
print(y)
```

For a Transformers model configuration, you would typically see:

```json
{
  "hidden_act": "gelu_pytorch_tanh"
}
```

This means the model uses the **tanh-approximated GELU**, rather than the exact Gaussian-error-function form.

For your **Qwen4** work, if `config.json` specifies `gelu_pytorch_tanh`, it should generally be preserved exactly rather than changed just because the RoPE/YaRN context length was upgraded. The activation and the RoPE scaling are independent model components. 🚀

