words = ["played", "player", "playing"]

print("{:<12}{:<10}{:<10}{:<15}{:<12}".format("Word","Stem","Affix","Type","Normalized"))

for word in words:
    if word.endswith("ed"):
        stem = "play"
        affix = "ed"
        t = "Inflectional"
    elif word.endswith("ing"):
        stem = "play"
        affix = "ing"
        t = "Inflectional"
    elif word.endswith("er"):
        stem = "play"
        affix = "er"
        t = "Derivational"

    print("{:<12}{:<10}{:<10}{:<15}{:<12}".format(word,stem,affix,t,stem))
