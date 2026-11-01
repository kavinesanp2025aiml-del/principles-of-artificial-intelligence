# Smart Thermostat vs. Bump-Sensor Vacuum
class SmartThermostatAgent:
    """
    Fully Observable Simple Reflex Agent.
    It can see the exact, complete state required to make a perfect choice:
    (Current Temperature, Occupancy Status)
    """

    def __init__(self, target_temp=72):
        self.target_temp = target_temp
        # Rules map explicit condition tuples to clear actions
        self.rules = {
            ("cold", "Occupied"): "Turn Heat On High",
            ("cold", "Vacant"): "Turn Heat On Low (Eco)",
            ("perfect", "Occupied"): "Turn Off System",
            ("perfect", "Vacant"): "Turn Off System",
            ("hot", "Occupied"): "Turn AC On High",
            ("hot", "Vacant"): "Turn AC On Low (Eco)",
        }

    def act(self, percept):
        # Percept structure: (temperature_status, occupancy_status)
        return self.rules.get(percept, "Maintain Idle")


class BasicRoboticVacuumAgent:
    """
    Partially Observable Simple Reflex Agent.
    It has a major blind spot: it only senses if it is currently touching
    an obstacle ("bumped") or not ("clear"). It cannot see walls ahead or
    know its coordinates in the room.
    """

    def __init__(self):
        # Rules map a single, limited sensor reading directly to an action
        self.rules = {
            "clear": "Drive Forward",
            "bumped": "Reverse and Spin 90 Degrees",
        }

    def act(self, percept):
        # Percept structure: string matching sensor state
        return self.rules.get(percept, "Stop")


# =====================================================================
# SIMULATION ENGINE
# =====================================================================

# 1. Testing the Fully Observable Smart Thermostat
thermostat = SmartThermostatAgent(target_temp=72)

# Scenario A: House is freezing and the family is home
percept_winter_night = ("cold", "Occupied")
action_thermostat_a = thermostat.act(percept_winter_night)

# Scenario B: House is freezing but everyone is at work
percept_winter_workday = ("cold", "Vacant")
action_thermostat_b = thermostat.act(percept_winter_workday)


# 2. Testing the Partially Observable Basic Vacuum
vacuum = BasicRoboticVacuumAgent()

# Scenario A: Vacuum is in open space in the center of the living room
percept_open_floor = "clear"
action_vacuum_a = vacuum.act(percept_open_floor)

# Scenario B: Vacuum hits the base of the sofa
percept_hit_wall = "bumped"
action_vacuum_b = vacuum.act(percept_hit_wall)


# =====================================================================
# CONSOLE OUTPUT (Execution Logs)
# =====================================================================

print("--- SMART THERMOSTAT SIMULATION (Fully Observable) ---")
print(f"Percept: {percept_winter_night} -> Action: {action_thermostat_a}")
print(f"Percept: {percept_winter_workday} -> Action: {action_thermostat_b}")
print("\nWhy it is Fully Observable:")
print("The agent accurately tailors its power usage because its sensors")
print("deliver the absolute reality of both the environment and context.")

print("\n" + "=" * 60 + "\n")

print("--- ROBOTIC VACUUM SIMULATION (Partially Observable) ---")
print(f"Percept: '{percept_open_floor}' -> Action: {action_vacuum_a}")
print(f"Percept: '{percept_hit_wall}' -> Action: {action_vacuum_b}")
print("\nWhy it is Partially Observable:")
print("The vacuum operates blindly. When it receives 'clear', it moves forward")
print("whether it is 10 feet away from a wall or 1 inch away from a drop-off.")
print("It lacks the complete environmental state to plan ahead.")
