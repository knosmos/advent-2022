res = 0
a = open("4").read().split("\n")
for i in a:
    x,y = i.split(",")
    x = list(map(int,x.split("-")))
    y = list(map(int,y.split("-")))
    if x[0] <= y[0] and y[1] <= x[1]:
        res += 1
    elif y[0] <= x[0] and x[1] <= y[1]:
        res += 1
    elif x[0] <= y[0] <= x[1] or x[0] <= y[1] <= x[1]:
        res += 1
print(res)

r=0
for i in open("4").readlines():a,b,c,d=map(int,i.replace("-",",").split(","));r+=a<=c<=d<=b or c<=a<=b<=d or a<=c<=b or a<=d<=b
print(r)

import base64
print(base64.a85encode(
    bytes("""r=0
for i in open("4").readlines():a,b,c,d=map(int,i.replace("-",",").split(","));r+=a<=c<=d<=b or c<=a<=b<=d or a<=c<=b or a<=d<=b
return r""".encode("utf-8"))
))

(lambda i:exec(i.a85decode("E]l)`AoD]4Bcq,-+E)41DC?\\c+t5-bART+cBl7L'-n.2c/7L/?/7^n\\@;mW/DKIFD/okNBCgggb-mC5e/0ZVh.5#[\\Ch[u>+tOoe.6DQ#4^gH9@lunb4?[-rDfQt14?[+84^pN:A0>f2+CRAq@lun`+E)9C@6?\\`4?[-\\E,oZ1F=;/Y")))(__import__("base64"))