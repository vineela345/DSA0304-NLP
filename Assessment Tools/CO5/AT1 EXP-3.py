sentence = "The bank by the river flooded after the storm, but it was saved by quick action."

print("SOURCE SENTENCE:")
print(sentence)

print("\nWORD SENSE DISAMBIGUATION")

context = ["river", "flooded", "storm"]

if "river" in context and "flooded" in context:
    bank = "riverbank"
else:
    bank = "financial bank"

print("Ambiguous word: bank")
print("Resolved meaning:", bank)
print("Reason: river and flooded indicate the land beside a river.")

print("\nPREDICATE LOGIC")

print("river(r)")
print("bank(b)")
print("location(b,r)")
print("storm(s)")
print("flood(b)")
print("after(flood(b),s)")
print("quick_action(a)")
print("saved_by(b,a)")

print("\nDISCOURSE RELATION")
print("Contrast(flood(b), saved_by(b,a))")

print("\nPARAPHRASE")
print("The riverbank flooded after the storm, but quick action saved it.")

print("\nRST DISCOURSE TREE")
print("                 CONTRAST")
print("                /        \\")
print("               /          \\")
print("      Clause 1              Clause 2")
print("         |                      |")
print(" Riverbank flooded       Quick action saved it")
print("         |                      |")
print("   After the storm        Quick action")
