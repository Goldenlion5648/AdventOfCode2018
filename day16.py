before = []
instructs = []
after = []
entries = 3188 // 4
codes = [[] for i in range(16)]
print(codes)

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

# for i in range(entries):
#     print("before", before[i])
#     print("instructs", instructs[i])
#     print("after", after[i])


threeOrMoreCount = 0
for i in range(entries):
    potentialCount = 0
    if before[i][instructs[i][1]] + before[i][instructs[i][2]] == after[i][instructs[i][3]]:
        potentialCount += 1
        codes[0].append()
    if before[i][instructs[i][1]] + instructs[i][2] == after[i][instructs[i][3]]:
        potentialCount += 1
    if before[i][instructs[i][1]] * before[i][instructs[i][2]] == after[i][instructs[i][3]]:
        potentialCount += 1
    if before[i][instructs[i][1]] * instructs[i][2] == after[i][instructs[i][3]]:
        potentialCount += 1
    #BITWise And
    if before[i][instructs[i][1]] & before[i][instructs[i][2]] == after[i][instructs[i][3]]:
        potentialCount += 1
    if before[i][instructs[i][1]] & instructs[i][2] == after[i][instructs[i][3]]:
        potentialCount += 1
    #OR
    if before[i][instructs[i][1]] | before[i][instructs[i][2]] == after[i][instructs[i][3]]:
        potentialCount += 1
    if before[i][instructs[i][1]] | instructs[i][2] == after[i][instructs[i][3]]:
        potentialCount += 1
    #assignment
    if before[i][instructs[i][1]] == after[i][instructs[i][3]]:
        potentialCount += 1
    if instructs[i][1] == after[i][instructs[i][3]]:
        potentialCount += 1
    #greater
    if instructs[i][1] > before[i][instructs[i][2]] and after[i][instructs[i][3]] == 1:
        potentialCount += 1
    elif instructs[i][1] <= before[i][instructs[i][2]] and after[i][instructs[i][3]] == 0:
        potentialCount += 1
    if before[i][instructs[i][1]] > instructs[i][2] and after[i][instructs[i][3]] == 1:
        potentialCount += 1
    elif before[i][instructs[i][1]] <= instructs[i][2] and after[i][instructs[i][3]] == 0:
        potentialCount += 1
    if before[i][instructs[i][1]] > before[i][instructs[i][2]] and after[i][instructs[i][3]] == 1:
        potentialCount += 1
    elif before[i][instructs[i][1]] <= before[i][instructs[i][2]] and after[i][instructs[i][3]] == 0:
        potentialCount += 1
    #equality
    if instructs[i][1] == before[i][instructs[i][2]] and after[i][instructs[i][3]] == 1:
        potentialCount += 1
    elif instructs[i][1] != before[i][instructs[i][2]] and after[i][instructs[i][3]] == 0:
        potentialCount += 1
    if before[i][instructs[i][1]] == instructs[i][2] and after[i][instructs[i][3]] == 1:
        potentialCount += 1
    elif before[i][instructs[i][1]] != instructs[i][2] and after[i][instructs[i][3]] == 0:
        potentialCount += 1
    if before[i][instructs[i][1]] == before[i][instructs[i][2]] and after[i][instructs[i][3]] == 1:
        potentialCount += 1
    elif before[i][instructs[i][1]] != before[i][instructs[i][2]] and after[i][instructs[i][3]] == 0:
        potentialCount += 1


    if potentialCount >= 3:
        threeOrMoreCount += 1
print(threeOrMoreCount)

