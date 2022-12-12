r = 0
j = open("3").read().split("\n")
for i in range(len(j)//3):
    a,b,c = j[i*3:i*3+3]
    k = list(set(a) & set(b) & set(c))[0]
    if k.isupper():
        r += ord(k) - 64 + 26
    else:
        r += ord(k) - 96
print(r)



