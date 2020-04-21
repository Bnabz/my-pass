import pyperclip
class User:
    user_list = []
    def __init__(self,first_name, last_name, user_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    def save_user(self):
          User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)

    @classmethod
    def find_by_username(cls,username):
        for user in cls.user_list:
            if user.user_name == username:
                return user

    @classmethod
    def user_exists(cls,username):
        for user in cls.user_list:
            if user.user_name == username:
                    return True
        return False

    @classmethod
    def display_user_details(cls):
        return cls.user_list


class Credentials:

    credentials_list = []

    def __init__(self,platform,password):
        self.platform = platform
        self.password = password
    
    def save_credentials(self):
        Credentials.credentials_list.append(self)
    
    def delete_credentials(self):
        Credentials.credentials_list.remove(self)
    
    @classmethod
    def find_credentials(cls, platform):
      
        for credential in cls.credentials_list:
            if credential.platform == platform:
                return credential

    @classmethod
    def credential_exists(cls, platform):
      
        for credential in cls.credentials_list:
            if credential.platform == platform:
                return True
        return False
    
    @classmethod
    def display_credentials(cls):
        return cls.credentials_list
    
    # def new_password(stringLength = 10):
    #     password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
    #     return ''.join(random.choice(password) for i in range(stringLength))
    
    @classmethod
    def copy_credentials(cls,platform):
        copied_credentials = Credentials.find_credentials('platform')
        pyperclip.copy(copied_credentials)
    
 

