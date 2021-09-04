'''
Тригонометрическое выражение
Напишите программу, вычисляющую значение тригонометрического выражения: sin x + cos x + tan**2*x по заданному числу градусов x.
#
Формат входных данных
На вход программе подается одно вещественное число x измеряемое в градусах​. 
#
Формат выходных данных
Программа должна вывести одно число – значение тригонометрического выражения.
#
Примечание 1. Тригонометрические функции принимают аргумент в радианах. Чтобы перевести градусы в радианы, воспользуйтесь формулой 
r = x * pi / 180
#
Примечание 2. Модуль math содержит встроенную функцию radians(), которая переводит угол из градусов в угол в радианах.
'''
import math 

x = math.radians(float(input()))

trigonometric = math.sin(x) + math.cos(x) + math.tan(x) ** 2
print(trigonometric)