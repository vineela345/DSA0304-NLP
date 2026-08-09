words = ["writes", "writing", "written"]

print("{:<10}{:<25}{:<10}{:<15}{:<10}".format("Word","State Path","Root","Pattern","Normalized"))

for word in words:
    if word == "writes":
        path = "Start->write->s"
        root = "write"
        pattern = "Regular"
    elif word == "writing":
        path = "Start->write->ing"
        root = "write"
        pattern = "Regular"
    else:
        path = "Start->write->written"
        root = "write"
        pattern = "Irregular"

    print("{:<10}{:<25}{:<10}{:<15}{:<10}".format(word,path,root,pattern,root))
