'''
До КОНЦА 1
На вход программе подается последовательность слов, каждое слово на отдельной строке. 
Концом последовательности является слово «КОНЕЦ» (без кавычек). 
Напишите программу, которая выводит члены данной последовательности.
#
Формат входных данных
На вход программе подается последовательность слов, каждое слово на отдельной строке.
#
Формат выходных данных
Программа должна вывести члены данной последовательности.
'''
# + еще несколько задач было решено

some_text = input()
count = 0
while some_text != 'стоп' and some_text != 'хватит' and some_text != 'достаточно':
    # print(some_text)
    some_text = input()
    count += 1
    if some_text == 'стоп' or some_text == 'хватит' or some_text == 'достаточно':
        print(count)