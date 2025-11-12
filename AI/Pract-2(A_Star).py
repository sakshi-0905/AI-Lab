import heapq

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start, goal = (0, 0), (4, 4)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    open_set = [(heuristic(start, goal), 0, start, [start])]
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            x, y = current[0] + dx, current[1] + dy
            if 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0:
                next_node = (x, y)
                if next_node not in visited:
                    heapq.heappush(open_set, (g + 1 + heuristic(next_node, goal), g + 1, next_node, path + [next_node]))
    return None

path = astar(maze, start, goal)

if path:
    print("A* Path:", path)
    for x, y in path:
        maze[x][y] = '*'
    print("\nMaze with Path:")
    for row in maze:
        print(' '.join(str(cell) if cell != '*' else '*' for cell in row))
else:
    print("No path found.")
