'''
При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах.
'''
'''
            *
          *   *
        *       *
      *           *
    *               *
  *                   *
* * * * * * * * * * * * *
'''
n=int(input('Введите высоту фигуры: '))
for h in range(n):
    for w in range(n*2-1):
        if w==n-h-1 or w==n-1+h or h==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

