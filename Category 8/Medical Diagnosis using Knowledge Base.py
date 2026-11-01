# Medical Diagnosis using Knowledge Base

facts = {
    "fever",
    "cough",
    "cold",
    "headache"
}

rules = {
    "Flu": ["fever", "cough", "headache"],
    "Common Cold": ["cold", "cough"],
    "Malaria": ["fever", "headache"],
    "Viral Infection": ["fever", "cough"]
}

# Forward Chaining
def forward_chaining(facts):

    new_facts = set(facts)

    while True:
        added = False

        for disease, symptoms in rules.items():

            if all(s in new_facts for s in symptoms):
                if disease not in new_facts:
                    new_facts.add(disease)
                    print("Derived:", disease)
                    added = True

        if not added:
            break

    return new_facts


# Backward Chaining
def backward_chaining(goal, facts):

    if goal in facts:
        return True

    if goal in rules:
        return all(
            backward_chaining(symptom, facts)
            for symptom in rules[goal]
        )

    return False


print("Medical Diagnosis System")

print("\nInitial Symptoms:", facts)

print("\nForward Chaining:")
result = forward_chaining(facts)

print("\nPossible Diseases:")
for item in result:
    if item not in facts:
        print(item)

print("\nBackward Chaining:")
disease = "Flu"

if backward_chaining(disease, facts):
    print(disease, "is supported by the symptoms")
else:
    print(disease, "is not supported")
