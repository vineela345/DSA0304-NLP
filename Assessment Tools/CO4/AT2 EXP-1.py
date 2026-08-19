import nltk
from nltk import CFG, PCFG
from nltk.parse import ChartParser, EarleyChartParser

grammar = CFG.fromstring("""
S -> VP
VP -> V NP PP
NP -> Det N
NP -> Det N PP
PP -> P NP
V -> "show"
Det -> "the" | "me"
N -> "transactions" | "card" | "month"
P -> "with" | "from"
""")

sentence = "show the transactions with the card from month".split()

print("BANKING CHATBOT - CFG ANALYSIS")
print("-" * 50)

parser = EarleyChartParser(grammar)

trees = list(parser.parse(sentence))

print("Input:", " ".join(sentence))
print("Number of possible parses:", len(trees))

for i, tree in enumerate(trees[:3], 1):
    print("\nParse", i)
    print(tree)

print("\nAMBIGUITY")
print("The phrase 'with the card' can modify transactions")
print("or describe the method used for the transaction.")

print("\nCFG LIMITATIONS")
print("1. CFG does not assign probabilities.")
print("2. Ambiguous structures may have equal priority.")
print("3. Basic CFG does not handle agreement well.")
print("4. Long sentences can generate many parse trees.")
print("5. Conversational context is difficult to represent.")

pcfg = PCFG.fromstring("""
S -> VP [1.0]
VP -> V NP PP [1.0]
NP -> Det N [0.7]
NP -> Det N PP [0.3]
PP -> P NP [1.0]
V -> "show" [1.0]
Det -> "the" [0.7]
Det -> "me" [0.3]
N -> "transactions" [0.5]
N -> "card" [0.3]
N -> "month" [0.2]
P -> "with" [0.6]
P -> "from" [0.4]
""")

print("\nPCFG IMPROVEMENT")
print("PCFG assigns probabilities to competing parse structures.")
print("The highest probability interpretation can be selected.")

print("\nFEATURE STRUCTURE")
features = {
    "subject": "customer",
    "number": "singular",
    "intent": "transaction_query",
    "object": "transactions",
    "payment_method": "card",
    "time": "last_month"
}

for key, value in features.items():
    print(key, ":", value)

print("\nINDUSTRY BENEFITS")
print("1. Better ambiguity resolution")
print("2. Agreement checking")
print("3. Efficient parsing of long queries")
print("4. Better transaction intent detection")
print("5. More accurate banking responses")
