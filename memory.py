import json
import os

FILE="memory.json"

def load_memory():

    if not os.path.exists(FILE):
        return []

    with open(FILE,"r") as f:
        return json.load(f)

def save_memory(user,assistant):

    memory = load_memory()

    memory.append({"role":"user","content":user})
    memory.append({"role":"assistant","content":assistant})

    memory = memory[-20:]

    with open(FILE,"w") as f:
        json.dump(memory,f)