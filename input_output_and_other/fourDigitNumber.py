'''
Напишите программу для нахождения цифр четырёхзначного числа.

Формат входных данных
На вход программе подаётся положительное четырёхзначное целое число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''

num = int(input())
a = num // 1000
b = (num - a * 1000) // 100
e = (a * 1000) + (b * 100)
c = (num - e) // 10
d = num % 10
print('Цифра в позиции тысяч равна{}'.format(a))
print('Цифра в позиции сотен равна{}'.format(b))
print('Цифра в позиции десятков равна{}'.format(c))
print('Цифра в позиции единиц равна{}'.format(d))