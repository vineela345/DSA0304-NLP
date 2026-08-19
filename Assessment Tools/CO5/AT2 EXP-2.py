text = [
    "The roads were flooded after heavy rainfall.",
    "Therefore, schools were closed for the day.",
    "Students attended classes online."
]

relations = [
    ("S1", "S2", "Cause-Effect"),
    ("S2", "S3", "Sequence")
]

print("Discourse:")
for i, sentence in enumerate(text, 1):
    print(f"S{i}: {sentence}")

print("\nDiscourse Relations:")
for relation in relations:
    print(f"{relation[0]} -> {relation[1]} : {relation[2]}")

print("\nDiscourse Structure:")
print("S1")
print("  |")
print("  | Cause-Effect")
print("  v")
print("S2")
print("  |")
print("  | Sequence")
print("  v")
print("S3")

print("\nCoherence Explanation:")
print("S1 provides the cause of the school closure in S2.")
print("The word 'Therefore' explicitly indicates a cause-effect relationship.")
print("S3 follows S2 logically because online classes occur after schools are closed.")
print("These relationships connect the sentences and maintain a logical flow.")
