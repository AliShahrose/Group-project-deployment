import unittest
import time
from main import User, Prizes, Questions, WrongAnswers, Games, init_db, clear_db


class TestDB(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_add_user(self):

        for i in range(1):
            usrname = "jakob_" + str(i)
            User.add_user(usrname, 'paswrd123')


    def test_get_user(self):
        user_list = User.get_all_users()

if __name__=='__main__':
    init_db()
    unittest.main()


