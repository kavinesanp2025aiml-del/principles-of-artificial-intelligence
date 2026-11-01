# A Smart Warehouse Robot vs A Self-Driving Cruise Control
class DiscreteModelAgent:
    def __init__(self):
        self.internal_state = {"x": 0, "y": 0}
        self.action_effects = {
            "NORTH": (0, 1),
            "SOUTH": (0, -1),
            "EAST":  (1, 0),
            "WEST":  (-1, 0)
        }

    def update_model_and_act(self, action):
        dx, dy = self.action_effects.get(action, (0, 0))
        self.internal_state["x"] += dx
        self.internal_state["y"] += dy

        return f"Discrete Warehouse Robot moved {action}. New Internal Model State: {self.internal_state}"


class ContinuousModelAgent:
    def __init__(self):
        self.internal_state = {"velocity": 55.0}
        self.target_speed = 60.0

    def update_model_and_act(self, current_sensor_speed):
        self.internal_state["velocity"] = current_sensor_speed
        speed_error = self.target_speed - self.internal_state["velocity"]

        raw_throttle = speed_error * 0.5
        applied_throttle = max(-1.0, min(1.0, raw_throttle))

        self.internal_state["velocity"] += applied_throttle * 2.0

        return f"Continuous Cruise Control applied throttle: {applied_throttle:.2f}. Predicted Velocity: {self.internal_state['velocity']:.2f} mph"


print("=== RUNNING DISCRETE AGENT (Warehouse Robot Grid Navigation) ===")
discrete_agent = DiscreteModelAgent()
print(discrete_agent.update_model_and_act("NORTH"))
print(discrete_agent.update_model_and_act("EAST"))
print(discrete_agent.update_model_and_act("NORTH"))

print("\n=== RUNNING CONTINUOUS AGENT (Autonomous Cruise Control System) ===")
continuous_agent = ContinuousModelAgent()
print(continuous_agent.update_model_and_act(55.0))
print(continuous_agent.update_model_and_act(57.0))
print(continuous_agent.update_model_and_act(62.5))
