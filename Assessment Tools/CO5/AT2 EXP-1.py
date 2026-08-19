import re

text = "Ravi met Arun at the library. He borrowed a book and later returned it."

sentences = text.split(". ")
entities = ["Ravi", "Arun"]

pronouns = ["He", "it"]

antecedents = {
    "He": "Ravi",
    "it": "book"
}

resolved = text

for pronoun, entity in antecedents.items():
    resolved = re.sub(r"\b" + pronoun + r"\b", entity, resolved)

print("Original Discourse:")
print(text)

print("\nPronoun Resolution:")
for pronoun, entity in antecedents.items():
    print(pronoun, "->", entity)

print("\nResolved Discourse:")
print(resolved)

print("\nContext Validation:")
print("He -> Ravi because Ravi is the most suitable male antecedent in the context.")
print("it -> book because 'book' is the object previously introduced and fits the action 'returned'.")
