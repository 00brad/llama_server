from fastapi import FastAPI, HTTPException, Request
from openai import OpenAI
from llama_cpp.llama import Llama
import json

app = FastAPI()

client = OpenAI(
    api_key="none"
)

llm = Llama("llama-2-7b.Q8_0.gguf")


@app.post("/chat/completions")
async def chat_completions(request: Request) -> str:
    response_data = await request.json()
    message = response_data['messages'][0]['content']

    try:
        response = llm(
            prompt=message.strip(),
            max_tokens=-1
        )
        print(response)
        return json.dumps(response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
