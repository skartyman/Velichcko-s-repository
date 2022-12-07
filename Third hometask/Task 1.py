'''
Написать калькулятор для простых операций(+,-,*,/,**),
Операнды и оператор вводятся с клавиатуры отдельно(отдельные переменные)
'''

left_operand = int(input('Введите левый операнд: '))
operator = input('Введите рператор: +, -, *, / или ** (возведение в степень)')
right_operand = int(input('Введите правый операнд: '))
if operator == "+" :
    print(float(left_operand + right_operand))
elif operator == "-" :
    print(float(left_operand - right_operand))
elif operator == "*" :
    print(float(left_operand * right_operand))
elif operator == "/" :
    print(float(left_operand / right_operand))
elif operator == "**" :
    print(float(left_operand ** right_operand))
else :
    print('Вы ввели какой-то неизвестный мне оператор, прощайте!')
