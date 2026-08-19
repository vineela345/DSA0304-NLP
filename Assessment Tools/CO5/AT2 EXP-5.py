source = "The boy is playing football."

interlingua = {
    "Subject": "boy",
    "Action": "play",
    "Object": "football",
    "Tense": "Present",
    "Aspect": "Progressive"
}

candidates = [
    ("The boy is playing football.", 0.95),
    ("The boy plays football.", 0.82),
    ("Boy is football playing.", 0.35)
]

best_translation = max(candidates, key=lambda x: x[1])

print("Source Sentence:")
print(source)

print("\nStep 1 - Source Analysis:")
print("Subject: The boy")
print("Verb: is playing")
print("Object: football")
print("Tense: Present")
print("Aspect: Progressive")

print("\nStep 2 - Interlingua Representation:")
for key, value in interlingua.items():
    print(f"{key}: {value}")

print("\nStep 3 - Candidate Translations:")
for sentence, score in candidates:
    print(f"{sentence} -> Score: {score}")

print("\nStep 4 - Statistical Scoring:")
print("The candidate with the highest probability score is selected.")

print("\nStep 5 - Final Translation:")
print(best_translation[0])

print("\nEvaluation:")
print("The Interlingua representation captures the meaning independently of a specific language.")
print("Statistical scoring compares possible translations and selects the most probable one.")
print("This combination reduces ambiguity and improves translation quality.")
