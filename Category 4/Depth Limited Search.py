# Searching for a Book in a Library using DLS
graph = {
    "Library": ["Floor1", "Floor2", "Floor3"],

    "Floor1": ["Science", "Literature"],
    "Floor2": ["ComputerScience", "Mathematics"],
    "Floor3": ["History", "Geography"],

    "Science": [],
    "Literature": [],

    "ComputerScience": ["AI", "DataScience"],
    "Mathematics": [],

    "History": [],
    "Geography": [],

    "AI": [],
    "DataScience": []
}


def depth_limited_search(node, goal, limit):

    print("Visiting:", node)

    if node == goal:
        return True

    if limit <= 0:
        return False

    for child in graph[node]:

        if depth_limited_search(child, goal, limit - 1):
            return True

    return False


start = "Library"
goal = "AI"
depth_limit = 3

result = depth_limited_search(start, goal, depth_limit)

if result:
    print("\nGoal Found")
else:
    print("\nGoal Not Found")
