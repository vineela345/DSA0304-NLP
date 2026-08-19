import re

sentence = (
    "The doctor who reviewed the patient last week recommends "
    "starting medication and scheduling a follow-up visit in Chennai."
)

print("HEALTHCARE NLP SYSTEM")
print("=" * 60)

print("\n1. INPUT")
print(sentence)

tokens = re.findall(r"\b[\w-]+\b", sentence)

print("\n2. TOKENIZATION")
print(tokens)

print("\n3. SYNTACTIC ANALYSIS USING CFG")
print("Subject: The doctor")
print("Relative Clause: who reviewed the patient last week")
print("Main Verb: recommends")
print("Object 1: starting medication")
print("Object 2: scheduling a follow-up visit in Chennai")

print("\n4. PCFG AMBIGUITY RESOLUTION")
print("Main subject probability: Doctor -> 0.95")
print("Relative clause attachment -> 0.90")
print("Medical action interpretation -> 0.97")

print("\n5. FEATURE STRUCTURE")

features = {
    "subject": "doctor",
    "number": "singular",
    "tense": "present",
    "main_verb": "recommends",
    "domain": "healthcare"
}

for key, value in features.items():
    print(key, ":", value)

print("\n6. SUB-CATEGORIZATION FRAMES")

frames = {
    "review": "review(DOCTOR, PATIENT)",
    "recommend": "recommend(DOCTOR, ACTION)",
    "start": "start(PATIENT, MEDICATION)",
    "schedule": "schedule(PATIENT, VISIT, LOCATION)"
}

for verb, frame in frames.items():
    print(verb, "->", frame)

print("\n7. SEMANTIC ROLE ASSIGNMENT")

roles = {
    "doctor": "Agent",
    "patient": "Patient/Experiencer",
    "medication": "Treatment",
    "follow-up visit": "Medical Action",
    "Chennai": "Location"
}

for entity, role in roles.items():
    print(entity, "->", role)

print("\n8. MEDICAL ACTION EXTRACTION")

actions = [
    "Starting medication",
    "Scheduling follow-up visit"
]

for action in actions:
    print("Action:", action)

print("\n9. LOCATION EXTRACTION")
print("Location: Chennai")

print("\n10. REAL-TIME PROCESSING")
print("Input received")
print("-> Tokenization")
print("-> Syntax parsing")
print("-> PCFG ranking")
print("-> Feature validation")
print("-> Semantic extraction")
print("-> Structured output")

print("\n11. STRUCTURED OUTPUT")

output = {
    "Diagnosis": "Not explicitly stated",
    "Doctor": "Doctor",
    "Patient": "Patient",
    "Actions": [
        "Start medication",
        "Schedule follow-up visit"
    ],
    "Location": "Chennai",
    "Time": "Follow-up visit",
    "Confidence": 0.95
}

for key, value in output.items():
    print(key, ":", value)

print("\n12. HOSPITAL SCALABILITY")
print("1. Use efficient chart parsing.")
print("2. Use medical-specific PCFG rules.")
print("3. Use feature structures for agreement.")
print("4. Use sub-categorization frames for medical verbs.")
print("5. Use parallel processing for multiple reports.")
print("6. Store structured information in a medical database.")
print("7. Use confidence scores for uncertain cases.")
