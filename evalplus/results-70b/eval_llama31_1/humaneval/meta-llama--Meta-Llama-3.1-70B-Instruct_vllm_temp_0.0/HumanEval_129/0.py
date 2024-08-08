from collections import deque

def minPath(grid, k):
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(grid[0][0], [(0, 0)])])
    visited = set([(0, 0)])
    res = None

    for _ in range(k - 1):
        for _ in range(len(queue)):
            val, path = queue.popleft()
            x, y = path[-1]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    queue.append((grid[nx][ny], path + [(nx, ny)]))
                    visited.add((nx, ny))

    while queue:
        val, path = queue.popleft()
        if res is None or path[-1] < res[-1]:
            res = path

    return [grid[x][y] for x, y in res[:k]]