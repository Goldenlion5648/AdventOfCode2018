a = {-1e9}
total = 0
c= []
for i in range(963):
    b = int(input())
    c.append(b)
    # total += b
    # if( total not in a):
    #     a.add(total)
    # else:
    #     print('up here',total)
    #     break
print(a)
i = 0
d = 0
while total not in a:
    if( total not in a):
        a.add(total)
    else:
        print('answer:',total)
        break
    total += c[i]
    i += 1
    if(i == len(c)):
        i = 0
        d += 1
print(total)
print(d)
print(i)
print('done')