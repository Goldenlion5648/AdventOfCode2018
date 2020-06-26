from collections import deque

def manhat(a, b):
    total = 0
    for i in range(4):
        total +=abs(a[i]-b[i])
    return total

a = deque()
numPoints = 1483

for i in range(numPoints):
    a.append(tuple((map(int, input().split(',')))))
# a.sort(key=lambda x: x[0])
# for i in a:
#     print(*i, sep=',')

# found = True
# b = set(a)
# print('b len', len(b))

# stars = dict()

connections = deque()

for i in range(numPoints):
    # stars[numPoints[i]] = set()
    # print(a[i])
    connections.append(set([a[i]]))
    # print(connections)
    # stars[i].add()

    for j in range(i+1, numPoints):
        if manhat(a[i], a[j]) <=3:
            # stars[numPoints[i]].add(a[j])
            connections[-1].add(a[j])
            # connections[-1].append(a[j])

print(connections)
print(len(connections))
pooled = deque()
q = 0
while q < len(connections):
    w = 0

    while w < len(connections):
        if w == q:
            w += 1
            continue
        together = connections[q].union(connections[w])
        if len(together) != len(connections[q]) + len(connections[w]):
            # pooled.append(together)
            connections[q] = together
            del connections[w]
            w = 0
        else:
            w += 1
    q += 1

print(len(connections))
# print(pooled)
# print(len(pooled))

didCombine = True
while didCombine:
    didCombine = False

# poolSize = 0
# for i in pooled:
#     poolSize += len(i)

# print(poolSize)
