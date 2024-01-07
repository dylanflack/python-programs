import socket
import random
import secrets
import string
from datetime import *


state_list = [
                    'Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa',
                    'Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire',
                    'New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota',
                    'Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming'
                    ]
email_list = [
                    '@gmail.com','@yahoo.com','@hotmail.com','@outlook.com','@aol.com','@icloud.com',
                    '@msn.com','@live.com','@zoho.com','@yandex.com','@protonmail.com','@gmx.com','@mpxf.men'
                    ]
password_list = [
                    '!','@','#','$','%','^','&','*','(',')','_','+','=','{','}','[',']','|',';',':','"',"'",'<','>',',','.','?','/','`','~'
                    '1','2','3','4','5','6','7','8','9','0', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p' 'q','r','s','t','u','v','w','x','y','z',
                        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O' 'P','Q','R','S','T','U','V','W','X','Y','Z'
                        ]

def red_text(text):
        print('\033[1;31;40m' + text + '\033[0m')       # prints text in red, used for invalid input only

class SystemInfo:
    def __init__(self, use_system_info=True):
        if use_system_info:
            self.user_ip_address()
            self.user_hostname()
            self.user_time()

    def user_ip_address(self):
        user_hostname = socket.gethostname()
        user_ip_address = socket.gethostbyname(user_hostname)
        print('\nYour IP address is:', user_ip_address)

    def user_hostname(self):
        user_hostname = socket.gethostname()
        print('Your hostname is:', user_hostname)

    def user_time(self):
        today = date.today()
        print('\nTodays date is:')
        dt = today.strftime("%B %d, %Y")
        print(dt)


class UserInfo:
    def __init__(self, state_list, email_list, password_list):
        self.state_list = state_list
        self.email_list = email_list
        self.password_list = password_list
         
    def user_name(self):
        while True:
            name = input('\nWhat is your name? ')
            
            if len(name) >= 3 and name.isalpha():
                print('Hello', name)
                break
            else:
                red_text('Invalid input, please make sure to enter more than 3 characters')


    def user_age(self):
        while True:
            age = input('\nHow old are you? ')

            if age.isdigit():
                print('You are', age, 'years old')
                break
            else:
                red_text('Invalid input')
    

    def user_state(self):
            print('\nPlease choose a state from the list below')

            for i in range(len(state_list)):
                print(i, state_list[i])

            while True:
                state = input('\nWhat state do you live in? ')

                if state.isdigit():
                    state = int(state)
                    if state >= 0 and state <= 50:
                        print('You live in', state_list[state])
                        break
                    else:
                        red_text('Invalid input')
               

    def user_email(self):
            print('\nWhat is your email name?')

            email_name = input('Enter your email name: ')

            if len(email_name) < 3 or not email_name.isalnum():
                red_text('Invalid input')
                return self.user_email()

            print('Your email name is: ', email_name)

            print('\nPlease choose an email domain from the list below: ')


            for i, domain in enumerate(email_list):
                print(i, domain)

            while True:
                email_domain = input('\nEnter your email domain: ')

                if email_domain.isdigit():
                    email_domain = int(email_domain)
                    if 0 <= email_domain <= 12:
                        print('\nYour email is:', email_name + email_list[email_domain])
                        break
                    else:
                        red_text('Invalid input')


    def genrate_password(self, length=10):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password
    
    def user_password(self):
        print('\n Would you like to create a random password?')

        ask_password = input('yes or no: ')

        if ask_password.lower() == 'yes':
            random_password = self.genrate_password()
            print('\nYour random password is:', random_password)
        elif ask_password.lower() == 'no':
            enter_password = input('\nEnter your custom password: ')
            print('\nYour password is:', enter_password)
        else:
            red_text('Invalid input')
            return self.user_password()
             






