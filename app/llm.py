from ollama import chat

def generate_response(messages):

    stream = chat(
        model = "qwen2.5:7b-instruct",
        messages = messages,
        stream = True,
    )

    reply = ""
    print("Assistant: ", end="")

    for chunk in stream:
        content = chunk.message.content
        reply += content
        print(content, end="", flush=True)

    print('\n')

    return reply
    