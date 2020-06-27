from collections import deque

def manhat(a, b):
    total = 0
    for i in range(2):
        total += abs(a[i] - b[i])
    return total
# board = deque([deque([0 for i in range(-30, 380)]) for j in range(-30, 380)])
offset = 0
dim = 370
board = deque([deque([0 for i in range(0- offset, dim)]) for j in range(0- offset, dim)])
# board[5][6] = 7
# for i in board:
#     print(i)
# c= []
points = dict()
for i in range(50):
# for i in range(6):
    # c.append(tuple(map(int, input().split(','))))
    points[tuple(map(int, input().split(',')))] = 0

coordCount = 0
edgePoints = set()
for y in range(offset, len(board)):
    for x in range(offset, len(board[0])):
        isTie = False
        closet = (1000000, 1000000)
        curSum = 0
        for key in points:
            man1 = manhat(closet, (y,x))
            man2 = manhat(key, (y,x))
            # print(y, x, man1, man2)
            curSum += man2
            if man2 < man1:
                closet = key
                # print('new closet', closet)
                isTie = False
            elif man1 == man2:
                isTie = True
        if curSum < 10000:
            coordCount += 1
        # if isTie == False:
        #     # print('adding', y, x, key )
        #     # print(points)
        #     board[y][x] = closet
        #     points[closet] += 1

    print(y)
points = {k: v for k, v in sorted(points.items(), key=lambda item: item[1])}
print(points)
for i in board[0]:
    edgePoints.add(i)
for i in board[-1]:
    edgePoints.add(i)

dum = deque([i[0] for i in board])
for col in dum:
    edgePoints.add(col)
dum = deque([i[-1] for i in board])
for col in dum:
    edgePoints.add(col)
print(edgePoints)
# for i in board:
#     print(i)


pos = 0
answer = dict()
for i in points:
    if i not in edgePoints:
        answer[i] = points[i]
answer = {k: v for k, v in sorted(answer.items(), key=lambda item: item[1])}

print(answer)
print(coordCount)
