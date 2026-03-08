import requests
from config import MODEL
from memory import load_memory, save_memory

def ask_ai(prompt):

    memory = load_memory()

    context = ""

    for m in memory:
        context += m["role"] + ":" + m["content"] + "\n"

    full_prompt = context + "User:" + prompt + "\nAssistant:"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": MODEL,
            "prompt": full_prompt,
            "stream": False
        }
    )

    answer = response.json()["response"]

    save_memory(prompt, answer)

    return answer