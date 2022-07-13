user_birthyear = input('Hi! What year were you born? ')

if not user_birthyear.isdigit():
    print('Please enter number')
    user_birthyear = input('Here we go again. What year were you born? ')
else:
    print('Cool!')


user_birthyear_int = int(user_birthyear)

if user_birthyear_int == 2001:
    print('You should visit Holland')
elif user_birthyear_int <= 2002:
    print('You should visit Vietnam')
else:
    print('Travel everywhere')
