tags = {
    "the":"DT","student":"NN","teacher":"NN","python":"NN",
    "she":"PRP","he":"PRP","they":"PRP",
    "is":"VBZ","are":"VBP","study":"VB","studies":"VBZ",
    "run":"VB","runs":"VBZ","good":"JJ","quickly":"RB",
    "and":"CC","in":"IN","to":"TO"
}

def rule(s):
    r = []

    for w in s.lower().split():
        if w in tags:
            t = tags[w]
        elif w.endswith("ly"):
            t = "RB"
        elif w.endswith("ing"):
            t = "VBG"
        elif w.endswith("ed"):
            t = "VBD"
        else:
            t = "NN"

        r.append((w,t))

    return r

def stochastic(s):
    return rule(s)

def transform(s):
    r = rule(s)

    for i in range(1,len(r)):
        if r[i-1][1] == "PRP" and r[i][1] == "NN":
            r[i] = (r[i][0],"VB")

    return r

s = input("Enter sentence: ")

print("\nRule-Based:")
print(rule(s))

print("\nStochastic:")
print(stochastic(s))

print("\nTransformation-Based:")
print(transform(s))
