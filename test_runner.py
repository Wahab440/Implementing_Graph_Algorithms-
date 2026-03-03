import yaml
from collections import deque
import heapq

with open("graph_search_tests.yaml", "r") as f:
    data = yaml.safe_load(f)

graph = data["graph"]["edges"]

def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()
    expanded = 0
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        expanded += 1
        if node == goal:
            return path, expanded
        for n, _ in reversed(graph[node]):
            if n not in visited:
                stack.append((n, path + [n]))
    return None, expanded

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    expanded = 0
    while queue:
        node, path = queue.popleft()
        expanded += 1
        if node == goal:
            return path, expanded
        for n, _ in graph[node]:
            if n not in visited:
                visited.add(n)
                queue.append((n, path + [n]))
    return None, expanded

def astar(start, goal):
    pq = [(0, start, [start])]
    gscore = {start: 0}
    expanded = 0
    while pq:
        cost, node, path = heapq.heappop(pq)
        expanded += 1
        if node == goal:
            return path, expanded, cost
        for n, w in graph[node]:
            new_cost = cost + w
            if n not in gscore or new_cost < gscore[n]:
                gscore[n] = new_cost
                heapq.heappush(pq, (new_cost, n, path + [n]))
    return None, expanded, float("inf")

def run_tests():
    for test in data["tests"]:
        algo = test["algorithm"]
        start = test["start"]
        goal = test["goal"]

        if algo == "DFS":
            path, expanded = dfs(start, goal)
            cost = None
        elif algo == "BFS":
            path, expanded = bfs(start, goal)
            cost = None
        else:
            path, expanded, cost = astar(start, goal)

        print("Test:", test["name"])
        print("Path:", path)
        print("Expanded:", expanded)
        if cost is not None:
            print("Cost:", cost)
        print("-" * 40)

run_tests()
