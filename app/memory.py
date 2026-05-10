import json
import os

MEMORY_FILE = "memory.json"

def save_memories(messages):
    with open(MEMORY_FILE, 'w', encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)
        



def load_memories():