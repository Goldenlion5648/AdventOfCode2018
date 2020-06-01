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

fringe = []
while len(answer) != len(requirements):
    for i in requirements:
        if(requirements[i] == ''):
            if(i not in fringe and i not in answer):
                fringe.append(i)
    fringe.sort()
    print(fringe)
    cur = fringe.pop(0)
    answer += cur
    for i in requirements:
        requirements[i] = requirements[i].replace(cur, '')

    fringe.sort()
    print(requirements)
    print(fringe)
    print(answer)
print(requirements)