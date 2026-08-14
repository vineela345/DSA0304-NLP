import pandas as pd
import nltk
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download("punkt")

ps = PorterStemmer()

data = pd.read_csv("BBCNews.csv")

def preprocess(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    words = word_tokenize(text)
    stems = [ps.stem(word) for word in words]
    return " ".join(stems)

data["Processed"] = data["Text"].apply(preprocess)

print(data[["Text", "Processed"]].head())

test_words = [
    "organization", "organizer", "organizing", "organized",
    "studies", "studied", "studying", "companies", "connectivity",
    "happiness", "relational", "educational", "traditional",
    "national", "effective", "hopeful", "readable", "kindness",
    "quickly", "management"
]

for word in test_words:
    print(word, "->", ps.stem(word))
