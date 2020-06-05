import sys

def goDeeper(pos, arr):
    total = 0
    childCount = arr[pos]
    metaCount = arr[pos + 1]
    print(arr)
    if arr[pos] == 0:
        print('pos', pos)
        print('before', total)
        total += sum(arr[pos + 2: pos+2 + metaCount])
        print('after', total)
    else:

        # for i in range(childCount):
        
        print('nest before', total)
        total += goDeeper(pos + 2, arr)
        print('nest after', total)
    return total



sys.setrecursionlimit(50000)
a = list(map(int, input().split()))
pos = 0
total = 0
metaCount = []
numNodes = []
print(goDeeper(0, a))


    # else:
        # pos += 2
