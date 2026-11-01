import random
import time

class Environment:
    def __init__(self):
        # The environment contains two rooms, each can be 'Clean' or 'Dirty'
        self.locations = {'A': 'Dirty', 'B': 'Dirty'}
        self.randomize_environment()

    def randomize_environment(self):
        # Randomly assign status to rooms to simulate a real-world scenario
        for room in self.locations:
            self.locations[room] = random.choice(['Clean', 'Dirty'])

    def get_status(self, room):
        return self.locations[room]

    def update_environment(self, room, action):
        if action == 'Suck':
            self.locations[room] = 'Clean'


class SimpleReflexVacuumAgent:
    def __init__(self, initial_room):
        # The agent only tracks its current location, not past states
        self.current_location = initial_room

    def perceive(self, environment):
        # SENSOR: Perceives the status of the current room
        status = environment.get_status(self.current_location)
        return self.current_location, status

    def act(self, percept):
        # CONDITION-ACTION RULES: Decisions made purely on current percept
        location, status = percept
        
        if status == 'Dirty':
            return 'Suck'
        elif location == 'A':
            return 'Right'  # Move to Room B
        elif location == 'B':
            return 'Left'   # Move to Room A

    def execute_action(self, action):
        # ACTUATORS: Executing the chosen action
        if action == 'Suck':
            print(f"[Agent] Cleaning Room {self.current_location}...")
        elif action == 'Right':
            print(f"[Agent] Room {self.current_location} is clean. Moving Right...")
            self.current_location = 'B'
        elif action == 'Left':
            print(f"[Agent] Room {self.current_location} is clean. Moving Left...")
            self.current_location = 'A'


# --- Simulation Run ---
if __name__ == "__main__":
    # Setup environment and place agent initially in Room A
    env = Environment()
    agent = SimpleReflexVacuumAgent(initial_room='A')
    
    print("Initial Environment State:", env.locations)
    print("-" * 40)

    # Simulate 4 cycles of perception and action
    for step in range(1, 5):
        print(f"\nStep {step}:")
        
        # 1. Perceive environment
        percept = agent.perceive(env)
        print(f"[Sensors] Perceived State: Room {percept[0]} is {percept[1]}")
        
        # 2. Rule evaluation
        chosen_action = agent.act(percept)
        
        # 3. Act on environment
        agent.execute_action(chosen_action)
        env.update_environment(agent.current_location, chosen_action)
        
        time.sleep(0.5)

    print("-" * 40)
    print("Final Environment State:", env.locations)
