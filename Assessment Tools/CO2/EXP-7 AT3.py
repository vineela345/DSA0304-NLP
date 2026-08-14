from nltk.stem import PorterStemmer

ps = PorterStemmer()

documents = [
    "The organization announced a new technology platform.",
    "The organizer arranged a business conference.",
    "The company organized a technology event.",
    "The technology organization developed new software.",
    "The company is organizing a new project."
]

print("ORIGINAL AND STEMMED TEXT\n")

for text in documents:
    words = text.lower().split()
    stemmed = [ps.stem(word.strip(".,!?")) for word in words]

    print("Original:", text)
    print("Stemmed :", " ".join(stemmed))
    print("-" * 60)

print("\n20 STEMMING EXAMPLES\n")

words = [
    "organization",
    "organizer",
    "organizing",
    "organized",
    "studies",
    "studied",
    "studying",
    "companies",
    "connectivity",
    "happiness",
    "relational",
    "educational",
    "traditional",
    "national",
    "effective",
    "hopeful",
    "readable",
    "kindness",
    "quickly",
    "management"
]

for word in words:
    print(word, "->", ps.stem(word))
