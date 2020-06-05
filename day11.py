dim = 300
serial = 9995
board = [[0 for i in range(dim)] for j in range(dim)]
for y in range(dim):
    for x in range(dim):
        # if(x != 32 or y != 44):
        #     continue
        rack = x + 11
        # print(rack)
        rack *= (y + 1)
        # print(rack)
        rack += serial
        # print(rack)
        rack *= x + 11
        # print(rack)
        if(len(str(rack)) > 2):
            rack = int(str(rack)[-3])
        else:
            rack = 0
        # print(rack)
        rack -= 5
        # print(rack)
        board[y][x] = rack

totals = {}
# xTotals = []
# yTotals = list(map (sum, zip(*board)))

# for i in board:
#     xTotals.append(sum(i))

# for k in range(dim):
#     print(xTotals[k], yTotals[k])

for y in range(dim):
    for x in range(dim):
        t = 0
        # for i in range(min(3, dim-y)):
            # for j in range(min(3, dim-x)):
        size2 = min(30, min(dim-x, dim-y))
        # size = min(3, min(dim-x, dim-y))
        for size in range(size2):
            t = 0
            for i in range(size):
                for j in range(size):
                    t += board[y + i][x + j]
            if(t > 0):
                totals[(x, y, size)] = t

high = -10
pos = 0
for i in totals:
    if(totals[i] >= high):
        high = max(high, totals[i])
        pos = i
        # print('high', high, 'pos', pos)

# print(max(totals))
print(high)
print(pos)
# for i in board:
#     print(*i, sep='\t')

