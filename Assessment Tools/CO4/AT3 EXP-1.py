from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> PRP | DET NOUN | DET NOUN PP
VP -> VERB NP | VERB NP PP
PP -> PREP NP
PRP -> 'She'
DET -> 'the' | 'a'
NOUN -> 'man' | 'telescope'
VERB -> 'saw'
PREP -> 'with'
""")

parser = ChartParser(grammar)

sentence = "She saw the man with a telescope".split()

print("CFG Parse Trees:\n")

found = False

for tree in parser.parse(sentence):
    print(tree)
    print()
    tree.pretty_print()
    found = True
    break

if not found:
    print("No parse tree found.")

print("\nDependency Relationships:")

dependencies = [
    ("saw", "She", "subject"),
    ("saw", "man", "object"),
    ("man", "the", "determiner"),
    ("saw", "with", "preposition"),
    ("with", "telescope", "object"),
    ("telescope", "a", "determiner")
]

for head, word, relation in dependencies:
    print(f"{head} -> {word} ({relation})")
