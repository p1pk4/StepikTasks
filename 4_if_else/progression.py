# У нас три числа (по условию). 
# Если сложить первое и третье число, поделить эту сумму на 2, должно получаться второе число. 
# Тогда перед нами арифметическая прогрессия.

'''
Напишите программу, которая определяет, являются ли три заданных числа 
(в указанном порядке) последовательными членами арифметической прогрессии.

Формат входных данных
На вход программе подаются три числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести «YES» или «NO» (без кавычек) в соответствии с условием задачи. 
'''
'''
a1 = 1
a2 = 2 # = int(input()) # 2 начало
n = int(input()) # 9 конец
d = int(input()) # 1 шаг
a2 = (a2 - 1) + d # формула прогрессии
'''
a = int(input())
b = int(input())
c = int(input())
num = (b - a) + b
if num == c:
    print('YES')
else:
    print('NO')
 