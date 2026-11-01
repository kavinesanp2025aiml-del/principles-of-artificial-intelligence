# Industrial Manufacturing using Knowledge Base

facts = {
    "machine_on",
    "raw_material_available",
    "temperature_normal",
    "operator_available"
}

rules = {
    "Production_Ready": [
        "machine_on",
        "raw_material_available",
        "operator_available"
    ],

    "Start_Production": [
        "Production_Ready",
        "temperature_normal"
    ],

    "Quality_Check": [
        "Start_Production"
    ],

    "Product_Ready": [
        "Quality_Check"
    ],

    "Machine_Overheating": [
        "temperature_high"
    ]
}


# Forward Chaining
def forward_chaining(facts):

    new_facts = set(facts)

    while True:
        added = False

        for result, conditions in rules.items():

            if all(c in new_facts for c in conditions):

                if result not in new_facts:
                    new_facts.add(result)
                    print("Derived:", result)
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
            backward_chaining(condition, facts)
            for condition in rules[goal]
        )

    return False


print("Industrial Manufacturing System")

print("\nInitial Facts:", facts)

print("\nForward Chaining:")
result = forward_chaining(facts)

print("\nBackward Chaining:")

goal = "Product_Ready"

if backward_chaining(goal, facts):
    print(goal, "is achieved")
else:
    print(goal, "is not achieved")
