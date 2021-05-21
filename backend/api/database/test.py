import unittest
import time
from main import User, Prizes, Questions, WrongAnswers, Games, init_db, clear_db

class TestDB(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_empty_db(self):
        print("check empty db test")
        self.assertEqual(len(User.get_all_users()), 0)
        self.assertEqual(len(Games.get_all_games()), 0)
        self.assertEqual(len(Prizes.get_all_prizes()), 0)
        self.assertEqual(len(Questions.get_all_questions()), 0)
        self.assertEqual(len(WrongAnswers.get_all_wrong_answers()), 0)

    def test_add_user(self):
        print("Add users test")
        User.add_user('Jakob22', 'paswrd123')
        User.add_user('Olivia221', 'aaaaa')
        self.assertEqual(len(User.get_all_users()), 2)
        clear_db()

    def test_add_prize(self):
        print("Add prize test")
        Prizes.add_prize("teddybear", 250)
        self.assertEqual(len(Prizes.get_all_prizes()), 1)
        clear_db()

    def test_add_question(self):
        print("Add question test")
        Questions.add_question("how far can you swim?", "3km", 10, "swim")
        self.assertEqual(len(Questions.get_all_questions()), 1)
        clear_db()

    def test_add_wrong_answer(self):
        print("Add W-answer test")
        Questions.add_question("how far can you swim?", "3km", 10, "swim")
        q = Questions.query.filter_by(question="how far can you swim?").first()
        q.add_wrong_ans("tjena")
        wa_list=WrongAnswers.get_wrong_answers(q.id)
        for i in wa_list:
            print(i.answer_text)
        self.assertEqual(len(WrongAnswers.get_all_wrong_answers()), 1)
        clear_db()

    def test_prize_rel(self):
        print("Prize relation test")
        User.add_user('Jakob22', 'paswrd123')
        user = User.get_user_info("Jakob22")
        Prizes.add_prize("monkey", 666)
        user.update_points(700)
        prize = Prizes.get_prize_from_name("monkey")
        print(prize)
        user.purchase_prize(prize.id)
        print(user.points)
        clear_db()


if __name__=='__main__':
    init_db()
    unittest.main()

