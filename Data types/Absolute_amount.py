'''
Абсолютная сумма
Даны пять чисел a_1, a_2, a_3, a_4, a_5.
Напишите программу, которая вычисляет сумму их модулей a_1 + a_2 + a_3 + a_4 + a_5.
#
Формат входных данных
На вход программе подается пять действительных чисел a_1, a_2, a_3, a_4, a_5, каждое на отдельной строке.
#
Формат выходных данных
Программа должна вывести одно число – сумму модулей введённых чисел.
'''
num1 = abs(float(input()))
num2 = abs(float(input()))
num3 = abs(float(input()))
num4 = abs(float(input()))
num5 = abs(float(input()))
summ = num1 + num2 + num3 + num4 + num5
print(summ)

# abs можно использовать везде. И в инпутах, и в принтах и в вычислениях применяя к однуму операнду или сразу ко всем