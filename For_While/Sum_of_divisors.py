'''
Сумма делителей
На вход программе подается натуральное число n. 
Напишите программу, которая вычисляет сумму всех его делителей.
#
Входные данные
На вход программе подается натуральное число n.
#
Выходные данные
Программа должна вывести единственное число в соответствии с условием задачи.
#
Примечание. Функция подсчета суммы всех делителей числа является очень важной в теории чисел.
'''
n = int(input())
result = 0
for i in range(1, n + 1): 
    # num = n / i
    if n % i == 0:
        result += i # num
print(result)