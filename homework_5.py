''' # 1
password = input('Please enter your password ')
check_password = input('Now do it again ')
while check_password != password: # Запуск цикла с условием несовпадения пароля и его проверки
    password = input('They are not a match. Please enter your password ') # В таком случае повторный прием пароля и его проверки до тех пор пока условие не перестанет выполняться
    check_password = input('Now do it again ')
else: # Как только условие перестает выполняться, значит оба пароли совпали
    print('This password is set!') '''


''' #2
some_list = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
i = 0 # Присваивание переменной значения 0
while i <= len(some_list): # Запуск цикла с условием работы до тех пор, пока он не пройдется по всем элементам списка
    some_list.remove('eg') # Удаление каждого элемента "eg"
    i += 1 # Присваиние переменной +1 для перехода к следующему элементу
print(some_list) # Вывод списка без повторений '''


''' # 3
some_numbers = list(map(int, input('Please enter list of numbers with using commas: ').split(','))) 
i = 0 
while i < len(some_numbers): # Цикл проверяет все числа в списке
    if some_numbers[i] % 2 == 0: 
        i += 1 # Если число четное, цикл продолжает работу
    elif some_numbers[i] % 2 != 0:
        print('NO') # Если число нечетное, цикл останавливается
        break
else:
    print("All numbers are even") # Если цикл не прерван условием break, значит весь список чисел четный '''


''' # 4
import copy
dir_set = copy.deepcopy(dir(set)) # Копирование значений dir(set) в переменную
for i in dir(set):
    if i[0] == '_': # Цикл находит методы в списке, начинающиеся с '_' и удаляет их в списке dir_set
        dir_set.remove(i)
print(dir_set) '''

# 5 Статьи прочла)


''' # 6

some_set = {2, 4, 6} # Создание множества
print(f'Set example: {some_set}')
some_set.add (0) # add(), добавление элемента
print(f'New set with added element: {some_set}')
some_set.remove(0) # remove(), удаление элемента; при его отсутсвии в множетсве будет ошибка KeyError
some_set.discard(2) # discard(), удаление элемента; при его отсутсвии в множетсве вывода никаких ошибок не будет
print(f'New set with deleted elements: {some_set}')
some_set.clear() # clear(), очистка множетсва
print(f'New empty set: {some_set}')

first_set = {'a', 'b', 'c', 'd'}
second_set = first_set.copy() # copy(), создание копии существующего множества
first_set.remove('a')
print(second_set.difference(first_set)) # difference(), вывод элементов, которые есть в second_set, но отсутсвуют в first_set
print(f'First set: {first_set}. Second set: {second_set}')
second_set.difference_update(first_set) # difference_update(), удаление из second_set всех елементов, которые есть в firs_set
print(f'First set: {first_set}. Second set: {second_set}')
print(second_set.intersection(first_set)) # intersection(), вывод элементов, совпадающих в обоих множествах
print(first_set.isdisjoint(second_set)) # isdisjoint(), вывод True, если у множеств нет общих элементов
print(first_set.pop()) # pop (), вывод и удаление рандомного элемента
print(first_set.union(second_set)) # union (), объединение множеств '''



