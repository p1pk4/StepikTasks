'''
Средние значения
В математике выделяют следующие средние значения:
....Много формул, посмотреть можно тут: 
# https://cdn.discordapp.com/attachments/474001813071462412/883595883751555082/unknown.png
#
Формат входных данных
На вход программе подается два вещественных числа aa и bb​, каждое на отдельной строке.
#
Формат выходных данных
Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.
'''
import math

a = float(input())
b = float(input())

# Среднее арифметическое чисел a и b.
arithmetic = (a + b) / 2
print(arithmetic)
# Среднее геометрическое чисел a и b.
geometry = math.sqrt(a * b) 
print(geometry)
# Среднее гармоническое чисел a и b.
harmonic = (2 * a * b) / (a + b)
print(harmonic)
# Среднее квадратное чисел a и b.
quadratic = math.sqrt((math.pow(a, 2) + math.pow(b, 2)) / 2)
print(quadratic)