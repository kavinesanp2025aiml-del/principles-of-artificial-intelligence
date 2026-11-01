#It calculates a utility score for different brightness levels to find the choice that provides the best balance between visibility and battery life
import time
class UtilityBasedAgent:
    def __init__(self):
        pass
    def act(self, battery_level):
        choices = ["HIGH_BRIGHTNESS", "MEDIUM_BRIGHTNESS", "LOW_BRIGHTNESS"]
        best_action = None
        highest_utility = -float("inf")
        for action in choices:
            if action == "HIGH_BRIGHTNESS":
                utility = battery_level * 2 - 80
            elif action == "MEDIUM_BRIGHTNESS":
                utility = 50
            elif action == "LOW_BRIGHTNESS":
                utility = (100 - battery_level) * 2
            if utility > highest_utility:
                highest_utility = utility
                best_action = action
        return best_action
agent = UtilityBasedAgent()
simulated_battery = [100, 80, 50, 30, 10]

for battery in simulated_battery:
    action = agent.act(battery)
    print(f"Battery: {battery}% | Action chosen: {action}")
    time.sleep(0.1)
