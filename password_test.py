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


if __name__ == '__main__':
    unittest.main()