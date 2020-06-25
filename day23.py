a = []

for i in range(1000):
    b = input()
    a.append((list(map(int, b[5:b.index('>')].split(','))), int(b[b.index('r=')+2:])))
a.sort(key=lambda x: x[0][0])
for i in a:
    print(i)

largest = a[-1]
radius = largest[1]
x,y, z = largest[0]
total = 0
for i in a:
    if abs(i[0][0] - x) + abs(i[0][1] - y) + abs(i[0][2] - z) <= radius:
        total += 1
# print(total)
