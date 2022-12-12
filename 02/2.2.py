r=0
for a,b in[l.split()for l in open("2").readlines()]:
 j="ABC".find(a)
 r+=[[3,1,2][j],j+4,[8,9,7][j]]["XYZ".find(b)]
print(r)

#print(sum([(lambda j,k:[[3,1,2][j],j+4,[2,3,1][j]+6][k])("ABC".index(i[0]),"XYZ".index(i[1])) for i in[l.split()for l in open("2.in").read().split("\n")]]))