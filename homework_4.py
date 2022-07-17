''' # 1
users_str = input('Please enter a string ')
if len(users_str) < 2:
    print('The string is too short - %s' %users_str)
else:
    print(users_str[0] +users_str[1] + users_str[-2] + users_str[-1]) '''

''' # 2 
import string
from collections import Counter
some_string = input('Enter text: ') # Принятие у пользователя строки
counter = Counter(some_string) # Подсчет кол-ва символов в строке с помощью импортированного счетчика

alphabet = string.ascii_letters # Вложение латинского алфавита в переменную с помощью импортированного модуля string
dictionary = (counter[alphabet]) # Подсчет кол-ва присутствующих в строке символов 
print(counter) '''

 # 3
''' user_grocery = input ('Enter your grocery list ')
user_grocery_list = user_grocery.split(' ') # Преобразование строки в список с разделением пробелом
longest_word = (max(user_grocery_list, key=len)) # С помощью функции max() и ключа len определяем самое длинное слово в списке
number_of_characters = len(longest_word) # Определяем кол-во символов в самом длинном слове
print('The longest word in a grocery list is a {}, lentgh is {}' .format(longest_word, number_of_characters)) '''

''' # 4
user_name = input('Please enter your name: ')
print(user_name.upper(), (user_name.lower())) '''

''' # 5
colors = input ('Enter your fav colors: ')
colors_list = colors.split(' ') # Преобразование строки в список с разделением пробелом
unique_colors_list = list(set(colors_list)) # Преобразовывание списка в множество, где содержатся только уникальные элементы 
unique_colors_list.sort() # Сортировка списка по алфавиту 
print(unique_colors_list) '''

# 6 Кортеж - неизменяемый объект

''' # 7
list_of_tuples =  [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
list_of_lists = [] # Создаем пустой список
for l in list_of_tuples:
    list_of_lists.append(list(l)) # Через цикл for каждый элемент кортежа переводим в новый пустой список
print(list_of_lists) # Выводим список '''

''' # 8 
    # Создаем цикл, в котором генерируем список необходимых чисел и проверяем их способность деления на 3 без остатка
for multiple in range(-99, 99, 3): 
    if multiple%3 == 0:
        print(f'This number is a multiple of three {multiple}') '''

''' # 9
list_1 = input('Enter first list: ')
list_2 = input('Enter second list: ')
# Преобразование строк в списки с разделением пробелом:
list_1_l = list_1.split(' ')
list_2_l = list_2.split(' ')
# Создаем пустой список
list_3_l = []
# С помощью цикла проверяем элементы двух списков на совпадение, одинаковые элементы (в одном экземпляре) переводим в третий список
for a in list_1_l:
    for b in list_2_l:
        if a == b:
            list_3_l.append(a)
            break
print('Тrue {}' .format(list_3_l)) '''




