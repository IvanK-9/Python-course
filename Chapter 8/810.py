def send_messages(messages, sent_messages):
    """Prints each message and moves it to the sent_messages list."""
    while messages:  # Continue while there are messages in the list
        current_message = messages.pop()  # Remove the last message
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)  # Add to sent list


# Initial list of messages
unread_messages = [
    "Hi! How are you?",
    "Meeting scheduled for 10:00 tomorrow",
    "Don't forget the report",
    "Have a great day!"
]

# Empty list to store sent messages
sent_messages = []


# Call the function
send_messages(unread_messages, sent_messages)


# Print both lists to confirm the move
print("\n--- Verification ---")
print("Unread messages (should be empty):", unread_messages)
print("Sent messages (should contain all):", sent_messages)
