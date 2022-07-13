print('Hi there!')
user_nickname = input('Enter your nickname ')

if 'admin' in user_nickname:
    print('Hello, Lord')

user_gender = input('Please enter your gender: F or M ')
user_age = input('Now enter your age ')

user_age_int = int (user_age)

if 10 < user_age_int < 14 and user_gender == 'M' or user_age_int > 30 and user_gender == 'M' :
    print('I advise you to watch "StarWars" or "The Mandalorian"')
elif 22 < user_age_int < 32 and user_gender == 'F' :
    print('I advise you to watch "Transformers"')
elif user_age_int < 16 and user_gender == 'F' :
    print('I advise you to watch "The divergent"')
elif user_nickname == 'Zhenya' :
    print('I advise you to watch "TENET"')
elif user_age_int <= 10 and user_gender == 'M' :
    print('I advise you to watch "TMNT"')

if user_nickname == 'Guido' :
    print('Thank you so much!')

