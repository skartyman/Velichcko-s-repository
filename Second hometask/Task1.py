'''
    1. n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
    Сколько яблок достанется каждому школьнику?
    Сколько яблок останется в корзинке?
    Программа получает на вход числа `n` и `k` и должна вывести искомое количество яблок (два числа)
'''

n = int(input('Введите количество школьников между которыми нужно поделить яблоки: '))
k = int(input('Введите изначальное количество яблок в корзине: '))
value_apples_per_child = int(k / n)
value_apples_in_basket = int(k % n)
print(f'Каждый школьник получит по {(value_apples_per_child)} яблок.')
if value_apples_in_basket != 0:
    print(f'И в корзине осталось {(value_apples_in_basket)} яблок.')
else :
    print ('В корзине не осталось яблок.')

