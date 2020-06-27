from collections import deque

def manhat(a, b):
    total = 0
    for i in range(2):
        total += abs(a[i] - b[i])
    return total
# board = deque([deque([0 for i in range(-30, 380)]) for j in range(-30, 380)])
offset = 0
dim = 404
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

edgePoints = set()
for y in range(offset, len(board)):
    for x in range(offset, len(board[0])):
        isTie = False
        closet = (1000000, 1000000)
        for key in points:
            man1 = manhat(closet, (y,x))
            man2 = manhat(key, (y,x))
            # print(y, x, man1, man2)

            if man2 < man1:
                closet = key
                # print('new closet', closet)
                isTie = False
            elif man1 == man2:
                isTie = True
        if isTie == False:
            # print('adding', y, x, key )
            # print(points)
            board[y][x] = closet
            points[closet] += 1
            # if x == 0 or y == 0 or x == len(board)-1 or y == len(board)-1:
            #     points.pop(closet)
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


# dist = 10
# for p in points:
#     for x in range(-dist, dist):
#         for y in range(-dist, dist):
#             if p[1] + y < 0 or p[0] + x < 0 or p[1] + y >= len(board) or \
#             p[0] + x >= len(board[0]):
#                 continue
#             if board[p[1]+y][p[0]+x] == 0:
#                 board[p[1]+y][p[0]+x] = p
#                 points[p] += 1
#             elif manhat(board[p[1]+y][p[0]+x], p) == manhat(board[board[p[1]][p[0]][1]][board[board[p[1]][p[0]][0]]], board[p[1]+y][p[0]+x]):
#                 points[board[board[p[1]+y][p[0]+x]]] -= 1

#             elif manhat(board[p[1]+y][p[0]+x], p) < manhat(board[p[1]][p[0]], board[p[1]+y][p[0]+x]):
#                 # print(board[p[1]+y][p[0]+x])
#                 points[board[p[1]+y][p[0]+x]] -= 1
#                 points[p] += 1
#                 board[p[1]+y][p[0]+x] = p






# xPoints = {}
# c.sort()
# for i in c:
#     xPoints[(i)] = 1

# c.sort(key = lambda x: x[0]+x[1])
# for i in c:
#     print(i)

# yPoints = {}
# for i in c:
#     yPoints[(i)] = 1
# print(c)
# print(xPoints)
# print()
# print(yPoints)




# # for k in c:
# #     points[k] = 0
# # print(points)

# count = 0
# for k in c:
#     board[k[1]][k[0]] = g[count]
#     count += 1
#     # x[k[0]] = 0
#     # y[k[1]] = 0

# print(board)

# # print(x)
# # print(y)
# # c.sort()
# # print(*c)

