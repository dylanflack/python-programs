import random
import string

def user_name():
    username = input('\nEnter your name: ')

    while True:
        if len(username) < 3 or len(username) > 25:
            print('Invalid Input, no less than 3 characters and no more than 25')
            username = input('Enter your name: ')
        else:
            print(f'Hello, {username}!')
            break
           
def user_age():
    age = input('\nEnter your age: ')

    while True:
        if age.isdigit() == False or int(age) <= 0 or int(age) > 99:
            print('Invalid Input, Age must be a number between 1 and 99')
            age = input('Enter your age: ')
        else:
            print(f'You are {age} years old\n')
            break

def user_sex():
    arr = ['male', 'female', 'other', 'prefer not to say']

    for i in range(len(arr)):
        print(i, arr[i])

    while True:
        sex = input(f'Please select your sex: ')

        if sex.isdigit():
            sex = int(sex)
            if sex >= 0 and sex <= 3:
                break
            else:
                print('Invalid Input, Please enter a valid number')

def user_email():
    arr = ['@gmail.com', '@yahoo.com', '@outlook.com', '@mpxf.men']

    while True:
        email_name = input('\nEnter your email name: ')

        if len(email_name) <= 2 or not email_name.isalnum():
            print('Invalid Input, Please enter a valid email')
        else:
            break

    for i in range(len(arr)):
        print(i, arr[i])

    while True:
        email_domain = input('Please select your email domain: ')

        if email_domain.isdigit():
            email_domain = int(email_domain)
            if email_domain >= 0 and email_domain <= 3:
                print(f'Your email is {email_name}{arr[email_domain]}')
                break
            else:
                print('Invalid Input, Please enter a valid number')

def user_password():
    while True:
        password = input('\nEnter your password: ')

        if len(password) < 8:
            print('Invalid Input, Password must be at least 8 characters')
        else:
            break

    while True:
        confirm_password = input('Confirm your password: ')

        if confirm_password == password:
            print('Password confirmed!')
            break
        else:
            print('Invalid Input, Passwords do not match')

user_name()
user_age()
user_sex()
user_email()
user_password() 