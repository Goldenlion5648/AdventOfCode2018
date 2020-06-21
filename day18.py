a = []
size = 50
for i in range(size):
    a.append(list(input()))
# print(a)

trees = []
lumber = []
for time in range(500):
    board = [row[:] for row in a]
    for y in range(size):
        for x in range(size):
            treeCount = 0
            lumberCount = 0
            for w in range(-1, 2):
                for q in range(-1, 2):
                    if w == 0 and q == 0:
                        continue
                    if(y + w < 0 or x + q < 0 or \
                        y + w >= size or x + q >= size):
                        continue
                    if a[y + w][x + q] == '|':
                        treeCount += 1
                    elif a[y + w][x + q] == '#':
                        lumberCount += 1
                    

            if a[y][x] == '.' and treeCount >= 3:
                board[y][x] = '|'
            elif a[y][x] == '|' and lumberCount >= 3:
                board[y][x] = '#'

            if a[y][x] == '#':
                if lumberCount > 0 and treeCount > 0:
                    pass
                else:
                    board[y][x] = '.'
    a = [row[:] for row in board]
    
    if(time > 422):
        # for b in board:
        #     print("".join(b))

        treeCount = 0
        lumberCount= 0
        for y in range(size):
            for x in range(size):
                if a[y][x] == '|':
                    treeCount += 1
                elif a[y][x] == '#':
                    lumberCount += 1

        trees.append(treeCount)
        lumber.append(lumberCount)
        # print(treeCount)
        # print(lumberCount)
        # print(lumberCount * treeCount)
    else:
        print(time)
    # if time > 320:
    for b in board:
        print("".join(b))

# for c in range(len(trees)):
#     print(c, trees[c], lumber[c], trees[c] * lumber[c],(trees[c] * lumber[c]) - trees[c-1] * lumber[c-1] if c != 0  else 0, trees[c] + lumber[c], sep='\t')

answer = 1000000000 - 424
print(answer % 28)