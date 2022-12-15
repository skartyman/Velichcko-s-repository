n=int(input('Введите высоту фигуры: '))
for h in range(n):
    for w in range(h+1,n):
        print(' ', end=' ')
    for w in range(h):
        print('*', end=' ')
    for w in range(h+1):
        print('*',end=' ')
    print()