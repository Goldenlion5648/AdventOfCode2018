a = []
for i in range(1134):
    a.append(input())
a.sort()
# print(a)
d = {}
g = 'Guard'
# a = a[:5]

for j in range(len(a)):
    if(g in a[j]):
        num = a[j][26:]
        if(num not in d):
            d[num] = [0 for c in range(60)]

print(d)
i = 0
while i < len(a):
    # date = a[i][:11]
    # print(date)
    if g in a[i]:
        gNum = a[i][26:]
        i += 1
        if(i >= len(a)):
            break
        while i < len(a) -1 and g not in a[i]:
            # print(i)
            # print(a[i])
            # print(a[i+1])
            for w in range(int(a[i][15:17]), int(a[i+1][15:17])):
                d[gNum][w] += 1
            i += 2
        # i += 1
    else:
        if(i == len(a) - 1):
            break
        print(i, 'wrong')
print(d)
# print()
total = 0
maxVal = -1
ans = 0
gID = 0
highest = -1
for x in d:
    if max(d[x]) > highest:
        highest = max(d[x])
        gID = x
        print(highest)
        print(gID)
print(d[gID].index(highest))

    # maxVal = max(d[x])
    # if(d[x].count(maxVal) == 1):
    #     print(x, maxVal)
    #     print(d[x].index(maxVal))
    # t = sum(d[x])
    # # print(x, t)
    # if(t > total):
    #     total = t
    #     print(total)
    #     print(x)
    #     ans = x

# print(d[ans].index(max(d[ans])))
# print(max(d[ans]))

# for x in d:

# print(d)


    # if date not in d:
    #     d[date] = []
    # print(i)

