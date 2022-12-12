a = [i.split() for i in open("2.in").read().split("\n")]
res = 0
for i in a:
    j = "ABC".index(i[0])
    k = "XYZ".index(i[1])
    res += k + 1
    if (k-1)%3 == j:
        res += 6
    elif k == j:
        res += 3
    print(res)
print(res)