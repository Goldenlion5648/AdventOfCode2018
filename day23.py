from collections import deque

def manhat(a, b):
    total = 0
    for i in range(3):
        total += abs(a[i] - b[i])
    return total

a = []

for i in range(1000):
    b = input()
    a.append((list(map(int, b[5:b.index('>')]
        .split(','))), int(b[b.index('r=')+2:])))
a.sort(key=lambda x: x[0][0])
# for i in a:
#     print(i)

# for x in range(-100000, 100000, 10000):
#     for y in range(-100000, 100000, 10000):
#         for z in range(-100000, 100000, 10000):
#             potentials.append([(x, y, z), 0])

potentials = dict()

for p in a:
    # for i in potentials:
    for j in range(3):
        p[]
    potentials[p]
temp = list(potentials)
temp.sort(key=lambda x: x[1])
# print(temp)

print(potentials[0][1])
print(potentials[-1][1])
print(len(potentials))
pos = 0
while pos < len(potentials):
    if potentials[pos][1] < 101:
        del potentials[pos]
    else:
        pos += 1
# 
# print(potentials.popleft())
# print(potentials[0][1])
# print(potentials[-1][1])
# print(len(potentials))
# print(potentials)


# largest = a[-1]
# radius = largest[1]
# x,y, z = largest[0]
# total = 0
# for i in a:
#     if abs(i[0][0] - x) + abs(i[0][1] - y) + abs(i[0][2] - z) <= radius:
#         total += 1
# print(total)
