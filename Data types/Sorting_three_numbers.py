'''
Сортировка трёх 🌶️
Напишите программу, которая упорядочивает три числа от большего к меньшему.
#
Формат входных данных
На вход программе подается три целых числа, каждое на отдельной строке.
#
Формат выходных данных
Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.
'''
num1 = int(input())
num2 = int(input())
num3 = int(input())

a = min(num1, num2, num3)
e = min(num1, num2, num3) + max(num1, num2, num3)
c = max(num1, num2, num3)
b = num1 + num2 + num3 - e 

print(c)
print(b)
print(a)