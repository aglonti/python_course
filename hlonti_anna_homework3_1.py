user_name = input('Hi! Please enter your name ')
user_age = input('Great, now tell me how old are you ')
user_age_int = int(user_age)

if user_age_int > 121:
    print('You are not real', user_name)
elif user_age_int == 16:
    print('Dear', user_name, 'need to wait one year')
elif 70 < user_age_int < 90:
    print('You are lucky', user_name, 'and welcome')
elif user_age_int != (70 > user_age_int > 90) and user_age_int <= 121 and user_age_int > 16:
   print('Welcome', user_name, 'on our website')
else:
   print ('I am sory', user_name, 'you are too young')