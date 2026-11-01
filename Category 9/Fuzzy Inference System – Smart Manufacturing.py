# Fuzzy Inference System for Smart Manufacturing

def triangle(x, a, b, c):

    if x <= a or x >= c:
        return 0

    elif x == b:
        return 1

    elif x < b:
        return (x - a) / (b - a)

    else:
        return (c - x) / (c - b)


# Input values
temperature = 65
vibration = 5

# Fuzzy membership values
temp_low = triangle(temperature, 0, 0, 50)
temp_medium = triangle(temperature, 30, 50, 70)
temp_high = triangle(temperature, 60, 100, 100)

vib_low = triangle(vibration, 0, 0, 4)
vib_medium = triangle(vibration, 2, 5, 8)
vib_high = triangle(vibration, 6, 10, 10)

# Fuzzy Rules
slow = max(temp_high, vib_high)

normal = min(temp_medium, vib_medium)

fast = min(temp_low, vib_low)

# Defuzzification using weighted average
numerator = (slow * 30 +
             normal * 60 +
             fast * 90)

denominator = slow + normal + fast

if denominator != 0:
    speed = numerator / denominator
else:
    speed = 0

# Display Results
print("Fuzzy Inference System")
print("Smart Manufacturing")

print("Temperature:", temperature)
print("Vibration:", vibration)

print("\nFuzzy Rule Results:")
print("Slow:", round(slow, 2))
print("Normal:", round(normal, 2))
print("Fast:", round(fast, 2))

print("\nRecommended Machine Speed:",
      round(speed, 2))
