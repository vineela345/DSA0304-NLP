from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> PRON | DET NOUN
VP -> VERB NP | VERB
PRON -> 'I' | 'She'
DET -> 'the' | 'a'
NOUN -> 'book' | 'movie'
VERB -> 'read' | 'watched'
""")

sentence = ["I", "read", "the"]

print("Input Sentence:")
print(" ".join(sentence))

print("\nEarley Parser:")

parser = EarleyChartParser(grammar)
trees = list(parser.parse(sentence))

if trees:
    for tree in trees:
        print(tree)
else:
    print("Incomplete sentence - no complete parse tree found.")

print("\nTop-Down Parsing:")
print("Starts from the start symbol S.")
print("Predicts grammar rules from top to bottom.")
print("Incomplete or ambiguous input can make parsing difficult.")

print("\nComparison:")
print("Top-Down Parser -> Simple but less flexible.")
print("Earley Parser   -> Handles ambiguity and incomplete input better.")

print("\nConclusion:")
print("Earley parsing is more suitable for dynamic input conditions.")
