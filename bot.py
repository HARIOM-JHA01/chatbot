from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the English corpus
trainer.train("chatterbot.corpus.english")

# Train based on English greetings corpus
trainer.train("chatterbot.corpus.english.greetings")

# Train based on the English conversations corpus
trainer.train("chatterbot.corpus.english.conversations")

# Define exit commands
exit_commands = ("bye", "quit", "exit")

# Start the conversation loop
while True:
    # Get user input
    user_input = input("You: ")

    # Check if user wants to exit
    if user_input.lower() in exit_commands:
        print("Chatbot: Goodbye!")
        break

    # Get chatbot response
    response = chatbot.get_response(user_input)
    print("Chatbot:", response)
