def dfs(graph, start, visited):
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

# Read input
n = int(input())
m = int(input())

# Initialize graph
graph = {i: [] for i in range(1, n+1)}

# Read edges
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

# Read start node
start = int(input())

# Perform DFS
visited = {i: False for i in range(1, n+1)}
dfs(graph, start, visited)

# Find unreachable nodes
unreachable = [node for node in range(1, n+1) if not visited[node]]

# Print result
print(*sorted(unreachable))
