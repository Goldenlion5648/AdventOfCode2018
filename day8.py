import sys
def goDeeper(pos, arr, total, numNodes, metaLengths):
    # if(pos >= len(arr)):
    #     print('pos', pos)
    #     return total
    endSum = sum(metaLengths)
    if(pos + endSum >= len(arr) - 1):
        print('end exit')
        print('end pos', pos)
        print('end sum', endSum)
        for i in range(sum(metaLengths), -1, -1):
            total += arr[-i]
            print('ending added', arr[-i])
            print('new total', total)
        # total += sum(arr[-sum(metaLengths):])
        return total

    if(arr[pos] != 0):
        numNodes.append(arr[pos])
        metaLengths.append(arr[pos + 1])
        print('appended', arr[pos+1])
        return goDeeper(pos+2, arr, total, numNodes, metaLengths)
    else:
        # isFirst = True
        # keepGoing = True
        metaLengths.append(arr[pos + 1])
        extra = 2
        nodeCount = numNodes.pop(-1)
        for r in range(nodeCount):
            size = metaLengths.pop(-1)
            for i in range(size):
                meta = arr[pos + extra + i]

                total += meta
                print('added', meta)
                print('total', total)
            # isFirst = False
            pos += size + extra
            extra = 0
        print('bottom', metaLengths)
        # print('metaLengths', metaLengths)
        # print('pos2', pos)
        
        return goDeeper(pos, arr, total, numNodes, metaLengths)

a = list(map(int, input().split()))
print('len a', len(a))
sys.setrecursionlimit(50000)
metaTotal = 0
startPos = 0
# for i in range(a[0]):
answer = goDeeper(startPos, a, 0, [])
print(answer)
