def send_messages(messages, sent_messages):
    """As defined in Exercise 8‑10."""
    while messages:
        current_message = messages.pop()
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)


# Original list of messages (to be preserved)
original_messages = [
    "Hi! How are you?",
    "Meeting scheduled for 10:00 tomorrow",
    "Don't forget the report",
    "Have a great day!"
]

# List to collect sent messages
sent_messages = []

# Pass a copy of the original list, not the original itself
send_messages(original_messages.copy(), sent_messages)


# Print both lists
print("\n--- Verification ---")
print("Original messages (should remain unchanged):", original_messages)
print("Sent messages (should contain all):", sent_messages)
