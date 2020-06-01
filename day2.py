# a = 0
# b = 0
# c = {}
# for i in range(250):
#     c = dict.fromkeys([chr(i) for i in range(97, 123)], 0)
#     j = input()
#     # print(j)
#     for q in j:
#         c[q] += 1
#     found2 = False
#     found3 = False
#     for f in c:
#         if(c[f] == 2 and not found2):
#             a += 1
#             found2 = True
#         if(c[f] == 3 and not found3):
#             b += 1
#             found3 = True

# print(c)
# print(a)
# print(b)

a = []
for i in range(250):
    a.append(input())
# print(a)
# print(len(a))
for i in range(25):
    b = set()
    for k in a:
        c = k[:i] + k[i+1:]
        # print(i)
        if(c not in b):
            b.add(c)
        else:
            print(c)


