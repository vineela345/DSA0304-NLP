words = ["activate", "activation", "reactivation"]

print("-" * 150)
print("{:<15}{:<10}{:<12}{:<12}{:<25}{:<25}{:<15}{:<20}".format(
    "Original", "Prefix", "Root", "Suffix",
    "Derivational Sequence", "Meaning Change",
    "Normalized", "Parsed"))
print("-" * 150)

for word in words:

    if word == "activate":
        prefix = "-"
        root = "active"
        suffix = "-ate"
        sequence = "active → activate"
        meaning = "Make active"
        normalized = "active"
        parsed = "active + ate"

    elif word == "activation":
        prefix = "-"
        root = "active"
        suffix = "-ation"
        sequence = "active → activate → activation"
        meaning = "Process of activating"
        normalized = "active"
        parsed = "active + ate + ion"

    elif word == "reactivation":
        prefix = "re"
        root = "active"
        suffix = "-ation"
        sequence = "active → activate → activation → reactivation"
        meaning = "Activate again"
        normalized = "active"
        parsed = "re + active + ate + ion"

    print("{:<15}{:<10}{:<12}{:<12}{:<25}{:<25}{:<15}{:<20}".format(
        word, prefix, root, suffix,
        sequence, meaning, normalized, parsed))
