# # def wrapAround(xPos, yPos, board):
# #     e = 0
# #     for i in range(yPos -1, yPos + 2):
# #         for j in range(xPos -1, xPos + 2):
# #             board[i][j] = 

# # d= dict.fromkeys([chr(i) for i in range(65, 65 + 26)], 0)
# # e= dict.fromkeys([chr(i) for i in range(97, 97 + 26)], 0)
# # g = [chr(i) for i in range(65, 65 + 26)]
# # dum= [chr(i) for i in range(97, 97 + 26)]
# g = g + dum
# print(g)
# points = {}
# x = {}
# y = {}
# d.update(e)
# # print(d)
board = [[0 for i in range(365)] for j in range(365)]
c= []
for i in range(50):
    c.append(tuple(map(int, input().split(','))))

xPoints = {}
c.sort()
for i in c:
    xPoints[(i)] = 1

c.sort(key = lambda x: x[1])
yPoints = {}
for i in c:
    yPoints[(i)] = 1
# print(c)
print(xPoints)
print()
print(yPoints)

pointID = 65
for i in xPoints:
    board[i[0]][i[1]] = chr(pointID)
    pointID += 1
    if(pointID == 91):
        pointID = 97

for i in board:
    print(i)




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

