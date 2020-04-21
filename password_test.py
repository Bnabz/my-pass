import unittest 
import pyperclip
from password import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Brian", "Nabiswa", "Bnabz", "mypass")



if __name__ == '__main__':
    unittest.main()