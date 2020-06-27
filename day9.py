from collections import deque
# a = input()
# maxMarbles = int(a[33:38])
# playerCount = int(a[:a.index(' ')])
# maxMarbles = 71863
# playerCount = 493
maxMarbles = 7186300
playerCount = 493



print(maxMarbles)
print(playerCount)

# marbles = [0]
curPlayer = 1
scores = {}
i = 1
insertPos = 1
marbles = deque([0])
while i <= maxMarbles:
    if(i % 23 == 0 and i != 0):
        if(curPlayer not in scores):
            scores[curPlayer] = i
        else:
            scores[curPlayer] += i
        insertPos -= 9

        if(insertPos < 0):
            insertPos = len(marbles) + insertPos
        try:
            scores[curPlayer] += marbles[insertPos]
            del marbles[insertPos]
        except:
            print('error on',insertPos)
            print('len marbles',len(marbles))
            break
    else:
        marbles.insert(insertPos, i)
    if(insertPos == len(marbles) - 1):
        insertPos = 1
    elif(insertPos == len(marbles) - 2):
        insertPos = 0
    else:
        insertPos += 2
    if(insertPos >= len(marbles)):
        insertPos = (insertPos % len(marbles))
    # print(curPlayer, marbles)
    # if(len(marbles) > 650745):
    #     print('marbles len', len(marbles))
    # if(insertPos > 650745):
    #     print('insertPos', insertPos)
    # print(marbles)
    i += 1
    curPlayer += 1
    if i % 1000 == 0:
        print(i)
    if(curPlayer == playerCount + 1):
        curPlayer = 1
# scores[10] = 2
# print(scores)
a = max(scores.items(), key=lambda x: x[1])
print(a[1])