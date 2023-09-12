import tkinter as tk
from tkinter import scrolledtext

# Define a larger set of predefined rules and responses
rules = {
    "hello": "Hey! How can I assist you?",
    "how are you": "I don't have feelings, but thanks for asking!",
    "what's your name": "I'm a chatbot. You can call me Sino.",
    "bye|goodbye": "Goodbye!, Have a great day!",
    "what is your purpose": "I'm here to answer your questions and have conversations.",
    "who created you": "I'm a product of programming and design.",
    "what do you like": "My main goal is to assist you.",
    "how does the internet work": "The internet is a global network of interconnected computers that communicate using protocols.",
    "tell me a fun fact": "Bananas are berries, while strawberries are not.",
    "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "what's the meaning of life": "The answer to the ultimate question of life, the universe, and everything is 42.",
    "default": "I'm not sure how to respond to that.", 
    }

def send_message():
    user_message = user_input.get()
    if user_message.lower() == "exit":
        chatbox.insert(tk.END, "Sino: Goodbye!\n")
        window.after(1000, window.destroy)  # Close the window after 1 second
    else:
        chatbox.insert(tk.END, f"You: {user_message}\n")
        response = "Sino: " + generate_response(user_message)  # Generate chatbot response
        chatbox.insert(tk.END, response + "\n")
        user_input.delete(0, tk.END)

# Function to generate chatbot response (example)
def generate_response(user_input):
    
    return "I'm a chatbot response. Ask me something!"

# Create the main window
window = tk.Tk()
window.title("Sino")

# Create a scrolled text widget for the chat
chatbox = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20, bg="#007bff")
chatbox.pack()

# Create an entry widget for user input
user_input = tk.Entry(window, width=50)
user_input.pack()

# Create a colorful "Send" button
send_button = tk.Button(window, text="Send", command=send_message, bg="#28a745", fg="white")
send_button.pack()

# Start the GUI main loop
window.mainloop()







