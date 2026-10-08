import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: process.env.DASHSCOPE_API_KEY,
    baseURL: "https://maas.qwencloudapi.com/compatible-mode/v1"
});

async function main() {
    const response = await openai.responses.create({
        model: "qwen3.8-max",
        input: "Which is larger, 9.9 or 9.11?",
        enable_thinking: true  // Enable thinking mode
    });

    // Iterate through output items
    for (const item of response.output) {
        if (item.type === "reasoning") {
            console.log("[Reasoning]");
            for (const summary of item.summary) {
                console.log(summary.text.substring(0, 500));
            }
            console.log();
        } else if (item.type === "message") {
            console.log("[Answer]");
            console.log(item.content[0].text);
        }
    }
}

main();
