'''
*8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список. Если строка
 содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен
 подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_'](используйте срезы длинны 2)
'''
my_str = 'adadsdsdwewedee'
if len(my_str)%2!=0:
    my_str=(my_str[::]+'_')
my_list = ([my_str[i:i+2] for i in range(0, len(my_str), 2)])
print(my_list)