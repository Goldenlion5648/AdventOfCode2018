def checkInFringe(fringe2, a):
    for i in range(len(fringe2)):
        if(a in fringe2[i]):
            return True
    return False
def allHasElements(fringe2):
    for i in range(len(fringe2)):
        if(len(fringe2[i]) == 0):
            return False
    return True


a = []
requirements = {}
finished = ''
answer = ''
for i in range(101):
    letter = input()
    a.append([letter[5:6], letter[36:37]])
a.sort()
# print(a)
for i in a:
    if i[1] not in requirements:
        requirements[i[1]] = i[0]
    else:
        requirements[i[1]] += i[0]

for i in a:
    if i[0] not in requirements:
        requirements[i[0]] = ''
sorted(requirements)
print(requirements)
# print(a)

counter = 0
posToPop = []
fringe = [[] for i in range(5)]
while len(answer) != len(requirements):
    # added = False
    for i in requirements:
        if(requirements[i] == ''):
            if(not checkInFringe(fringe, i) and i not in answer):
                for k in range(len(fringe)):
                    if(len(fringe[k]) == 0):
                        # added = True
                        for q in range(ord(i) - 4):
                            fringe[k].append(i)
                        break
                # if(added == False):
                #     while 
    posToPop = []
    changed = False
    print('fringe before', fringe)
    while changed == False:
        counter += 1
        for z in range(len(fringe)):
            if(len(fringe[z]) != 0):
                # while len(fringe[z]) != 0:
                dum = fringe[z].pop(0)
                if(len(fringe[z]) == 0):
                    posToPop.append(dum)
                    changed = True

    print("posToPop", posToPop)
    # for i in range(len(fringe)):
    #     fringe[i].sort()
    # print(fringe)
    while len(posToPop) > 0:
        cur = posToPop.pop(0)
        answer += cur
        for i in requirements:
            requirements[i] = requirements[i].replace(cur, '')

    for i in range(len(fringe)):
        fringe[i].sort()
    print(requirements)
    print(fringe)
    print(answer)
# print(requirements)
print(counter)