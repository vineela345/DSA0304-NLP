from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["relational", "relation", "relate"]

print("{:<12}{:<20}{:<15}".format("Word","Intermediate","Final Stem"))

for word in words:
    if word == "relational":
        step = "relate"
    elif word == "relation":
        step = "relate"
    else:
        step = "relate"

    stem = ps.stem(word)

    print("{:<12}{:<20}{:<15}".format(word,step,stem))
