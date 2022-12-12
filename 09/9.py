t = [[0,0] for i in range(10)]
vis = {(0,0)}
for i in open("9").read().split("\n"):
    d, k = i.split()
    k = int(k)
    for i in range(k):
        if d == "U":
            t[0][1] -= 1
        elif d == "D":
            t[0][1] += 1
        elif d == "L":
            t[0][0] -= 1
        elif d == "R":
            t[0][0] += 1
        for j in range(1,10):
            if abs(t[j-1][0] - t[j][0]) > 1:
                t[j][0] += 1 if t[j-1][0] > t[j][0] else -1
                if abs(t[j-1][1] - t[j][1]) == 1:
                    t[j][1] += 1 if t[j-1][1] > t[j][1] else -1
            if abs(t[j-1][1] - t[j][1]) > 1:
                t[j][1] += 1 if t[j-1][1] > t[j][1] else -1
                if abs(t[j-1][0] - t[j][0]) == 1:
                    t[j][0] += 1 if t[j-1][0] > t[j][0] else -1
        #print(t[-1])
        vis.add(tuple(t[9]))
for i in range(1000):
    for j in range(1,10):
        if abs(t[j-1][0] - t[j][0]) > 1:
            t[j][0] += 1 if t[j-1][0] > t[j][0] else -1
            if abs(t[j-1][1] - t[j][1]) == 1:
                t[j][1] += 1 if t[j-1][1] > t[j][1] else -1
        if abs(t[j-1][1] - t[j][1]) > 1:
            t[j][1] += 1 if t[j-1][1] > t[j][1] else -1
            if abs(t[j-1][0] - t[j][0]) == 1:
                t[j][0] += 1 if t[j-1][0] > t[j][0] else -1
    #print(t[-1])
    vis.add(tuple(t[9]))
#print(vis)
# print vis on a grid
for i in range(-20,20):
    for j in range(-20,20):
        if (i,j) in vis:
            print("#", end="")
        else:
            print(".", end="")
    print()

print(len(vis))