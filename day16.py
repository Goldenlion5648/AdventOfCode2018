from itertools import permutations
before = []
instructs = []
after = []
combined = []

entries = 3188 // 4
codeFinals = dict.fromkeys([j for j in range(16)])
codeMap = {
"addr": [],
"addi": [],
"mulr": [],
"muli": [],
"banr": [],
"bani": [],
"borr": [],
"bori": [],
"setr": [],
"seti": [],
"gtir": [],
"gtri": [],
"gtrr": [],
"eqir": [],
"eqri": [],
"eqrr": [] 
}

answerMap = {
"addr": -1,
"addi": -1,
"mulr": -1,
"muli": -1,
"banr": -1,
"bani": -1,
"borr": -1,
"bori": -1,
"setr": -1,
"seti": -1,
"gtir": -1,
"gtri": -1,
"gtrr": -1,
"eqir": -1,
"eqri": -1,
"eqrr": -1 
}


# print(codes)

for i in range(entries):
    w = input()
    nums = w[9:-1].split(', ')
    # print(nums)
    before.append(list(map(int, nums)))
    w = input()
    instructs.append(list(map(int, w.split())))

    w = input()
    after.append(list(map(int,w[9:-1].split(', '))))
    dum = input()
    combined.append((instructs[-1], before[-1], after[-1]))

# for i in range(entries):
#     print("before", before[i])
#     print("instructs", instructs[i])
#     print("after", after[i])


threeOrMoreCount = 0
for i in range(entries):
    potentialCount = 0
    if before[i][instructs[i][1]] + before[i][instructs[i][2]] == after[i][instructs[i][3]]:
        potentialCount += 1
        codeMap['addr'].append(instructs[i][0])
    if before[i][instructs[i][1]] + instructs[i][2] == after[i][instructs[i][3]]:
        potentialCount += 1
        codeMap['addi'].append(instructs[i][0])
    #MULTiply
    if before[i][instructs[i][1]] * before[i][instructs[i][2]] == after[i][instructs[i][3]]:
        potentialCount += 1
        codeMap['mulr'].append(instructs[i][0])
    if before[i][instructs[i][1]] * instructs[i][2] == after[i][instructs[i][3]]:
        potentialCount += 1
        codeMap['muli'].append(instructs[i][0])
    #BITWise And
    if before[i][instructs[i][1]] & before[i][instructs[i][2]] == after[i][instructs[i][3]]:
        potentialCount += 1
        codeMap['banr'].append(instructs[i][0])
    if before[i][instructs[i][1]] & instructs[i][2] == after[i][instructs[i][3]]:
        potentialCount += 1
        codeMap['bani'].append(instructs[i][0])
    #OR
    if before[i][instructs[i][1]] | before[i][instructs[i][2]] == after[i][instructs[i][3]]:
        potentialCount += 1
        codeMap['borr'].append(instructs[i][0])
    if before[i][instructs[i][1]] | instructs[i][2] == after[i][instructs[i][3]]:
        potentialCount += 1
        codeMap['bori'].append(instructs[i][0])
    #assignment
    if before[i][instructs[i][1]] == after[i][instructs[i][3]]:
        potentialCount += 1
        codeMap['setr'].append(instructs[i][0])
    if instructs[i][1] == after[i][instructs[i][3]]:
        potentialCount += 1
        codeMap['seti'].append(instructs[i][0])
    #greater
    if instructs[i][1] > before[i][instructs[i][2]] and after[i][instructs[i][3]] == 1:
        potentialCount += 1
        codeMap['gtir'].append(instructs[i][0])
    elif instructs[i][1] <= before[i][instructs[i][2]] and after[i][instructs[i][3]] == 0:
        potentialCount += 1
        codeMap['gtir'].append(instructs[i][0])
    if before[i][instructs[i][1]] > instructs[i][2] and after[i][instructs[i][3]] == 1:
        potentialCount += 1
        codeMap['gtri'].append(instructs[i][0])
    elif before[i][instructs[i][1]] <= instructs[i][2] and after[i][instructs[i][3]] == 0:
        potentialCount += 1
        codeMap['gtri'].append(instructs[i][0])
    if before[i][instructs[i][1]] > before[i][instructs[i][2]] and after[i][instructs[i][3]] == 1:
        potentialCount += 1
        codeMap['gtrr'].append(instructs[i][0])
    elif before[i][instructs[i][1]] <= before[i][instructs[i][2]] and after[i][instructs[i][3]] == 0:
        potentialCount += 1
        codeMap['gtrr'].append(instructs[i][0])
    #equality
    if instructs[i][1] == before[i][instructs[i][2]] and after[i][instructs[i][3]] == 1:
        potentialCount += 1
        codeMap['eqir'].append(instructs[i][0])
    elif instructs[i][1] != before[i][instructs[i][2]] and after[i][instructs[i][3]] == 0:
        potentialCount += 1
        codeMap['eqir'].append(instructs[i][0])
    if before[i][instructs[i][1]] == instructs[i][2] and after[i][instructs[i][3]] == 1:
        potentialCount += 1
        codeMap['eqri'].append(instructs[i][0])
    elif before[i][instructs[i][1]] != instructs[i][2] and after[i][instructs[i][3]] == 0:
        potentialCount += 1
        codeMap['eqri'].append(instructs[i][0])
    if before[i][instructs[i][1]] == before[i][instructs[i][2]] and after[i][instructs[i][3]] == 1:
        potentialCount += 1
        codeMap['eqrr'].append(instructs[i][0])
    elif before[i][instructs[i][1]] != before[i][instructs[i][2]] and after[i][instructs[i][3]] == 0:
        potentialCount += 1
        codeMap['eqrr'].append(instructs[i][0])


    if potentialCount >= 3:
        threeOrMoreCount += 1
print(threeOrMoreCount)

# for key in codeMap:
#     codeMap[key].sort()
#     print(key, codeMap[key])
#     print()

# print(codeMap['setr'].count(11))
# print(codeMap['setr'].count(13))
# while True:
assigned = []
for key in codeMap:
    codeMap[key] = set(codeMap[key])
    print(key, codeMap[key])

for z in range(30):
    for key in codeMap:
        if len(codeMap[key]) == 1:
            value = list(codeMap[key])[0]
            answerMap[key] = value
            assigned.append(value)
            print("assigned", assigned)
            for w in codeMap:
                if value in codeMap[w]:
                    codeMap[w].remove(value)
for key in answerMap:
    print(key, answerMap[key])

# for p in range(2):
#     for j in range(16):
#         seen = False
#         ans = ''
#         for key in codeMap:
#             if len(assigned) > 0:
#                 # print('before', key, codeMap[key])
#                 codeMap[key] = [x for x in codeMap[key] if x not in assigned]
#                 # print('after', key, codeMap[key])
#             if(j in codeMap[key]):
#                 if seen == False:
#                     seen = True
#                     ans = key
#                 else:
#                     seen = False
#                     break
#         if seen == True:
#             answerMap[ans] = j
#             assigned.append(j)
#             print('\n\nanswer\n\n',answerMap)






# combined.sort()
# print(*combined, sep='\n')
# registers = [0,0,0,0]
# print(codeMap)
# for k in range(16):
#     # print(codeMap[j])
#     maxPos = -1
#     maxOccurences = -1
#     pos = 0
#     for j in codeMap:
#         c = codeMap[j].count(k)
#         print(c, '\t', end='')
#         if(c > maxOccurences):
#             maxOccurences = c
#             maxPos = pos
#         pos += 1
#     print()
#     # print(max(set(codeMap[j]), key=codeMap[j].count))
#     print(codeMap[k].key(), k)
