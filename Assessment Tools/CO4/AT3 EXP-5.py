sentence = ["She", "eats", "an", "apple"]

print("Sentence:")
print(" ".join(sentence))

print("\nTransition-Based Parsing:")

stack = ["ROOT"]
buffer = sentence.copy()
dependencies = []

while buffer:
    word = buffer.pop(0)

    if stack[-1] == "ROOT":
        head = word
    else:
        head = stack[-1]

    dependencies.append((head, word))
    stack.append(word)

for head, dependent in dependencies:
    print(head, "->", dependent)

print("\nGraph-Based Parsing:")

graph = [
    ("eats", "She"),
    ("eats", "apple"),
    ("apple", "an")
]

for head, dependent in graph:
    print(head, "->", dependent)

print("\nComparison:")

print("\nTransition-Based:")
print("1. Makes decisions step by step.")
print("2. Uses local information.")
print("3. Faster for large datasets.")
print("4. Requires less computation.")

print("\nGraph-Based:")
print("1. Considers multiple possible structures.")
print("2. Makes global decisions.")
print("3. Can provide better global accuracy.")
print("4. Requires more computation.")

print("\nConclusion:")
print("Transition-based parsing is more suitable for large-scale applications")
print("when speed and efficiency are important.")
