'''
Пол и потолок
Напишите программу, вычисляющую значение [x] + [x] по заданному вещественному числу x.
#
Формат входных данных
На вход программе подается одно вещественное число x.
#
Формат выходных данных
Программа должна вывести одно число – значение указанного выражения.
#
Примечание. ⌈x⌉ – потолок числа, ⌊x⌋ – пол числа.
'''
import math

num = float(input())

num = math.ceil(num) + math.floor(num)
print(num)