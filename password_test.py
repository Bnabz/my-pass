import unittest 
import pyperclip
from password import User

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

if __name__ == '__main__':
    unittest.main()