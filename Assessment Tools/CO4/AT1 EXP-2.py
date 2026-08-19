machines = {
    "M1": "Active",
    "M2": "Active",
    "M3": "Maintenance",
    "M4": "Active"
}

produces = {
    "M1": "Gear",
    "M2": "Wheel",
    "M3": "Gear",
    "M4": "Engine"
}

print("FIRST-ORDER PREDICATE CALCULUS")
print("-" * 50)

print("\nPRODUCTION DATA")

for machine, status in machines.items():
    print(f"{status}({machine})")

print("\nPREDICATE INFERENCES")

producing = []

for machine, status in machines.items():
    if status == "Active":
        producing.append(machine)
        print(f"Active({machine}) -> Producing({machine})")
    else:
        print(f"Maintenance({machine}) -> NOT Producing({machine})")

print("\nCURRENTLY PRODUCING MACHINES:")
print(producing)

available_products = []

for machine in producing:
    product = produces[machine]
    available_products.append(product)
    print(f"Produces({machine}, {product}) AND Active({machine}) -> Available({product})")

print("\nAVAILABLE PRODUCTS:")
for product in available_products:
    print(product)

if machines["M3"] == "Maintenance":
    print("\nGEAR PRODUCTION ANALYSIS")
    print("M3 is under maintenance.")
    print("Maintenance(M3) -> NOT Producing(M3)")
    print("M3 normally produces Gear.")
    print("Therefore, Gear production is affected by maintenance.")

print("\nEFFECTIVENESS")
print("1. Predicate logic represents machine states clearly.")
print("2. Rules allow automatic inference.")
print("3. It supports explainable decisions.")
print("4. It can detect production problems.")
print("5. More complex factories require additional predicates and rules.")
