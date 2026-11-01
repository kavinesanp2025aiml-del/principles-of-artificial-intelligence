# A Quality Control Scanner vs E-Commerce Delivery Drone
class EpisodicGoalAgent:
    def __init__(self):
        self.goal = {"defect_flagged": True}
    def process_item(self, item_id, sensor_scratch_detected):
        goal_achieved = sensor_scratch_detected == self.goal["defect_flagged"]
        actions = ["PASS ITEM", "DIVERT TO REWORK BIN"]
        chosen_action = actions[int(goal_achieved)]
        return f"Episode [Item #{item_id}]: Scratch Detected: {sensor_scratch_detected} -> Action: {chosen_action}"
class SequentialGoalAgent:
    def __init__(self):
        self.goal_position = 3
        self.current_position = 0
    def move_towards_goal(self):
        distance_remaining = self.goal_position - self.current_position
        step = int(distance_remaining > 0)
        self.current_position += step
        goal_reached = self.current_position == self.goal_position
        status_messages = ["In Transit", "Goal Destination Reached!"]
        status = status_messages[int(goal_reached)]
        return f"Sequential Step -> Moving. Position: {self.current_position}/{self.goal_position} | Status: {status}"

print("=== RUNNING EPISODIC AGENT (Quality Control Scanner) ===")
episodic_agent = EpisodicGoalAgent()
print(episodic_agent.process_item(101, sensor_scratch_detected=False))
print(episodic_agent.process_item(102, sensor_scratch_detected=True))
print(episodic_agent.process_item(103, sensor_scratch_detected=False))
print("\n=== RUNNING SEQUENTIAL AGENT (Delivery Drone Navigation) ===")
sequential_agent = SequentialGoalAgent()
print(sequential_agent.move_towards_goal())
print(sequential_agent.move_towards_goal())
print(sequential_agent.move_towards_goal())
print(sequential_agent.move_towards_goal())
