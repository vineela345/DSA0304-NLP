words = ["unhappy", "happiness", "happily"]

print("{:<15} {:<10} {:<10} {:<15} {:<15}".format(
    "Word", "Prefix", "Suffix", "Type", "Normalized"))
print("-" * 70)

for word in words:

    if word == "unhappy":
        prefix = "un"
        suffix = "-"
        type_ = "Derivational"
        normalized = "happy"

    elif word == "happiness":
        prefix = "-"
        suffix = "ness"
        type_ = "Derivational"
        normalized = "happy"

    elif word == "happily":
        prefix = "-"
        suffix = "ly"
        type_ = "Derivational"
        normalized = "happy"

    print("{:<15} {:<10} {:<10} {:<15} {:<15}".format(
        word, prefix, suffix, type_, normalized))
