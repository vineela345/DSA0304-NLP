from nltk import CFG
from nltk.parse import RecursiveDescentParser, EarleyChartParser

grammar = CFG.fromstring("""
S -> VP
VP -> V NP PP
NP -> Det N
NP -> Det N PP
NP -> ProperNoun
PP -> P NP
V -> "book"
Det -> "a"
N -> "flight" | "seat"
ProperNoun -> "Delhi"
P -> "to" | "with"
""")

sentence = "book a flight to Delhi with a seat".split()

print("VOICE ASSISTANT PARSING")
print("-" * 50)

print("Input:", " ".join(sentence))

print("\nTOP-DOWN PARSING")
parser1 = RecursiveDescentParser(grammar)

try:
    count = 0
    for tree in parser1.parse(sentence):
        count += 1
        print("\nParse", count)
        print(tree)
        if count == 2:
            break
    print("\nTop-down parsing uses backtracking when a rule fails.")
except Exception as e:
    print("Parsing problem:", e)

print("\nEARLEY PARSING")
parser2 = EarleyChartParser(grammar)

count = 0

for tree in parser2.parse(sentence):
    count += 1
    print("\nParse", count)
    print(tree)
    if count == 2:
        break

print("\nAMBIGUITY ANALYSIS")
print("'with a seat' can be attached to the flight")
print("or interpreted as an additional booking condition.")

print("\nTOP-DOWN LIMITATIONS")
print("1. Backtracking can increase processing time.")
print("2. Difficult to handle incomplete speech.")
print("3. Ambiguous inputs can create many alternatives.")
print("4. Not ideal for long real-time commands.")

print("\nEARLEY ADVANTAGES")
print("1. Handles ambiguous grammars.")
print("2. Uses dynamic programming.")
print("3. Avoids repeated parsing work.")
print("4. Can process partial input.")
print("5. Suitable for conversational systems.")

print("\nPERFORMANCE COMPARISON")
print("Top-Down: Simple but may require extensive backtracking.")
print("Earley: More robust for ambiguous and incomplete commands.")
print("Industry choice: Earley parsing is preferable for complex voice input.")
