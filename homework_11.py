# 1, конструкция try / except / finally
''' def division(num_1, num_2):
    try:
        return int(num_1) / int(num_2)
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    finally:
        print('Thank you for using program')


print(division(num_1=input('Enter first number: '), num_2=input('Enter second number: '))) '''

# использование raise и конструкции try / except / else

''' def division(num_2):
    try:
        if num_2 == 0:
            raise ZeroDivisionError
    except:
        print('ZeroDivisionError')
    else:
        print('It is okay')

print(division(num_2=int(input('Введите знаменатель ')))) '''


''' # 2
 def division(first_num, second_num):
    try:
        return int(first_num) / int(second_num)
    except ZeroDivisionError:
        print('Ай яй яй, делить на ноль можно не многим')
    except Exception as e:
        print(e)
    finally:
        print('I am happy that you learn python')

print(division(first_num=input('Enter first number: '),
               second_num=input('Enter second number: '))) '''

# 3 тест прошла, главу про исключения прочла. С паттерном разбираюсь, пока трудновато

#4
''' 
def example1():
    for i in range(3):
        try:
            x = int(input("enter a number: "))
            y = int(input("enter another number: "))
            print(x, '/', y, '=', x/y)
        except ZeroDivisionError: # Обрабатываем ошибку при делении на ноль
            print('Деление на ноль невозможно')
        except ValueError: # Обрабатываем ошибку при вводе float или использовании str вместо int при вводе
            print('Пожалуйста, вводите значения целыми числами и не используйте буквы')

print(example1()) '''

''' def example2(L):
    print("\n\nExample 2")
    sum = 0
    sumOfPairs = []
    try:
        for i in range(len(L)):
            if i != len(L)-1: # Исправление ошибки IndexError: list index out of range
                sumOfPairs.append(L[i]+L[i+1])
        print("sumOfPairs = ", sumOfPairs)
    except TypeError: # Обработка ошибки при использовании строки в списке
       print('Пожалуйста, вводите значения целыми числами и не используйте буквы')


print(example2(L=[1,1,2,2,3,3])) '''

