'''
Задача 1. Напишите программу, которая считывает одну строку. 
Если это строка «Python», программа выводит «ДА», в противном случае программа выводит «НЕТ».

Решение. Программа, решающая поставленную задачу, может иметь вид:
'''
# Example 1
'''
word = input()
if word == 'Python':
    print('yeah!')
else:
    print('nope')
'''
'''
Задача 2. Напишите программу, которая определяет, состоит ли двузначное число, 
введенное с клавиатуры, из одинаковых цифр. 
Если состоит, то программа выводит «ДА», в противном случае программа выводит «НЕТ».

Решение. Программа, решающая поставленную задачу, может иметь вид:
'''
# Example 2
'''
num = int(input())
last_digit = num % 10
first_digit = num // 10

if last_digit == first_digit:
    print('Yeah')
else:
    print('Nope')
'''
'''
Задача 3. Напишите программу, которая считывает три числа и подсчитывает количество чётных чисел.

Решение. Программа, решающая поставленную задачу, может иметь вид:
'''
num1, num2, num3  = int(print()), int(print()), int(print())
counter = 0 # Счетчик
if num1 % 2 == 0:
    counter += 1
if num2 % 2 == 0:
    counter += 1
if num3 % 2 == 0:
    counter += 1
print(counter)