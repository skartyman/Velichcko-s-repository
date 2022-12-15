'''
При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах.

'''
'''
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *
  *                   *
    *               *
      *           *
        *       *
          *   *
            *
'''
n=int(input('Введите высоту фигуры: '))
for h in range(n-1):
    for w in range(h+1,n):
        print(' ', end=' ')
    for w in range(h):
        print('*', end=' ')
    for w in range(h+1):
        print('*',end=' ')
    print()
for h in range(n-1,-1,-1) :
    for w in range(n*2-1):
        if w==n-h-1 or w==n-1+h or h==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

