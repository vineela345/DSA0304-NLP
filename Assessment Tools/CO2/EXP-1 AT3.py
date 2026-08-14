import pandas as pd
from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = [
    "infection", "infectious", "infected", "infect",
    "infections", "infecting", "infectivity", "infectiousness"
]

df = pd.DataFrame({
    "Original": words,
    "Stem": [ps.stem(w) for w in words]
})

print(df)
