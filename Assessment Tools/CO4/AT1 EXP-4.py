sentences = [
    {
        "sentence": "Doctor prescribed medicine to patient.",
        "subject": "Doctor",
        "verb": "prescribed",
        "object": "Medicine",
        "recipient": "Patient"
    },
    {
        "sentence": "Patient reported severe headache.",
        "subject": "Patient",
        "verb": "reported",
        "object": "Headache",
        "recipient": None
    },
    {
        "sentence": "Nurse monitored patient continuously.",
        "subject": "Nurse",
        "verb": "monitored",
        "object": "Patient",
        "recipient": None
    },
    {
        "sentence": "Medicine reduced blood pressure.",
        "subject": "Medicine",
        "verb": "reduced",
        "object": "Blood Pressure",
        "recipient": None
    }
]

print("SYNTAX-DRIVEN SEMANTIC ANALYSIS")
print("-" * 50)

for item in sentences:
    print("\nSentence:", item["sentence"])
    print("Subject:", item["subject"])
    print("Verb:", item["verb"])
    print("Object:", item["object"])

    if item["recipient"]:
        print("Recipient:", item["recipient"])

print("\nSEMANTIC ROLES")

roles = {
    "Doctor": "Agent",
    "Medicine": "Instrument / Cause",
    "Patient": "Recipient",
    "Headache": "Symptom",
    "Nurse": "Agent",
    "Blood Pressure": "Affected Entity"
}

for entity, role in roles.items():
    print(entity, "->", role)

print("\nROLE ANALYSIS")
print("Doctor -> Agent: Appropriate")
print("Patient -> Recipient: Appropriate for prescribed medicine")
print("Headache -> Symptom: Appropriate")
print("Nurse -> Agent: Appropriate")
print("Medicine -> Instrument/Cause: Appropriate")
print("Blood Pressure -> Affected Entity: Appropriate")

print("\nPARSING ERRORS")
print("1. Wrong subject may assign an incorrect Agent.")
print("2. Wrong object may identify the wrong medical entity.")
print("3. Incorrect dependency parsing may change semantic meaning.")
print("4. Incorrect roles may lead to wrong clinical information extraction.")

print("\nIMPROVEMENT METHODS")
print("1. Use medical-domain NLP models.")
print("2. Apply dependency parsing.")
print("3. Use medical named-entity recognition.")
print("4. Combine syntax with semantic context.")
print("5. Validate extracted relationships using medical knowledge bases.")
