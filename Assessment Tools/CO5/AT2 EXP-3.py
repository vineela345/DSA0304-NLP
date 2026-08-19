conversation = [
    ("User", "Can you book a train ticket for me?"),
    ("Agent", "Sure, where would you like to travel?"),
    ("User", "I want to go to Chennai."),
    ("Agent", "Your ticket has been booked.")
]

def dialogue_act(speaker, text):
    text_lower = text.lower()

    if "can you" in text_lower or "book" in text_lower and speaker == "User":
        return "Request"

    if text_lower.startswith("sure") or "where" in text_lower:
        return "Question"

    if "i want" in text_lower or "i would" in text_lower:
        return "Inform"

    if "ticket has been booked" in text_lower:
        return "Confirmation"

    return "Action"

print("Dialogue Acts:\n")

acts = []

for speaker, text in conversation:
    act = dialogue_act(speaker, text)
    acts.append(act)
    print(f"{speaker}: {text}")
    print(f"Act: {act}\n")

print("Dialogue-Act Sequence:")
print(" -> ".join(acts))

print("\nEvaluation:")
print("Request identifies the user's goal.")
print("Question collects missing information from the user.")
print("Inform provides the required destination.")
print("Confirmation indicates successful completion of the request.")
print("The sequence helps the conversational agent track user intention and task progress.")
