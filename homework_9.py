''' # 1
some_list = [1, 2, 3, 4, 5, 6, 7, 8]
def sum_of_numbers (nums): # Функция, которая возвращает сумму с помощью sum
    return sum(nums)
print(sum_of_numbers(some_list)) '''

''' # 2
def sum_of_numbers (some_list): # Функция для подсчета суммы вложенных списков
    final_list = 0 # Новый пустой список
    for i in some_list:
        if type(i) == list: # Проверка на принадлежность классу
            final_list += sum_of_numbers(i) # Если элемент внутри основного списка это отдельный список - суммируются его элементы
        else: # В обратном случае это одиночный int и он суммируется с остальными значениями
            final_list += i
    return final_list

print(sum_of_numbers([1, 2, [3, 4, [5, 6], 7], 8])) '''