print("Welcome to AI Chatbot")
print("Type 'bye' to exit")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello! How can I help you?")
    elif user == "how are you":
        print("Bot: I am fine. Thank you!")
    elif user == "what is your name":
        print("Bot: My name is AI Chatbot.")
    elif user == "what is ai":
        print("Bot: AI means Artificial Intelligence.")
    elif user == "help":
        print("Bot: I can answer simple questions.")
    elif user == "thanks" or user == "thank you":
        print("Bot: You're welcome!")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")
