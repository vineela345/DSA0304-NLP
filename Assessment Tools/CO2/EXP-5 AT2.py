words = ["create", "creates", "creating"]

print("-" * 110)
print("{:<15}{:<12}{:<25}{:<12}{:<15}{:<15}".format(
    "Original", "Suffix", "Grammar", "Root", "Normalized", "Output"))
print("-" * 110)

for word in words:

    if word == "create":
        suffix = "-"
        grammar = "Base Form"
        root = "create"
        normalized = "create"
        output = "create"

    elif word == "creates":
        suffix = "-s"
        grammar = "3rd Person Singular"
        root = "create"
        normalized = "create"
        output = "create"

    elif word == "creating":
        suffix = "-ing"
        grammar = "Present Participle"
        root = "create"
        normalized = "create"
        output = "create"

    print("{:<15}{:<12}{:<25}{:<12}{:<15}{:<15}".format(
        word, suffix, grammar, root, normalized, output))
