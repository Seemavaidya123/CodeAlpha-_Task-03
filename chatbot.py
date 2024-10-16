import nltk
import random
import string
import numpy as np

# Sample responses
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Greetings! How may I help you?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "default": ["Sorry, I didn't understand that.", "Could you please rephrase?", "I'm not sure how to respond to that."]
}

# Predefined patterns and corresponding tags
patterns = [
    (r'hi|hello|hey', 'greeting'),
    (r'bye|goodbye', 'goodbye'),
    (r'thank you|thanks', 'thanks'),
    (r'(.*)', 'default')
]

def categorize_input(user_input):
    """Categorize user input based on predefined patterns."""
    for pattern, tag in patterns:
        if nltk.re.search(pattern, user_input.lower()):
            return tag
    return 'default'

def chatbot_response(user_input):
    """Generate a response based on user input."""
    tag = categorize_input(user_input)
    return random.choice(responses[tag])

def chatbot():
    print("Chatbot: Hi! I'm here to chat. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
