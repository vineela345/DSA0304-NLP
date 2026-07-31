words = ["unhappy", "happiness", "happily"]

print("{:<12}{:<10}{:<10}{:<10}{:<15}{:<10}".format("Word","Prefix","Root","Suffix","Type","Normalized"))

for word in words:
    prefix = "-"
    suffix = "-"

    if word.startswith("un"):
        prefix = "un"
        root = "happy"
        t = "Derivational"
    elif word.endswith("ness"):
        root = "happy"
        suffix = "ness"
        t = "Derivational"
    elif word.endswith("ly"):
        root = "happy"
        suffix = "ly"
        t = "Derivational"

    print("{:<12}{:<10}{:<10}{:<10}{:<15}{:<10}".format(word,prefix,root,suffix,t,root))
