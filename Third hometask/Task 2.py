'''
По данному целому числу N распечатайте все квадраты натуральных чисел,
 не превосходящие N, в порядке возрастания.
Например:
50      1 4 9 16 25 36 49
10      1 4 9
100     1 4 9 16 25 36 49 64 81 100

'''
N = int(input('Введите значение, которое не должен привышать наибольший квадрат из диапазона: '))
for i in range(1,N):
    i = i**2
    if i >= N:
        break
    print(i, end=' ')