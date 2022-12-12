x = [
    ["W","R","T","G"],
    ["W","V","S","M","P","H","C","G"],
    ["M","G","S","T","L","C"],
    ["F","R","W","M","D","H","J"],
    ["J","F","W","S","H","L","Q","P"],
    ["S","M","F","N","D","J","P"],
    ["J","S","C","G","F","D","B","Z"],
    ["B","T","R"],
    ["C","L","W","N","H"]
]
for i in open("5").read().split("\n"):
    _,a,_,b,_,c = i.split()
    a,b,c = int(a),int(b),int(c)
    n = []
    for i in range(a):
        n.append(x[b-1].pop(0))
    x[c-1] = n + x[c-1]
print("".join(i[0] for i in x))