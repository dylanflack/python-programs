from user_input import *

while True:
    use_system_info = input("\nDo you want to retrieve system information? This includes System hostname, IP address, and system time etc. (yes/no): ").lower()
    if use_system_info in ('yes', 'no'):
        break
    else:
        red_text("Invalid response. Please enter 'yes' or 'no'.")

#create an instance of SystemInfo based on the user's response
system_info = SystemInfo(use_system_info == 'yes')


def main():
    main_user  = UserInfo(state_list, email_list, password_list)
    
    main_user.user_name()
    main_user.user_age()
    main_user.user_state()
    main_user.user_email()
    main_user.user_password()
      

if __name__ == "__main__":
    main()
    
