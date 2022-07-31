# Документация по словарям https://docs.python.org/3/c-api/dict.html


''' # 1
first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}

dictionaries_list = [first, second, third, fourth, fifth] # Помещаем словари в один список
sixth = dict() # Создаем новый, пустой словарь


for i in dictionaries_list: # С помощью цикла проходимся по всем словарям, сложенным в список
    sixth.update(i) # Каждый существующий словарь поочередно добавляем в новый
print(sixth) '''

''' #2
square_numbers_dict = dict() # Создаем пустой словарь
for i in range(11, 21): # Устанавливаем ключами числа от 11 до 20 включительно
    square_numbers_dict[i] = i ** 2 # Значения - квадраты этих чисел 
print(sum(square_numbers_dict.values())) # Суммируем и выводим все значения словаря '''

''' # 3
colors_list = {2: 'green', 3: 'red', 4: 'white',  1: 'black'}  # Создаем словарь

for key in sorted(colors_list):  # Сортируем словарь по ключам
    print(f'{key}, {colors_list[key]}') '''


''' #4
some_dict = {'id1':
{
'name': 'Ruslan',
'class': 1,
'subjects' : {'Math', 'Algorithms', 'English'}
},
'id2':
{
'name': 'Mark',
'class': 2,
'subjects' : {'Geometry', 'Java', 'Cooking'}
},
'id3':
{
'name': 'Ruslan',
'class': 1,
'subjects' : {'Math', 'Algorithms', 'English'}
}
}

final_dict = dict() # Создаем пустой словарь для размещения в нем уникальных элементов

for key, value in some_dict.items(): # Перебираем ключи и значения в оригинальном словаре 
    if value not in some_dict.values(): # Если значения нет в новом словаре, то добавляем
        some_dict[key] = value
        
print(final_dict) '''


''' #6
shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None,
           'wednesday': ['manicure', 'hammam', 'beer']}

i = 0 # Создаем счетчик
for v in shedule.values(): # Просматриваем значения
    if type(v) == list: # Если значени - список
       i += len(v) # Увеличиваем счетчик на кол-во элементов списка

print(i) '''

# 7 тест прошла


