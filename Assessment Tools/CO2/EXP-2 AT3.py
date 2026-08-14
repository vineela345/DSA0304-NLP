prefixes = ["un", "re"]
suffixes = ["est", "ing", "able", "s"]

def parser(word):
    prefix = ""
    suffix = ""
    stem = word

    for p in prefixes:
        if stem.startswith(p) and len(stem) > len(p) + 2:
            prefix = p
            stem = stem[len(p):]
            break

    for s in sorted(suffixes, key=len, reverse=True):
        if stem.endswith(s) and len(stem) > len(s) + 2:
            suffix = s
            stem = stem[:-len(s)]
            break

    return prefix, stem, suffix

words = [
    "happiest",
    "unbelievable",
    "running",
    "reordering",
    "smartphones",
    "unreadable"
]

for word in words:
    print(word, "->", parser(word))
