i = input()
curr = [""] * 14
for j in range(len(i)):
    curr.append(i[j])
    curr.pop(0)
    if len(set(curr)) == 14 and not "" in curr:
        print(j)
        break