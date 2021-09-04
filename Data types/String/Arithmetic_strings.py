'''
Арифметические строки
Вводятся 3 строки в случайном порядке. 
Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.
#
Формат входных данных
На вход программе подаются три строки, каждая на отдельной строке.
#
Формат выходных данных
Программа должна вывести строку «YES», если из длин введенных слов можно построить арифметическую прогрессию, «NO» в ином случае.
'''
a = input()
b = input()
c = input()

mn = min(len(a), len(b), len(c))
mx = max(len(a), len(b), len(c))

# Сумма переменных
summ = len(a) + len(b) + len(c)
# Среднее число
average = summ - (mn + mx)

if mx - average == average - mn:
    print('YES')
else:
    print('NO')