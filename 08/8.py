a = [list(map(int, i)) for i in open("8").read().split()]
print(a)
res = 0
for row in range(len(a)):
    for col in range(len(a[0])):
        # up
        up = 0
        for i in range(row-1, -1, -1):
            if a[i][col] < a[row][col]:
                up += 1
            else:
                up += 1
                break

        # down
        down = 0
        for i in range(row+1, len(a)):
            if a[i][col] < a[row][col]:
                down += 1
            else:
                down += 1
                break

        # left
        left = 0
        for i in range(col-1, -1, -1):
            if a[row][i] < a[row][col]:
                left += 1
            else:
                left += 1
                break

        # right
        right = 0
        for i in range(col+1, len(a[0])):
            if a[row][i] < a[row][col]:
                right += 1
            else:
                right += 1
                break
        print(up, down, left, right)
        res = max(res, up * down * left * right)
print(res)
'''
g = [[0] * len(a[0]) for _ in range(len(a))]
for r in range(len(g)):
    curr = -1
    for col in range(len(g[0])):
        if a[r][col] > curr:
            curr = a[r][col]
            g[r][col] = 1
    curr = -1
    for col in range(len(g[r]) - 1, -1, -1):
        if a[r][col] > curr:
            curr = a[r][col]
            g[r][col] = 1
for col in range(len(g[0])):
    curr = -1
    for row in range(len(g)):
        if a[row][col] > curr:
            curr = a[row][col]
            g[row][col] = 1
    curr = -1
    for row in range(len(g) - 1, -1, -1):
        if a[row][col] > curr:
            curr = a[row][col]
            g[row][col] = 1
print(g)
print(sum(sum(i) for i in g))
'''
