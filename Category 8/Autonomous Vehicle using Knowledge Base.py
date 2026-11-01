# Autonomous Vehicle using Knowledge Base

facts = {
    "traffic_light_red",
    "obstacle_detected",
    "pedestrian_detected",
    "vehicle_moving"
}

rules = {
    "Stop": ["traffic_light_red"],
    "Brake": ["obstacle_detected"],
    "Pedestrian_Safety": ["pedestrian_detected"],
    "Slow_Down": ["vehicle_moving", "pedestrian_detected"],
    "Safe_To_Move": ["traffic_light_green"]
}


# Forward Chaining
def forward_chaining(facts):

    new_facts = set(facts)

    while True:
        added = False

        for action, conditions in rules.items():

            if all(c in new_facts for c in conditions):

                if action not in new_facts:
                    new_facts.add(action)
                    print("Action Derived:", action)
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


print("Autonomous Vehicle System")

print("\nInitial Facts:", facts)

print("\nForward Chaining:")
result = forward_chaining(facts)

print("\nBackward Chaining:")

goal = "Stop"

if backward_chaining(goal, facts):
    print(goal, "action is required")
else:
    print(goal, "action is not required")
