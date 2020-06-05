a = []
# timestep = int(input())
for i in range(394):
    k = input()
    a.append(list(map(int, k[10:24].split(','))) + list(map(int, k[36:42].split(','))))
    # a.append(list(map(int, k[10:16].split(','))) + list(map(int, k[28:34].split(','))))
# print(a)
step = 220000
for wq in range(step):
    for j in range(len(a)):
        a[j][0] += a[j][2]
        a[j][1] += a[j][3]
    # x[a[j][0]] += 1
    # y[a[j][1]] += 1

timestep = step
while timestep < step + 1000000:
    x = {}
    y = {}
    for j in range(len(a)):
        a[j][0] += a[j][2]
        a[j][1] += a[j][3]
        if(a[j][0] not in x):
            x[a[j][0]] = 0
        if(a[j][1] not in y):
            y[a[j][1]] = 0
        x[a[j][0]] += 1
        y[a[j][1]] += 1
    highX = 10 
    highY = 7 
    countX = 0
    countY = 0
    posDict = {}
    for k in x:
        if x[k] >= highX:
            countX += x[k]

    for k in y:
        if y[k] > highY:
            countY += y[k]
        # highY = max(highY, y[k])

    if(countY > 4 or countX > 4):
        a.sort(key=lambda x: x[1]) 
        minYPos = a[0][1]
        a.sort()
        minXPos = a[0][0]
        consecCount = 0
        highConsec = 0
        it = 0
        while it < len(a) - 1:
            if(a[it][0] + 1 == a[it + 1][0]):
                consecCount += 1
                highConsec = max(highConsec, consecCount)
            else:
                consecCount = 0
            it += 1
        if(highConsec > 4):
            # print("minXPos", minXPos)
            # print("minYPos", minYPos)
            modNum = 120
            board = [['.' for n in range(modNum)] for q in range(modNum)]
            print(timestep)
            for w in range(len(a)):
                # print(a[w][1] // 1000 + 60)
                # print(a[w][0] // 1000 + 60)
                board[(a[w][1] - minYPos) % modNum][(a[w][0] - minXPos) % modNum] = '#'
            # print('new', timestep)
            for w in board:
                print(*w, sep='')
            # print(board)
    timestep += 1
# print(x)
# print(y)



