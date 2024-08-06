# chatbot.py

def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm a bot, so I'm always good. How about you?",
        "what is your name": "I am a simple chatbot created using Python.",
        "bye": "Goodbye! Have a nice day!",
        "":"What the fuck! type something!",
        "hi":"Hello my boi how was your day?"
    }
    
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I don't understand that.")

def main():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
