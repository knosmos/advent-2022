from collections import deque
g = list(map(list, open("12","r").read().split("\n")))

# find S and E characters
viable = []
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] == "S":
            x, y = i, j
            g[i][j] = "a"
        if g[i][j] == "E":
            ex, ey = i, j
            g[i][j] = "z"
        if g[i][j] == "a":
            viable.append((i, j))
# Run BFS
opt = float("inf")
for x, y in viable:
    q = deque([(x, y, 0)])
    visited = set()
    while q:
        x, y, d = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if (x, y) == (ex, ey):
            opt = min(opt, d)
            break
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= x + i < len(g) and 0 <= y + j < len(g[0]):
                char = ord(g[x + i][y + j])
                if char <= ord(g[x][y]) + 1:
                    q.append((x + i, y + j, d + 1))
print(opt)