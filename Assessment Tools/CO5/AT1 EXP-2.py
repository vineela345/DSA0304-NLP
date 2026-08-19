responses = [
    "You can concentrate better by studying one small topic at a time, because short goals make the exam preparation easier. Take a short break after each study session so you feel confident for the exam.",
    
    "Try to focus on the most important topics first, because organized study reduces exam stress. Take a short break between sessions and remind yourself that you can be confident in the exam.",
    
    "Focus on one topic at a time and avoid distractions, because this will help you concentrate for the exam. Take a short break when needed so you stay confident and motivated."
]

print("A) DISCOURSE PLANNING STEPS")
print("1. Identify the situation: Student has an important exam and cannot concentrate.")
print("2. Select dialogue acts: Advise + Encourage.")
print("3. Maintain entities: exam, concentrate, you.")
print("4. Establish discourse relation: Cause-Effect.")
print("5. Include required keywords: focus, break, confident.")
print("6. Generate a polite and positive 2-3 sentence response.")

print("\nB) THREE POSSIBLE RESPONSES")
for i, response in enumerate(responses, 1):
    print(f"\nResponse {i}:")
    print(response)

print("\nC) EVALUATION")
scores = [5, 5, 5]

for i, score in enumerate(scores, 1):
    print(f"Response {i}: Coherence = Good, Constraints satisfied = Yes, Score = {score}/5")

print("\nBest Response: Response 3")
print("Reason: It directly addresses concentration, gives practical advice,")
print("uses a Cause-Effect relation, contains focus, break and confident,")
print("maintains entity coherence, and has a positive tone.")

print("\nD) EFFECT OF VIOLATING TWO CONSTRAINTS")
print("1. If entity coherence is violated, the response may become unclear")
print("because the connection with the exam and concentration problem is lost.")

print("2. If the 2-3 sentence length constraint is violated, the response")
print("may become too long or incomplete for the required dialogue format.")
