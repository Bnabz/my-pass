import unittest 
import pyperclip
from password import User
from password import Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Brian", "Nabiswa", "Bnabz", "mypass")

    def test_init(self):
        self.assertEqual(self.new_user.first_name, "Brian")
        self.assertEqual(self.new_user.last_name, "Nabiswa")
        self.assertEqual(self.new_user.user_name, "Bnabz")
        self.assertEqual(self.new_user.password, "mypass")

    def test_save_user(self):
        self.new_user.save_user() #saving the new user_list
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
            User.user_list = []

    def test_save_multiple_users(self):
        self.new_user.save_user()
        test_user = User("Laureen", "Mak", "kitten", "420")
        test_user.save_user()

        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("mullah", "Mwah", "comic", "choma")
        test_user.save_user()
        self.new_user.delete_user() 
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_username(self):
        self.new_user.save_user()
        test_user = User("mullah", "Mwah", "comic", "choma")
        test_user.save_user()
        found_user = User.find_by_username("comic")
        self.assertEqual(found_user.user_name,"comic")

    def test_user_exists(self):
        self.new_user.save_user()
        test_user = User("Test","user","testname","testpass") # new contact
        test_user.save_user()
        user_exists = User.user_exists("testname")
        self.assertTrue(user_exists)

    def test_display_user_information(self):
        self.assertEqual(User.display_user_details(),User.user_list)



class TestCredentials(unittest.TestCase):
  
    def setUp(self):
      
        self.new_credential = Credentials('TestPlat','tester','testpass')
   
    def test_init(self):
        self.assertEqual(self.new_credential.platform,'TestPlat')
        self.assertEqual(self.new_credential.username,'tester')
        self.assertEqual(self.new_credential.password,'testpass')
    
    def test_save_credentials(self):
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    
    def tearDown(self):
    
        Credentials.credentials_list = []
    

    def test_save_multiple_credentials(self):
       
        self.new_credential.save_credentials()
        test_credential = Credentials('TestPlat','tester','testpass')
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
    

    def test_delete_credentials(self):
        
        self.new_credential.save_credentials()
        test_credential = Credentials('TestPlat','tester','testpass')
        test_credential.save_credentials()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    
    def test_find_credentials(self):
      
        self.new_credential.save_credentials()
        test_credential = Credentials('TestPlat','tester','testpass')
        test_credential.save_credentials()
        found_credentials = Credentials.find_credentials('TestPlat')
        self.assertEqual(found_credentials.platform,test_credential.platform)
    
    def test_credential_exists(self):
       
        self.new_credential.save_credentials()
        test_credential = Credentials('TestPlat','tester','testpass')
        test_credential.save_credentials()
        found_credential_exists = Credentials.credential_exists('TestPlat')
        self.assertTrue(found_credential_exists)
    
    def test_display_all_credentials(self):
       
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    def test_copy_credentials(self):
        self.new_credential.save_credentials()
        Credentials.copy_credentials('TestPlat')
        test_copy = ('Platform:'+self.new_credential.platform+', '+ 'Username: '+self.new_credential.username+', '+ 'Password: '+self.new_credential.password)
        self.assertEqual(test_copy,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()