a = open("7").read().split("\n")
curr = [""]
res = {}
for i in a:
    if i[0] == "$":
        if i.split()[1] == "cd":
            b = i.split()[2]
            if b == "/":
                curr = [""]
            elif b == "..":
                curr.pop(-1)
            else:
                curr.append(curr[-1] + "/" + b)
    else:
        try:
            for j in curr:
                if not j in res:
                    res[j] = 0
                res[j] += int(i.split()[0])
        except:
            pass
r = float("inf")
print(res)
rem = 70000000 - max(res.values())
print(rem)
for i in res.values():
    if rem + i >= 30000000:
        r = min(r, i)
print(r)

