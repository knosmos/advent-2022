m = [
    [[80], "i*5", 2, 4, 3, 0],
    [[75, 83, 74], "i+7", 7, 5, 6, 0],
    [[86, 67, 61, 96, 52, 63, 73], "i+5", 3, 7, 0, 0],
    [[85, 83, 55, 85, 57, 70, 85, 52], "i+8", 17, 1, 5, 0],
    [[67, 75, 91, 72, 89], "i+4", 11, 3, 1, 0],
    [[66, 64, 68, 92, 68, 77], "i*2", 19, 6, 2, 0],
    [[97, 94, 79, 88], "i*i", 5, 2, 7, 0],
    [[77, 85], "i+6", 13, 4, 0, 0]
]
'''
m = [
    [[79,98],"i*19",23,2,3,0],
    [[54,65,75,74],"i+6",19,2,0,0],
    [[79,60,97],"i*i",13,1,3,0],
    [[74],"i+3",17,0,1,0]
]
'''
#mod = 23*19*13*17
mod = 2 * 7 * 3 * 17 * 11 * 19 * 5 * 13

for r in range(10000):
    for mon in m:
        for i in mon[0]:
            i = eval(mon[1])
            i %= mod
            if i % mon[2] == 0:
                m[mon[3]][0].append(i)
            else:
                m[mon[4]][0].append(i)
        mon[5] += len(mon[0])
        mon[0] = []
a = sorted([i[5] for i in m])
print(a[-1] * a[-2])