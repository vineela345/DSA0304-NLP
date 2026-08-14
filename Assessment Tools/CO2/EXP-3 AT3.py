from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

documents = [
    "The organization announced a new technology platform",
    "The organizer arranged a business conference",
    "The company organized a technology event",
    "The technology organization developed new software",
    "The business organizer announced a new company",
    "Technology companies developed new computer systems",
    "Business organizations announced new financial plans"
]

labels = [0, 1, 0, 0, 1, 0, 1]

ps = PorterStemmer()

def stem_text(text):
    return " ".join(ps.stem(w) for w in text.lower().split())

stemmed = [stem_text(x) for x in documents]

print("Original vs Stemmed:")

for original, stem in zip(documents, stemmed):
    print("\nOriginal:", original)
    print("Stemmed :", stem)

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(stemmed)

model = LogisticRegression(max_iter=1000)

model.fit(X, labels)

print("\nVocabulary Size:", len(vectorizer.vocabulary_))
print("Accuracy:", model.score(X, labels))

print("\nStemming Examples:")

for word in [
    "organization",
    "organizer",
    "organizing",
    "organized"
]:
    print(word, "->", ps.stem(word))
