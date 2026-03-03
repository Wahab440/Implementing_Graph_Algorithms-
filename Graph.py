from collections import deque
import heapq

graph = {
    "S": [("B_top", 2), ("C", 4), ("B_bottom", 4)],
    "B_top": [("G", 5), ("C", 5)],
    "B_bottom": [("C", 1)],
    "C": [("G", 3), ("F", 3), ("G", 2)],
    "E": [("B_bottom", 4)],
    "F": [("B_bottom", 1)],
    "G": [("C", 2)]
}

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

def heuristic(n):
    return 0

def astar(start, goal):
    open_set = [(0, start, [start])]
    gscore = {start: 0}
    expanded = 0
    while open_set:
        f, current, path = heapq.heappop(open_set)
        expanded += 1
        if current == goal:
            return path, expanded, gscore[current]
        for n, w in graph[current]:
            temp_g = gscore[current] + w
            if n not in gscore or temp_g < gscore[n]:
                gscore[n] = temp_g
                fscore = temp_g + heuristic(n)
                heapq.heappush(open_set, (fscore, n, path + [n]))
    return None, expanded, float("inf")

dfs_path, dfs_exp = dfs("S", "G")
bfs_path, bfs_exp = bfs("S", "G")
astar_path, astar_exp, astar_cost = astar("S", "G")

print("DFS Path:", dfs_path)
print("DFS Expanded Nodes:", dfs_exp)
print()

print("BFS Path:", bfs_path)
print("BFS Expanded Nodes:", bfs_exp)
print()

print("A* Path:", astar_path)
print("A* Expanded Nodes:", astar_exp)
print("A* Total Cost:", astar_cost)