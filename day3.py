nums = []
board = [[0 for i in range(2000)] for j in range(2000)]
# print(board)
diction = dict.fromkeys([i+1 for i in range(1293)], 0)
for i in range(1293):
    d = list(input())
    d = d[d.index('@') + 2:]
    # d = "".join(d)
    x, y = list(map(int, "".join(d[:d.index(':')]).split(',')))
    # print(x, y)
    d = d[d.index(':') + 2:]
    d = "".join(d)
    xSize, ySize = list(map(int, d.split('x')))
    # print(xSize, ySize)
    nums.append((y,x, ySize, xSize))
for i in range(len(nums)):
    for w in range(nums[i][0],nums[i][0] + nums[i][2]):
        for t in range(nums[i][1],nums[i][1] + nums[i][3]):
            if(board[w][t] == 0):
                board[w][t] = i+1
            else:
                diction[i+1] = 5
                diction[board[w][t]] = 5

count = 0
# for i in range(len(board)):
#     for j in range(len(board[0])):
#         if(board[i][j] > 1):
#             count += 1
# print(count)

for k in diction:
    if(diction[k] != 5):
        print(k)


    # left= list(map(int, d[d.index('@') + 2: d.index(':')])).split(',')