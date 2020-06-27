from collections import deque

def manhat(a, b):
    total = 0
    for i in range(3):
        total += abs(a[i] - b[i])
    return total

def pointsInRange(pos, a):
    value = 0
    for i in a:
        # print(pos, i)
        if manhat(pos, i[0]) <= i[1]:
            value += 1
    # print(value)
    return value
a = []
a = deque()

for i in range(1000):
    b = input()
    a.append((list(map(int, b[5:b.index('>')]
        .split(','))), int(b[b.index('r=')+2:])))
# a.sort(key=lambda x: x[1])

# potentials = {k: v for k, v in sorted(potentials.items(), key=lambda item: item[1])}
# for i in a:
#     print(i)

# for x in range(-100000, 100000, 10000):
#     for y in range(-100000, 100000, 10000):
#         for z in range(-100000, 100000, 10000):
#             potentials.append([(x, y, z), 0])

points = dict()
#12707570 31777570 16177860
for x in range(12707470, 12707770, 10):
    for y in range(31777270, 31777870, 10):
        for z in range(16177560, 16178160, 10):
            points[(x,y,z)] = 0
# x = 14680000
# y = 33400000
# z = 17782000
         



# dim = 200000000
# step = 10000000
# for z in range(-dim, dim, step):
#     for y in range(-dim, dim, step):
#         for x in range(-dim, dim, step):
#             points[(x, y, z)] = 0
#     print(z)
# # points = dict.fromkeys([[(y, x))
# # potentials = dict()

cur = 0
#12730000 31800000 16190000
# newX = 12730000
# newY = 31800000
# newZ = 16190000
newX,newY, newZ = [12707570, 31777570, 16177860]
maxxed = [False,False,False]
subtractAmount = 100
highestNum = 913
while maxxed != [True, True, True]:
    if maxxed[0] == False:
        newX -= subtractAmount 
    if pointsInRange((newX, newY, newZ), a) < highestNum:
        maxxed[0] = True
        newX += subtractAmount
        while pointsInRange((newX, newY, newZ), a) < highestNum:
            newX -= 1
    if maxxed[1] == False:
        newY -= subtractAmount 
    if pointsInRange((newX, newY, newZ), a) < highestNum:
        maxxed[1] = True
        newY += subtractAmount 
        while pointsInRange((newX, newY, newZ), a) < highestNum:
            newY -= 1
    if maxxed[2] == False:
        newZ -= subtractAmount 
    if pointsInRange((newX, newY, newZ), a) < highestNum:
        newZ += subtractAmount 
        maxxed[2] = True
        while pointsInRange((newX, newY, newZ), a) < highestNum:
            newZ -= 1
    print(maxxed)
    print(newX, newY, newZ)
    if pointsInRange((newX, newY, newZ), a) > highestNum:
        print('found new', pointsInRange((newX, newY, newZ), a))
        break
# for i in a:
    
    # if cur % 10 == 0:
    #     print(cur)
    # cur += 1

# points = {k: v for k, v in sorted(points.items(), key=lambda item: item[1])}

# for i in points:
#     if points[i] >= 873:
#         print(i, points[i])

# # for p in a:
# #     # for i in potentials:
# #     x, y, z = p[0]
# #     rad = p[1]
# #     pos = (x-rad,y,z)

# #     if pos not in potentials:
# #         potentials[pos] = 1
# #     else:
# #         potentials[pos] += 1
# #     pos = (x+rad,y,z)

# #     if pos not in potentials:
# #         potentials[pos] = 1
# #     else:
# #         potentials[pos] += 1
# #     pos = (x,y-rad,z)
# #     if pos not in potentials:
# #         potentials[pos] = 1
# #     else:
# #         potentials[pos] += 1
# #     pos = (x,y+rad,z)
# #     if pos not in potentials:
# #         potentials[pos] = 1
# #     else:
# #         potentials[pos] += 1
# #     pos = (x,y,z+rad)
# #     if pos not in potentials:
# #         potentials[pos] = 1
# #     else:
# #         potentials[pos] += 1
# #     pos = (x,y,z-rad)
# #     if pos not in potentials:
# #         potentials[pos] = 1
# #     else:
# #         potentials[pos] += 1

# # potentials = {k: v for k, v in sorted(potentials.items(), key=lambda item: item[1])}
# # print(temp)
# # print(potentials)
# # print(potentials[0][1])
# # print(potentials[-1][1])
# # print(len(potentials))
# # pos = 0
# # while pos < len(potentials):
# #     if potentials[pos][1] < 101:
# #         del potentials[pos]
# #     else:
# #         pos += 1
# # 
# # print(potentials.popleft())
# # print(potentials[0][1])
# # print(potentials[-1][1])
# # print(len(potentials))
# # print(potentials)


# # largest = a[-1]
# # radius = largest[1]
# # x,y, z = largest[0]
# # total = 0
# # for i in a:
# #     if abs(i[0][0] - x) + abs(i[0][1] - y) + abs(i[0][2] - z) <= radius:
# #         total += 1
# # print(total)
