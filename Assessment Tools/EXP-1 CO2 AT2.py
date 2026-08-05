words = ["analyzing", "analysis", "analytical"]

print("-" * 95)
print("{:<15}{:<12}{:<15}{:<15}{:<15}{:<15}".format(
    "Original", "Root", "Affix", "Type", "Normalized", "Structure"))
print("-" * 95)

for word in words:

    if word == "analyzing":
        root = "analyze"
        affix = "-ing"
        mtype = "Inflectional"
        normalized = "analyze"
        structure = "analyze + ing"

    elif word == "analysis":
        root = "analyze"
        affix = "-sis"
        mtype = "Derivational"
        normalized = "analyze"
        structure = "analyze + sis"

    elif word == "analytical":
        root = "analyze"
        affix = "-ical"
        mtype = "Derivational"
        normalized = "analyze"
        structure = "analyze + ical"

    print("{:<15}{:<12}{:<15}{:<15}{:<15}{:<15}".format(
        word, root, affix, mtype, normalized, structure))
