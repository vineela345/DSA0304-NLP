queries = {
    "Q1": {
        "query": "Activate international roaming for my number",
        "actual": "Activate Roaming",
        "predicted": "Activate Roaming",
        "representation": "ACTIVATE(Roaming, Customer)"
    },
    "Q2": {
        "query": "Deactivate caller tune service",
        "actual": "Deactivate Caller Tune",
        "predicted": "Activate Caller Tune",
        "representation": "DEACTIVATE(CallerTune, Customer)"
    },
    "Q3": {
        "query": "Check my data balance",
        "actual": "Check Data Balance",
        "predicted": "Query Data Balance",
        "representation": "QUERY(DataBalance, Customer)"
    },
    "Q4": {
        "query": "Enable 5G service",
        "actual": "Enable 5G Service",
        "predicted": "Activate 5G Service",
        "representation": "ACTIVATE(5GService, Customer)"
    }
}

print("SEMANTIC REPRESENTATION ANALYSIS")
print("-" * 50)

correct = 0

for q, data in queries.items():
    print("\n", q)
    print("Query:", data["query"])
    print("Semantic Representation:", data["representation"])

    if data["actual"] == data["predicted"]:
        print("Status: Correct")
        correct += 1
    else:
        print("Status: Semantic Error")

accuracy = correct / len(queries) * 100

print("\nACTION-OBJECT RELATIONSHIPS")
print("ACTIVATE -> Roaming / 5GService")
print("DEACTIVATE -> CallerTune")
print("QUERY -> DataBalance")

print("\nIncorrect Query: Q2")
print("Reason: User requested DEACTIVATE Caller Tune,")
print("but system predicted ACTIVATE Caller Tune.")

print("\nDecision Accuracy:", accuracy, "%")

print("\nIMPROVEMENTS")
print("1. Use intent classification with action and object separately.")
print("2. Identify positive and negative action words.")
print("3. Use context from previous conversations.")
print("4. Maintain telecom-specific semantic dictionaries.")
print("5. Validate semantic representation before executing an action.")
