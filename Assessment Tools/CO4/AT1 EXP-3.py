queries = {
    "Apple accessories": {
        "sense1": "Fruit",
        "sense2": "Technology Brand",
        "context": "iPhone Charger",
        "correct": "Technology Brand"
    },
    "Mouse wireless": {
        "sense1": "Animal",
        "sense2": "Computer Device",
        "context": "Bluetooth Mouse",
        "correct": "Computer Device"
    },
    "Java tutorial": {
        "sense1": "Island",
        "sense2": "Programming Language",
        "context": "Coding Lessons",
        "correct": "Programming Language"
    },
    "Python course": {
        "sense1": "Snake",
        "sense2": "Programming Language",
        "context": "Software Development Training",
        "correct": "Programming Language"
    }
}

print("WORD SENSE DISAMBIGUATION")
print("-" * 50)

for query, data in queries.items():
    print("\nQuery:", query)
    print("Possible Sense 1:", data["sense1"])
    print("Possible Sense 2:", data["sense2"])
    print("Clicked Result:", data["context"])
    print("Selected Sense:", data["correct"])

print("\nSEMANTIC CUES")
print("Apple -> iPhone Charger -> Technology")
print("Mouse -> Bluetooth Mouse -> Computer Device")
print("Java -> Coding Lessons -> Programming")
print("Python -> Software Development Training -> Programming")

print("\nIMPACT OF INCORRECT SENSE")
print("1. Irrelevant search results")
print("2. Lower click-through rate")
print("3. Poor customer experience")
print("4. Reduced recommendations")
print("5. Lower sales and conversion")

print("\nINDUSTRIAL-SCALE WSD STRATEGY")
print("1. Use query context.")
print("2. Analyze clicked and purchased products.")
print("3. Use embeddings for semantic similarity.")
print("4. Use domain-specific dictionaries.")
print("5. Continuously learn from user behavior.")
