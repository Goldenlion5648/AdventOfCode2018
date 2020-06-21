from collections import deque
startNum = 37
numList = list(str(startNum))

poses = [i for i in range(len(numList))]

# print(numList)
print("poses", poses)
print("start", numList)
# searchKey = list(map(int, list(str(5371393113))))
# print(searchKey)
# print('a', a)
start = 1800000
part2Key = 513401
# start = 2018
numList = deque(list(map(int, numList)))
for j in range(start + 11):
    total = 0
    for k in range(len(poses)):
        total += numList[poses[k]]

    # a = list(map(int, numList))
    string = str(total)
    for r in range(len(string)):
        numList.append(int(string[r]))
    # numList = deque(list(map(int, numList)))
    # print(numList)
    for i in range(len(poses)):
        poses[i] = (poses[i] + numList[poses[i]] + 1) % len(numList)
    # print(poses)
    # if j % 1000 == 0:
        # print(j)
# print(numList)
sVersion = "".join(list(map(str, numList)))
print(sVersion.index(str(part2Key)))
# answer = ''
# for i in range(10):
#     answer += str(numList[start + i])

# print(answer)
# print(numList.index([5,9,4,1,4]))

# i = 0
# while i < len(numList):
#     pos =0
#     while numList[i + pos] == searchKey[pos]:
#         pos += 1
#         if(pos == len(searchKey)):
#             print(i)
#             i = len(numList)
#             break
#     i += 1