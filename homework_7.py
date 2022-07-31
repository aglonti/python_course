''' # 1
def square(x): # Создаем функцию
    perimeter = x * 4 # Счетчик периметра
    diagonal = 2 * (x ** 2) # Счетчик диагонали
    sqr_area = x * x # Счетчик площади
    return (perimeter, diagonal, sqr_area)


print(square(int(input('Enter some number ')))) '''

'''# 2
def year_season(month): # Создаем функцию
    if 2 >= month > 0 or (month == 12): # Выставляем условия для счета месяца
        return print('Winter')
    elif 3 <= month <= 5:
        return print('Spring')
    elif 6 <= month <= 8:
        return print('Summer')
    elif 9 <= month <= 11:
        return print('Autumn')
    else:
        print('Oops, you did something wrong') 

print(year_season(int(input('Enter the number of month ')))) '''

''' # 3
first_list = input('Enter the first list with using commas ').split(',') # Принимаем два списка
second_list = input('Enter the second list with using commas ').split(',')

def common_list(first_list, second_list): # Создаем функцию
    final_list = [] # Создаем пустой список 
    for i in range(len(first_list)): # Проходимся по всем элементам
        final_list.append(first_list[i]) # Добавляем в новый список первый элемент первого списка
        final_list.append(second_list[i]) # И следом добавляем первый элемент второго списка
    return final_list


print(common_list(first_list,second_list)) '''

''' # 4 
def polindrome(user_str): 
    if user_str == user_str[::-1]: # Проверяем является ли слово палиндромом
        return print('True')
    else:
        return print('False')

print(polindrome(input('Enter a polindrome word '))) '''