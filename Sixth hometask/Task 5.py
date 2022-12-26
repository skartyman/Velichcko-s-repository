'''
*7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit и r_limit, которые точно находятся в
этой строке. Причем l_limit левее чем r_limit. В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими
 символами. my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
'''
my_string = 'Decentraland is home to a constant stream of community-organized events and new developments are frequent.'
l_limit = 'h'
r_limit = 'a'
sub_str = my_string[((my_string.find(l_limit))+1):(my_string.rfind(r_limit))]
print(sub_str)