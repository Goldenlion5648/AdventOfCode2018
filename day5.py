def react(s):
    changed = True
    while changed:
        changed = False
        i = 0
        while i < len(s) - 1:
            if(abs(ord(s[i]) - ord(s[i+1])) == 32):
                s = s[:i] + s[i+2:]
                changed = True
            else:
                i += 1
    return s

a = input()
c = []
# d = dict.fromkeys([chr(i) for i in range(97, 123)], 0)
for w in range(65, 65+26):
    v = 0
    li = list(a)
    while v < (len(li)):
        if(chr(w) == li[v].upper()):
            li.pop(v)
        else:
            v += 1
    c.append(react("".join(li)))

        # a[i] = a[i].lower()
        # d[g] += 1
small = 100000000
print(c[-1])
for k in c:
    small = min(small, len(k))
print(small)

# for x in d:
#     if(d[x] < high):
#         high = d[x]
# print(high)

# print(a)
# print(len(a))