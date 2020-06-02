a = []
timestep = int(input())
for i in range(31):
    k = input()
    # a.append(list(map(int, k[10:24].split(','))) + list(map(int, k[36:42].split(','))))
    a.append(list(map(int, k[10:16].split(','))) + list(map(int, k[28:34].split(','))))
# print(a)

timestep = 0
while timestep < 5:
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
    highX = 7 
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

    if(countY > 60 or countX > 60):
        board = [['.' for n in range(120)] for q in range(120)]
        for w in range(len(a)):
            # print(a[w][1] // 1000 + 60)
            # print(a[w][0] // 1000 + 60)
            board[a[w][1] // 1000 + 60][a[w][0] // 1000 + 60] = 'O'
        print('new', timestep)
        for w in board:
            print(w)
        # print(board)
    timestep += 1
# print(x)
# print(y)



