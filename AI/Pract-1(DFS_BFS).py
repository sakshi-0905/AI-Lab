from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A',  'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E'],
    'E': ['C','D' ]
}

def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])

print("DFS:")
dfs(graph, 'A')
print("\nBFS:")
bfs(graph, 'A')
