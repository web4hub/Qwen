from openai import OpenAI

# Initialize the client (Make sure your environment variables are set)
client = OpenAI()

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://aliyuncs.com"
                }
            },
            {
                "type": "text",
                "text": "Analyze this geometric chart step-by-step and provide the calculations."
            }
        ]
    }
]

chat_response = client.chat.completions.create(
    model="Qwen4/Qwen3.8-Flash-Next",
    messages=messages,
    temperature=0.7,
    top_p=0.8,
    extra_body={
        "chat_template_kwargs": {"enable_thinking": False} # Direct answer mode
    }
)

print("Chat response:", chat_response.choices[0].message.content)
