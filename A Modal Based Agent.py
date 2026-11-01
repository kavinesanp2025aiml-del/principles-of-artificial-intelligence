#Implementation of a model-based agent managing a Smart Warehouse Inventory System
import time

class WaterTankAgent:
    def __init__(self):
        self.water_level = 50
        self.pump_on = False

    def act(self, sensor_reading):
        # Update internal model
        self.water_level = sensor_reading

        # Condition-action rules
        if self.water_level < 20:
            self.pump_on = True
            return "TURN_PUMP_ON"
        elif self.water_level > 80:
            self.pump_on = False
            return "TURN_PUMP_OFF"

        return "HOLD"
agent = WaterTankAgent()
mock_sensor_data = [50, 35, 15, 45, 85, 70]

for reading in mock_sensor_data:
    action = agent.act(reading)
    print(f"Sensor: {reading}L | Model Level: {agent.water_level}L | Action: {action}")
    time.sleep(0.1)
