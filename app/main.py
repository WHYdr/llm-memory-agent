from llm import generate_response

messages = []

# to build a chat loop
while True:

    userinput = input("User: ")
    if userinput == "exit":
        break

    messages.append({'role': "user", 'content': userinput})

    reply = generate_response(messages)
    
    messages.append({'role': "assistant", 'content': reply})
