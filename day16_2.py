a = []
registers = [0, 0, 0, 0]
for i in range(950):
    w = list(map(int, input().split(' ')))
    code = w[0]
    print('instruct',w)
    print(i, '\t', registers)
        #addr
    if code == 1:
        registers[w[3]] = registers[w[1]] + registers[w[2]]
        #addi
    elif code == 3:
        registers[w[3]] = registers[w[1]] + w[2]
        #mulr
    elif code == 2:
        registers[w[3]] = registers[w[1]] * registers[w[2]]
        #muli
    elif code == 13:
        registers[w[3]] = registers[w[1]] * w[2]
    #borr
    elif code == 5:
        registers[w[3]] = registers[w[1]] & registers[w[2]]
    #bori
    elif code == 0:
        registers[w[3]] = registers[w[1]] & w[2]
    #borr
    elif code == 6:
        registers[w[3]] = registers[w[1]] | registers[w[2]]
    #bori
    elif code == 10:
        registers[w[3]] = registers[w[1]] | w[2]
        #setr
    elif code == 11:
        registers[w[3]] = registers[w[1]]
        #seti
    elif code == 8:
        registers[w[3]] = w[1]
        #gtir
    elif code == 15:
        if w[1] > registers[w[2]]:
            registers[w[3]] = 1
        else:
            registers[w[3]] = 0
    #gtri
    elif code == 4:
        if registers[w[1]] > w[2]:
            registers[w[3]] = 1
        else:
            registers[w[3]] = 0
    #gtrr
    elif code == 14:
        if registers[w[1]] > registers[w[2]]:
            registers[w[3]] = 1
        else:
            registers[w[3]] = 0
        #gtir
    elif code == 12:
        if w[1] == registers[w[2]]:
            registers[w[3]] = 1
        else:
            registers[w[3]] = 0
    #gtri
    elif code == 7:
        if registers[w[1]] == w[2]:
            registers[w[3]] = 1
        else:
            registers[w[3]] = 0
    #gtrr
    elif code == 9:
        if registers[w[1]] == registers[w[2]]:
            registers[w[3]] = 1
        else:
            registers[w[3]] = 0
    else:
        print('error was made, code', code)

print('answer', registers)
