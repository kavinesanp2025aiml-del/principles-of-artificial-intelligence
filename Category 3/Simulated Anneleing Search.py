# VLSI Chip Layout Optimization using Simulated Anneleing Search
import random
import math
wire_length = [150, 130, 110, 95, 90,
               85, 88, 92, 75, 60]
def simulated_annealing():
    current = random.randint(0, len(wire_length) - 1)
    best = current
    temperature = 100
    cooling_rate = 0.95
    while temperature > 1:
        neighbor = current + random.choice([-1, 1])
        if neighbor < 0 or neighbor >= len(wire_length):
            continue
        current_cost = wire_length[current]
        neighbor_cost = wire_length[neighbor]
        delta = neighbor_cost - current_cost
        if delta < 0:
            current = neighbor
        else:
            probability = math.exp(-delta / temperature)
            if random.random() < probability:
                current = neighbor
        if wire_length[current] < wire_length[best]:
            best = current
        temperature *= cooling_rate
    return current, best
final_layout, best_layout = simulated_annealing()
print("Final Layout:", final_layout + 1)
print("Best Layout:", best_layout + 1)
print("Minimum Wire Length:", wire_length[best_layout])
