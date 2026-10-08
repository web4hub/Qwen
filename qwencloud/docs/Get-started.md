> ## Documentation Index
> Fetch the complete documentation index at: https://docs.qwencloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Build with QwenCloud

> AI models for text, vision, speech, and image & video generation.

{/* 核心改动区域：外层增加卡片容器，并使用垂直居中对齐 */}

<div style={{ padding: "16px 0 48px 0" }}>
  <div style={{display: "flex", flexWrap: "wrap", gap: "2rem", alignItems: "center"}}>
    <div style={{flex: "1 1 280px"}}>
      <h2 style={{marginTop: 0, fontSize: "1.5rem", fontWeight: "600", borderBottom: "none", paddingBottom: 0}}>Developer quickstart</h2>

      <p style={{color: "#4B5563", lineHeight: "1.6", marginTop: "12px", marginBottom: "24px"}}>
        Make your first API request in minutes. Seamlessly integrate with any OpenAI SDK or client.
      </p>

      [Get started →](/developer-guides/getting-started/first-api-call)
    </div>

    <div style={{flex: "2 1 420px"}}>
      ```python
      import os
      from openai import OpenAI

      client = OpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://maas.qwencloudapi.com/compatible-mode/v1"
      )
      completion = client.chat.completions.create(
        model="qwen3.8-max",
        messages=[{"role": "user", "content": "Summarize the benefits of solar energy in three bullet points."}]
      )
      print(completion.choices[0].message.content)
      ```
    </div>
  </div>
</div>

{/* 卡片区域结束 */}

## Models

Start with **qwen3.7-plus** for a balance of quality and speed. Choose the flagship **qwen3.8-max** for the hardest reasoning and coding tasks, or **qwen3.8-flash** for cost efficiency. All models share the same API — just change the `model` parameter. [Browse all models →](/developer-guides/getting-started/model-selection)

<CardGroup cols={3}>
  <Card title="qwen3.8-max" icon="Qwen" href="https://www.qwencloud.com/models/qwen3.8-max">
    Complex reasoning and coding
  </Card>

  <Card title="qwen3.7-plus" icon="Qwen" href="https://www.qwencloud.com/models/qwen3.7-plus">
    Balanced performance, speed, and cost
  </Card>

  <Card title="qwen3.8-flash" icon="Qwen" href="https://www.qwencloud.com/models/qwen3.8-flash">
    Fast and cost-effective
  </Card>
</CardGroup>

## Start building

<CardGroup cols={2}>
  <Card title="Read and generate text" icon="TextResizeOutlined" href="/developer-guides/text-generation/quickstart">
    Prompt models to generate text, summarize, translate, or write code
  </Card>

  <Card title="Understand images and video" icon="ImageInPictureOutlined" href="/developer-guides/multimodal/vision">
    Analyze images, extract text from screenshots, or reproduce designs from mockups
  </Card>

  <Card title="Generate images" icon="BrushOutlined" href="/developer-guides/image-generation/text-to-image">
    Create and edit images from text prompts with Wan and Flux models
  </Card>

  <Card title="Generate videos" icon="VideoOutlined" href="/developer-guides/video-generation/text-to-video">
    Animate images into video clips or generate videos from text descriptions
  </Card>

  <Card title="Synthesize speech" icon="MicrophoneOutlined" href="/developer-guides/speech/tts-models">
    Convert text to natural speech with built-in voices, voice cloning, or voice design
  </Card>

  <Card title="Build agentic applications" icon="ToolOutlined" href="/developer-guides/tool-calling/function-calling">
    Connect models to external tools and APIs with function calling
  </Card>

  <Card title="Tackle complex tasks with thinking" icon="BulbOutlined" href="/developer-guides/text-generation/thinking">
    Use reasoning models to solve multi-step math, logic, and coding problems
  </Card>

  <Card title="Get structured data from models" icon="CodeOutlined" href="/developer-guides/text-generation/structured-output">
    Extract JSON that conforms to a schema from any model response
  </Card>
</CardGroup>

---

[Pricing](/developer-guides/getting-started/pricing) | [API Reference](/api-reference/preparation/api-key) | [Free Quota](/resources/free-quota)
