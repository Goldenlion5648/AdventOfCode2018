

a = list(map(int, input().split()))
pos = 0
total = 0
childCounts = []
metaCounts = []
childPos = -1
depth = 0
while pos < len(a):
    if(len(metaCounts) >depth):
        

    elif a[pos] == 0:
        metaCounts.append(a[pos + 1])
        # while len(metaCounts) > depth:
        for i in range(metaCounts[-1]):
            metaNum = a[pos + 2]
            print('added', metaNum, 'at', pos + 2)
            total += metaNum
            pos += 1
        pos += 2
        depth -= 1
        print("depth", depth)
        metaCounts.pop(-1)
        childCounts.pop(-1)
        print(metaCounts)
    else:
        depth += 1
        childCounts.append(a[pos])
        metaCounts.append(a[pos + 1])
        pos += 2
    print("pos", pos)

print(total)
    # if(len(childCounts))


