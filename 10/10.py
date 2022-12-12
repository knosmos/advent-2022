a = open("10").read().split("\n")
x = 1
c = 1
r = 0
for op in a:
    if (c-20) % 40 == 0:
        print(x * c, c, "st")
        r += x * c
    if op == "noop":
        c += 1
        continue
    c += 1
    if (c-20) % 40 == 0:
        print(x * c, c, "mid")
        r += x * c 
    c += 1
    x += int(op.split()[1])
print(r)