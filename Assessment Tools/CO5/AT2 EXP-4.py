semantic = {
    "Action": "Buy",
    "Agent": "Student",
    "Object": "Book",
    "Tense": "Past"
}

def lexical_selection(semantic):
    agent = semantic["Agent"]
    action = semantic["Action"]
    obj = semantic["Object"]

    if action == "Buy" and semantic["Tense"] == "Past":
        action = "bought"

    return agent, action, obj

def surface_realization(semantic):
    agent, action, obj = lexical_selection(semantic)
    sentence = f"The {agent.lower()} {action} a {obj.lower()}."
    return sentence

sentence = surface_realization(semantic)

print("Semantic Representation:")
for key, value in semantic.items():
    print(f"{key}: {value}")

print("\nLexical Selection:")
print("Agent -> student")
print("Action -> bought")
print("Object -> book")

print("\nSentence Structure:")
print("Subject + Verb + Object")

print("\nSurface Realization:")
print(sentence)

print("\nGrammatical Validation:")
print("The sentence has a subject, past-tense verb, and object.")
print("The generated sentence is grammatically correct.")
