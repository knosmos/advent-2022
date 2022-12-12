a = open("10").read().split("\n")
x = 1
c = 0
grid = [["." for i in range(40)] for _ in range(6)]
for op in a:
    if abs(c % 40 - x) <= 1:
        grid[c//40][c%40] = "#"
    if op == "noop":
        c += 1
        continue
    c += 1
    if abs(c % 40 - x) <= 1:
        grid[c//40][c%40] = "#"
    c += 1
    x += int(op.split()[1])
print(grid)
print("\n".join("".join(i) for i in grid))