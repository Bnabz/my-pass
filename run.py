import pyperclip
from password import User
from password import Credentials

def create_user(fname,lname,uname,pword):
    new_user = User(fname,lname,uname,pword)
    return new_user

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()

def find_user(username):
    return User.find_by_username(username)

def display_user():
    return User.display_user_details()


def create_credential(platform,email,password):
    new_credential = Credentials(platform,email,password)
    return new_credential

def save_credentials(credentials):
    credentials. save_credentials()

def display_credentials():
    return Credentials.display_credentials()

def delete_credential(credentials):
    credentials.delete_credentials()

def find_credential(platform):
    return Credentials.find_credentials(platform)

def check_credentials(platform):
    return Credentials.credential_exists(platform)

def copy_credentials(platform):
    return Credentials.copy_credentials(platform)


def main():
    print("Hey there! Welcome to My-Pass. What is your first name?")
    fname = input()
    print(f"Hello {fname}.Please choose one of the following options to proceed:")
    print('\n')


    print("Use these short-codes for: su - SignUp  or  si - Sign In")
    user_choice = input().lower()

    if user_choice == "su":
        print("Create an account")
        print("-"*20)
        
        print("Enter Last Name:")
        lname = input()

        print("Enter Username:")
        uname = input()

        print("Enter password")
        pword = input()

        save_user(create_user(fname,lname,uname,pword))
        print('\n')
        # print(f"Your account has been created successfully. To proceed, use the following short codes:")
        # print('\n')


    
    elif user_choice == "si":
        print("Enter your Username:")
        uname = input()

        print("Enter your password:")
        pword = input()
        print(f" Welcome,{uname}.")  


        
    while True:
        print(" Use the following short codes:\n nc - Create a new credential \n dc - Display credentials \n fc - Find a credential \n del - Delete credential \n ex - Exit the application \n")
        short_code = input( '_').lower().strip()
        if short_code == "nc":
            print(" Create New Credential")
            print(" ."*20)
            print(" Platform name:")
            platform = input( )
           
            print(" Your Platform username")
            username = input( )
            print(" Enter your password:")
            password = input()
            save_credentials(create_credential(platform,username,password))
            print('\n')
            print(f" You have successfully created new credentials for: {platform}")
            
            print('\n')
        elif short_code == "dc":
            if display_credentials():
                print(" Here are your credentials: ")
                for credential in display_credentials():
                    print(f" Platform:{credential.platform} \n Username:{username}\n Password:{password}")
                    print(' _'* 30)
                
            else:
                print(" You haven't saved any credentials yet")
        elif short_code == "fc":
            print(" Enter the Platform Name you want to search for")
            search_name = input( '_').lower()
            if find_credential(search_name):
                found_credential = find_credential(search_name)
                print(f" Platform Name : {found_credential.platform}")
                print(' -' * 20)
                print(f" Username: {found_credential.username} Password :{found_credential.password}")
                print('\n')
            else:
                print(" That Credential does not exist")
                print('\n')
        elif short_code == "del":
            print(" Enter the platform name of the Credentials you want to delete")
            search_name = input( '_').lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(" _"*20)
                search_credential.delete_credentials()
                print('\n')
                print(f" Your stored credentials for : {search_credential.platform}\n has successfully deleted!")
                print('\n')
            else:
                print(" The credential you would like to delete does not exist")

        elif short_code == 'ex':
            print(" Thanks for using My-Pass:) See you next time!")
            break
        else:
            print(" Please enter a valid code to continue")
    


if __name__ == '__main__':
     main()