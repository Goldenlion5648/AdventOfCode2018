from collections import deque
depth = 510
depth = 4848
targetXY = (10, 10)
targetXY = (15, 700)
geo = deque([deque([0 for i in range(targetXY[0] + 1)])] * (targetXY[1] + 1))

total = 0
print(geo)

y= 0
# for y in range(targetXY[1]):
pos = 0
while pos <= targetXY[1]:
    x = 0
    while x <= targetXY[0]:
        if x == 0 and y == 0:
            geo[y][x] = 0
        # elif x == 15 and y == 700:
        elif x == targetXY[0] and pos == targetXY[1]:
            geo[y][x] = 0
        elif y == 0:
            geo[y][x] = ((x * 16807)+ depth) % 20183
            total += geo[y][x]  % 3
        elif x == 0:
            geo[y][x] = ((pos * 48271)+ depth) % 20183
            total += geo[y][x] % 3
        else:
            print('pos', pos, 'y', y, "x", x)
            # print(*geo, sep='\n')
            # print()
            # print(len(geo), len(geo[0]))
            # print(geo[y][x-1])
            # print(geo[y-1][x])
            # print(geo[y][x])
            geo[y][x] = ((geo[y][x-1] * geo[y-1][x]) + depth) % 20183
            total += geo[y][x]  % 3
        x += 1
    # if y == 1:
    #     # print('before geo', geo)
    #     geo.popleft()
    #     geo.append(deque([0 for i in range(targetXY[0] + 1)]))
    #     # print('after geo', geo)
    # else:
    y += 1
    pos += 1
print(total)


# print(geo)    
# while pos <= targetXY[1] + 1:

#     print('y', y)
#     for x in range(len(geo[pos])):
#         if x == 0 and y == 0:
#             geo[y][x] = 0
#         # elif x == 15 and y == 700:
#         elif x == targetXY[0] and pos == targetXY[1]:
#             geo[y][x] = 0
#         elif y == 0:
#             geo[y][x] = x * 16807
#             total += ((geo[y][x] + depth) % 20183) % 3
#         elif x == 0:
#             geo[y][x] = y * 48271
#             total += ((geo[y][x] + depth) % 20183) % 3
#         else:
#             print('y', y, "x", x)
#             total += ((geo[y][x-1] * geo[y-1][x] + depth) % 20183) % 3
#             geo[y][x] = geo[y][x-1] * geo[y-1][x]
#         print(y, x)
#         print(geo)
#     if y >= 1:
#         geo.popleft()
#         print('popped')
#         geo.append([0 for n in range(targetXY[0] + 2)])
#     # else:
#     y += 1
#     print('geo len', len(geo))
#     # print(geo)
#     pos += 1
# # for y in range(targetXY[1] + 1):
# #     for x in range(targetXY[0] + 1):
# #         total += ((geo[y][x] + depth) % 20183) % 3
# print(total)
#         