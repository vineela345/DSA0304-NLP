words = ["govern", "government", "governance"]

print("-" * 110)
print("{:<15}{:<10}{:<15}{:<20}{:<15}{:<15}".format(
    "Original", "Root", "Affix", "Derivational Level", "Normalized", "Output"))
print("-" * 110)

for word in words:

    if word == "govern":
        root = "govern"
        affix = "-"
        level = "Level 0"
        normalized = "govern"
        output = "govern"

    elif word == "government":
        root = "govern"
        affix = "-ment"
        level = "Level 1"
        normalized = "govern"
        output = "govern"

    elif word == "governance":
        root = "govern"
        affix = "-ance"
        level = "Level 1"
        normalized = "govern"
        output = "govern"

    print("{:<15}{:<10}{:<15}{:<20}{:<15}{:<15}".format(
        word, root, affix, level, normalized, output))
