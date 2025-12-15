def show_messages(messages):
    """Prints each text message from the provided list."""
    for message in messages:
        print(message)

# Create a list of text messages
text_messages = [
    "Hi! How are you?",
    "Meeting scheduled for 10:00 tomorrow",
    "Don't forget the report",
    "Have a great day!"
]

# Call the function to display messages
show_messages(text_messages)
