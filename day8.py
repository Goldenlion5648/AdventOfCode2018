import sys
def goDeeper(pos, arr, total, metaLengths):
    if(pos >= len(arr)):
        return total
    if(arr[pos] != 0):
        metaLengths.append(arr[pos + 1])
        return goDeeper(pos+2, arr, total, metaLengths)
    else:
        metaLengths.append(arr[pos + 1])
        isFirst = True
        extra = 2
        while arr[pos] == 0:
            size = metaLengths.pop(-1)
            for i in range(size):
                if(isFirst):
                    meta = arr[pos + 2 + i]
                else:
                    meta = arr[pos + i]
                total += meta
            isFirst = False
            pos += size + extra
            if(extra > 0):
                extra = 0

        if(pos + metaLengths[0] == len(arr)):
            total += sum(arr[-metaLengths[0]:])
            return total 
        return goDeeper(pos, arr, total, metaLengths)

a = list(map(int, input().split()))
sys.setrecursionlimit(50000)
metaTotal = 0
startPos = 0
# for i in range(a[0]):
answer = goDeeper(startPos, a, 0, [])
print(answer)
