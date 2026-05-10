from ollama import chat

messages = []

while True:

    userinput = input("User: ")

    if userinput == "exit":
        break

    messages.append({'role': "user", 'content': userinput})

    stream = chat(
        model = "qwen2.5:7b-instruct",
        messages = messages,
        stream = True,
    )

    reply = ""
    print("Assistant: ", end="")
    for chunk in stream:
        reply += chunk.message.content
        print(chunk.message.content, end="", flush=True)
    print('\n\n')
    

    messages.append({'role': "assistant", 'content': reply})
