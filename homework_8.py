# Документация по datetime
# https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime

import datetime

''' # 1
def max_number(first_num, second_num, third_num): # Создаем функцию с 3мя аргументами
    return max(first_num, second_num, third_num) # Возвращаем максимальный

print(max_number(first_num=input('Enter the first number '),
                 second_num=input('Enter the second number '),
                 third_num=input('Enter the third number '))) '''

''' # 2
 def finding_max_tw(first_num, second_num): # Создаем функцию с 2мя аргументами
    return max(first_num, second_num) # Возвращаем максимальный

def finding_max_three(first_num, second_num, third_num): # Создаем новую функцию, добавляем один аргумент
    process = finding_max_tw(first_num, second_num) 
    return finding_max_tw(process, third_num) # С использованием первой функции возвращаем max среди всех трех аргументов

print (finding_max_three(3,65,800)) '''

''' # 3 
list_of_tuples = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
list_of_tuples.sort(key=lambda el: el[1]) # Сортируем список кортежей по цифре с помощью lambda
print(list_of_tuples) '''

''' # 4
now = datetime.datetime.now() 
year = lambda x: x.year # Определяем текущий год 
month = lambda x: x.month # Определяем текущий месяц 
day = lambda x: x.day # Определяем текущий день
print(year(now))
print(month(now))
print(day(now)) '''


