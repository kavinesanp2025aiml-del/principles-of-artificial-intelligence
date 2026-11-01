# Automated Real Estate Appraiser vs Ride-Sharing Surge Pricing Agent
class StaticUtilityAgent:
    def __init__(self):
        self.weights = {"sq_ft": 0.1, "bedrooms": 1.5}
    def calculate_property_utility(self, property_id, sq_ft, bedrooms):
        utility_score = (sq_ft * self.weights["sq_ft"]) + (bedrooms * self.weights["bedrooms"])
        return f"Static Valuation [Property #{property_id}] -> Calculated Utility: {utility_score:.2f} points"
class DynamicUtilityAgent:
    def __init__(self):
        self.base_fare = 10.0
    def calculate_trip_utility(self, trip_id, distance, active_passenger_demands):
        surge_multiplier = 1.0 + (active_passenger_demands * 0.05)
        utility_score = (self.base_fare + (distance * 1.5)) * surge_multiplier
        return f"Dynamic Fare Agent [Trip #{trip_id}] -> Current Demand: {active_passenger_demands} users | Utility Score: {utility_score:.2f}"
print("=== RUNNING STATIC AGENT (Real Estate Value Appraiser) ===")
static_agent = StaticUtilityAgent()
print(static_agent.calculate_property_utility(property_id=1, sq_ft=1200, bedrooms=2))
print(static_agent.calculate_property_utility(property_id=2, sq_ft=2500, bedrooms=4))
print(static_agent.calculate_property_utility(property_id=1, sq_ft=1200, bedrooms=2))
print("\n=== RUNNING DYNAMIC AGENT (Ride-Share Surge Pricing Dashboard) ===")
dynamic_agent = DynamicUtilityAgent()
print(dynamic_agent.calculate_trip_utility(trip_id=501, distance=5.0, active_passenger_demands=2))
print(dynamic_agent.calculate_trip_utility(trip_id=502, distance=5.0, active_passenger_demands=30))
print(dynamic_agent.calculate_trip_utility(trip_id=503, distance=5.0, active_passenger_demands=5))
