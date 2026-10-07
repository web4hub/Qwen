chat_response = client.chat.completions.create(
    model="Qwen4/Qwen3.8-Flash-Next",
    messages=[{"role": "user", "content": "Explain quantum computing in one sentence."}],
    temperature=0.7,
    top_p=0.8,
    presence_penalty=1.5,
    extra_body={
        "top_k": 20,
        "chat_template_kwargs": {"enable_thinking": False},
    },
)
print(chat_response.choices[0].message.content)
