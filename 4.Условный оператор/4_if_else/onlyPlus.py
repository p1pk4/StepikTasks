'''
Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

Формат входных данных
На вход программе подаются три целых числа.

Формат выходных данных
Программа должна вывести одно число – сумму положительных чисел.

Примечание. Если положительных чисел нет, то следует вывести 00.

'''
num1 = int(input())
num2 = int(input())
num3 = int(input())

'''
num1 /= 1
num2 /= 1
num3 /= 1
'''
digital = 0
if num1 >= 0:
    digital += num1
if num2 >= 0:
    digital += num2
if num3 >= 0:
    digital += num3
print(digital)
