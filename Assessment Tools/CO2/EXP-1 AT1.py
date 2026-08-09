words = ["connected", "connecting", "connection"]

print("{:<15} {:<10} {:<15} {:<15} {:<15}".format(
    "Word", "Root", "Suffix", "Type", "Normalized"))
print("-" * 75)

for word in words:

    if word == "connected":
        root = "connect"
        suffix = "ed"
        type_ = "Inflectional"
        normalized = "connect"

    elif word == "connecting":
        root = "connect"
        suffix = "ing"
        type_ = "Inflectional"
        normalized = "connect"

    elif word == "connection":
        root = "connect"
        suffix = "ion"
        type_ = "Derivational"
        normalized = "connect"

    print("{:<15} {:<10} {:<15} {:<15} {:<15}".format(
        word, root, suffix, type_, normalized))
