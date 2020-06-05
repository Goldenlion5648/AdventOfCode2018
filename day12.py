start = '###......#.#........##.###.####......#..#####.####..#.###..#.###.#..#..#.#..#..#.##...#..##......#.#'
# start = '#..#.#..##......###...###'
a = '.' * 30 + start + '.' * 300
startIndex = a.index('#')

b = list('.' * len(a))
instruct = []
#32
for i in range(32):
    instruct.append(input())

# print(instruct)
print('0:\t', *a,sep='')
# print(a)
for i in range(200):
    for j in range(len(instruct)):
        pat = instruct[j][:5]
        # print('pat',pat)
        # print('a', a)
        # b = a.replace(pat, '..'+instruct[j][-1] + ..)

        for w in range(len(a) - 4):
            matches = True
            for k in range(len(pat)):
                if(pat[k] != a[w + k]):
                    # print('pat[k]',pat[k], 'did not equal', a[w])
                    matches = False
                    break
            if(matches):
                b[w + 2] = instruct[j][-1]
                # print('changed')
    a = "".join(b)
    print(i + 1,':\t', *a, sep='')
    b = list('.' * len(a))

total = 0
count = 0
for i in range(31, len(a) - 70):
    if(a[i] == '#'):
        total += (i - 30) + 49999999800
        count += 1
        # print('added', i - 30)
# total += count * 50000000000
#wrong 2100000008828
print(total)