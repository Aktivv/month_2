n = int(input(''))

for i in range(1, n+1):
    num = 0
    for j in range(1, 11):
        num += i
        rovno = len(str(num))
        if rovno == 1:
            print(num, end='  ')
        else:
            print(num, end=' ')
    print('\n')