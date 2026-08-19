sentence = "She saw the man with a telescope"

print("Sentence:")
print(sentence)

print("\nCFG Parsing:")
print("Interpretation 1:")
print("She used the telescope to see the man.")

print("Interpretation 2:")
print("The man had the telescope.")

print("\nCFG Result:")
print("Both interpretations are possible.")

print("\nPCFG Parsing:")

interpretation1 = 0.70
interpretation2 = 0.30

print("Interpretation 1 probability:", interpretation1)
print("Interpretation 2 probability:", interpretation2)

if interpretation1 > interpretation2:
    print("Selected interpretation:")
    print("She used the telescope to see the man.")
else:
    print("Selected interpretation:")
    print("The man had the telescope.")

print("\nNeural Parsing:")

words = sentence.split()

for i, word in enumerate(words):
    print(i + 1, "->", word)

print("\nNeural parser uses contextual information")
print("to select the most likely dependency structure.")

print("\nComparison:")
print("CFG  -> Generates possible parse structures.")
print("PCFG -> Assigns probabilities to parse structures.")
print("Neural -> Uses learned contextual information.")

print("\nConclusion:")
print("Neural parsing is generally more effective for real-world NLP applications.")
