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



if __name__ == '__main__':
    unittest.main()