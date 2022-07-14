# Методы строк:

text = 'hi world '
print(text)
print('Does the text consist of numbers?', text.isdigit()) # Состоит ли строка из цифр
print('Is the text written in upper case?', text.isupper()) # Состоит ли строка из символов в верхнем регистре
print('So it is in lower case!', text.islower()) # Состоит ли строка из символов в нижнем регистре
print(text.upper()) # Преобразование строки к верхнему регистру
print(text.lower()) # Преобразование строки к нижнему регистру
print(text.capitalize()) # Переводит первый символ строки в верхний регистр, а все остальные в нижний
print(text.swapcase()) # Переводит символы нижнего регистра в верхний, а верхнего – в нижний
print(text.title()) # Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний
print(text * 5) # Повторение строки

# Объекты:

name = 'Anna'
surname = 'Hlonti'
county = 'Ukraine'
print('Strings:',  name, surname, county)


age = 16.5
birthyear = 2006
birthmonth = 2
print('Integers:', birthyear, birthmonth)
print('Float:', age)
print('Which number is the largest?', max(age, birthmonth, birthyear)) # Использование max()

books = ['The unbearable ligtness of being', 'Dandelion Wine', 'Kafka on the shore', 'The Great Gatsby']
numbers = [1,2,3,4,5]
letters_and_numders = [1, 'a', 2, 'b', 9, 'i', 12, 'l']
print('Lists:', books, numbers, letters_and_numders)
print('Is it "The Great Gatsby" in a list?') # Ипользование in и if..else
if 'The Great Gatsby' in books :
    print('Oh, so i already tell you about this book!')
else:
    print('So I forgot about it :( But you should read!')


magic_numbers = (2, 8, 20, 28, 50, 82, 126)
rare_animals = ('vaquita', 'gorilla', 'amur leopard', 'hainan gibbon')
сolors = ('freedom blue', 'energizing yellow')
print('Tuples:', magic_numbers, rare_animals, сolors)
print('Min from magic numbers: ', min(magic_numbers)) # Использование min ()
print('Max from magic numbers:', max(magic_numbers)) # Использование max()
print('Now lets check: is it gorilla in list of a rare animals?', 'gorilla' in rare_animals) # Использование in
print('And what about cats?', 'cat' in rare_animals, ', so you can even take one from a shelter:)') # Использование in

number_word = { 1: 'one', 2: 'two', 3: 'three' }
gender = { 0: 'Female', 1: 'Male' }
students = { 'John': 'student 1', 'David': 'student 2', 'Olya': 'student 3'}
print('Dictionaries:', number_word, gender, students)

# Условия If, elif.. else:

nature_preferences = input('Let me help you to choose a country for a vacation. Which do you love more: sea or ocean? ')

if nature_preferences == 'sea':
    print('You should go to Turkey')
elif nature_preferences == 'ocean':
    print('You should go to Bali')
else: print('I asked to write only "sea" or "ocean", so you so something wrong :(')

print('I hope I helped you. Now let’s pick you a book for the road!')
user_age = input('How old are you? ')
user_age_int = int (user_age)
user_gender = input('Please enter your gender: F or M ')

if user_age_int <= 12 and user_gender == 'F':
    print('I suggest you read "Peter Pan"')
elif user_age_int <= 12 and user_gender == 'M':
    print('I suggest you read "The adventures of Jules Verne"')
elif 12 < user_age_int <= 16 and user_gender == 'M' or 12 < user_age_int <= 16 and user_gender == 'F':
    print('I suggest you read "The Adventures of Tom Sawyer"')
elif 17 <= user_age_int <30 and user_gender == 'F':
    print('I suggest you read "To Kill a Mockingbird"')
elif 17 <= user_age_int <30 and user_gender == 'M':
    print('I suggest you read "The Shawshank Redemption"')
else:
    print('Looks like it is time to reread your favorite book!')

