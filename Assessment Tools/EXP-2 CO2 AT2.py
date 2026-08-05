words = ["disagree", "agreement", "agreeable"]

print("-" * 120)
print("{:<15}{:<10}{:<10}{:<12}{:<15}{:<25}{:<12}".format(
    "Original", "Prefix", "Root", "Suffix", "Type", "Meaning", "Normalized"))
print("-" * 120)

for word in words:

    if word == "disagree":
        prefix = "dis"
        root = "agree"
        suffix = "-"
        mtype = "Derivational"
        meaning = "Opposite of agree"
        normalized = "agree"

    elif word == "agreement":
        prefix = "-"
        root = "agree"
        suffix = "-ment"
        mtype = "Derivational"
        meaning = "State of agreeing"
        normalized = "agree"

    elif word == "agreeable":
        prefix = "-"
        root = "agree"
        suffix = "-able"
        mtype = "Derivational"
        meaning = "Able to agree"
        normalized = "agree"

    print("{:<15}{:<10}{:<10}{:<12}{:<15}{:<25}{:<12}".format(
        word, prefix, root, suffix, mtype, meaning, normalized))
