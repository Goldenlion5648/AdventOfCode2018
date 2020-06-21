import copy

def printTrack(a):
    print(' ', "".join([str(i%10) for i in range(len(a[0]))]), sep='')
    for i in range(len(a)):
        print(i,*a[i], sep='')
    pass

a = []
carts = []
for i in range(150):
    a.append(list(input()))

printTrack(a)
# print(*a)
forks = {}
for i in range(len(a)):
    for j in range(len(a[i])):
        if(a[i][j] == '^'):
            carts.append([i, j, 0, 0])
        elif(a[i][j] == '>'):
            carts.append([i, j, 1, 0])
        elif(a[i][j] == 'v'):
            carts.append([i, j, 2, 0])
        elif(a[i][j] == '<'):
            carts.append([i, j, 3, 0])
        elif(a[i][j] == '\\'):
            forks[(i,j)] = '\\'
        elif(a[i][j] == '/'):
            forks[(i,j)] = '/'
        elif(a[i][j] == '+'):
            forks[(i,j)] = '+'

# print(carts)
# print(carts)
noCrash = True
counter = 0
while noCrash and counter < 20000:
    newBoard = copy.deepcopy(a)
    poses = {}
    # print(counter // 2)
    # for i in carts:
    #     pos = (i[0], i[1])
    #     if(pos not in poses):
    #         poses[pos] = 1
    #     else:
    #         print(pos)
    #         noCrash = False
    #         print('crashed 1')
    #         break

    cartNum = 0
    # for i in carts:
    while cartNum < len(carts):
        i = carts[cartNum]
        # print(i)
        # print(counter % 2 + 1, i)
        if(i[2] == 0):
            i[0] -= 1
        elif(i[2] == 2):
            i[0] += 1
        elif(i[2] == 1):
            i[1] += 1
        elif(i[2] == 3):
            i[1] -= 1
        pos = (i[0], i[1])
        # print(pos)

        if(pos not in poses):
            poses[pos] = 1
            newBoard[pos[0]][pos[1]] = 'o'
        else:
            poses[pos] += 1
            # print(pos)
            # # noCrash = False
            carts.remove(i)

            # print('crashed 2')
            print('now fake answer', pos[1], pos[0])

            # for remain in carts:
            #     if (remain[0], remain[1]) in pos:

            # continue
            continue
        
        if(pos in forks):
            # print('got to', pos, "fork")
            if(forks[pos] == '+'):
                if(i[3] == 0):
                    i[2] = (i[2] - 1) % 4
                elif(i[3] == 2):
                    i[2] = (i[2] + 1) % 4
                i[3] = (i[3] + 1) % 3

            elif(forks[pos] == '\\'):
                i[2]=(i[2] + 1) % 4 if i[2] % 2 == 1 else (i[2] - 1) % 4
            elif(forks[pos] == '/'):
                i[2]=(i[2] + 1) % 4 if i[2] % 2 == 0 else (i[2] - 1) % 4
            else:
                print('wrong')
            # print('switched to', )
        
        cartNum += 1

    # print(poses)
    for key in poses:

        if(poses[key] > 1):

            jk = 0
            while jk < len(carts):
                cur = (carts[jk][0], carts[jk][1])
                # print(cur)
                if (carts[jk][0], carts[jk][1]) == key:
                    # print('removed')
                    carts.remove(carts[jk])
                else:
                    jk += 1
            # for remain in carts:
            #     if (remain[0], remain[1]) in pos:
    if(len(carts) == 1):
        print('last cart is',carts[0])
        print("answer ", carts[0][1], ',', carts[0][0], sep ='')
        break
    print('remaining carts',len(carts))
    counter += 1
    print(counter)
    # for q in carts:
        # print(i)
    # printTrack(newBoard)
        
    carts.sort()



