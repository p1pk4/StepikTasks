'''
Наибольшее и наименьшее
Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.
#
Формат входных данных
На вход программе подается пять целых чисел, каждое на отдельной строке.
#
Формат выходных данных
Программа должна вывести наименьшее и наибольшее число с поясняющей надписью.
'''
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
a = num1, num2, num3, num4, num5 # a = min(num1, num2, num3, num4, num5)
c = num1, num2, num3, num4, num5 # c = max(num1, num2, num3, num4, num5)
print('Наименьшее число = {}'.format(min(a))) # format(a)
print('Наибольшее число = {}'.format(max(c))) # format(c)