'''
Сумма чисел
На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке. 
Напишите программу, которая подсчитывает сумму введенных чисел. 
#
Формат входных данных
На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.
#
Формат выходных данных
Программа должна вывести сумму данных чисел.
'''

# Количество чисел сумму которых надо посчитать
n = int(input())
sum = 0

while n > 0:
    n -= 1
    num = int(input())
    sum += num
    if n == 0:
        break
print(sum)

a = int(input())
for i in range(0, a):
    num1 = int(input())
    sum += num1
print(sum, 'd')