graph = {
    'S': [['A', 'B'], ['C']],
    'A': [['D', 'E'], ['F']],
    'B': [['G']],
    'C': [['H', 'I']]
}

cost = {
    'D': 2,
    'E': 3,
    'F': 6,
    'G': 4,
    'H': 2,
    'I': 2
}

solution = {}

def ao_star(node):
    if node not in graph:
        return cost[node]

    min_cost = float('inf')
    best_option = None

    for option in graph[node]:
        total = 0

        for child in option:
            total += ao_star(child)

        if total < min_cost:
            min_cost = total
            best_option = option

    solution[node] = best_option
    cost[node] = min_cost

    return min_cost

result = ao_star('S')

print("Minimum Cost:", result)
print("Best Solution:")

for node, children in solution.items():
    print(node, "->", children)
