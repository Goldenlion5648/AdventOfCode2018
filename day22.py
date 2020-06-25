from collections import deque
depth = 510
targetXY = (10, 10)
geo = deque([deque([0 for i in range(targetXY[0] + 1)]) for j in range(targetXY[1] + 1)])
geo[0][0] = 0


for y in range(len(geo)):
    for x in range(len(geo[y])):
        if x == 0 and y == 0:
            geo[y][x] = 0
        # elif x == 15 and y == 700:
        elif x == targetXY[0] and y == targetXY[1]:
            geo[y][x] = 0
        elif y == 0:
            geo[y][x] = x * 16807
        elif x == 0:
            geo[y][x] = y * 48271
        else:
            geo[y][x] = geo[y][x-1] * geo[y-1][x]

total = 0
for y in range(targetXY[1] + 1):
    for x in range(targetXY[0] + 1):
        total += ((geo[y][x] + depth) % 20183) % 3
print(total)
        