import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='password', server='127.0.0.1:3306', database='test1')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def init_db():
    db.drop_all()
    db.create_all()
    print("DB init complete, wiped and started")


def clear_db():
    db.session.commit()
    db.drop_all()
    db.create_all()
    print(" Dropped all tables\n ________________________")


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    points = db.Column(db.Integer)
    high_score = db.Column(db.Integer)
    is_admin = db.Column(db.Boolean)
    password = db.Column(db.String(80))
    current_game = db.Column(db.Integer, db.ForeignKey('games.id'))
    prizes = db.Column(db.Integer, db.ForeignKey('prizes.id'))

    def __repr__(self):
        return "user; " + self.username + " points: " + str(self.points)

    def __init__(self, username, password):
        self.username = username
        self.points = 0
        self.high_score = 0
        self.is_admin = False
        self.password = password

    def update_points(self, amount):
        self.points = self.points + amount
        db.session.commit()

    def set_new_high_score(self, new_score):
        self.high_score = new_score

    @staticmethod
    def add_user(username, password):
        user = User(username, password)
        try:
            db.session.add(user)
            db.session.commit()
            return True
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            return False

    @staticmethod
    def set_admin(username, boolean):
        user = User.query.filter_by(username=username).first()
        user.is_admin = boolean
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_user_info(username):
        user = User.query.filter_by(username=username).first()
        return user

    @staticmethod
    def get_all_users():
        return User.query.all()

    def purchase_prize(self, prize_id):
        prize = Prizes.query.filter_by(id=prize_id).first()
        if self.points >= prize.cost:
            self.points = self.points - prize.cost
            self.prizes = prize.id
            db.session.commit()

    def join_game(self, game_id):
        game = Games.query.filter_by(id=game_id).first()
        self.current_game = game.id
        db.session.commit()


class Games(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    questions = db.relationship("Questions", backref=db.backref('games', lazy=True))
    participants = db.relationship("User", backref=db.backref('games', lazy=True))

    @staticmethod
    def get_all_games():
        return Games.query.all()

    @staticmethod
    def get_game_info(g_id):
        game = User.query.filter_by(id=g_id).first()
        return game


class Prizes(db.Model):
    __tablename__ = 'prizes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    cost = db.Column(db.Integer)
    description = db.Column(db.String(256))
    owned_by = db.relationship("User", backref=db.backref('user', lazy=True))

    def __init__(self, name, cost, description):
        self.name = name
        self.cost = cost
        self.description = description

    @staticmethod
    def get_all_prizes():
        return Prizes.query.all()

    @staticmethod
    def add_prize(name, cost, description):
        prize = Prizes(name, cost, description)
        db.session.add(prize)
        db.session.commit()

    @staticmethod
    def remove_prize(p_id):
        prize = Questions.query.filter_by(id=p_id).first()
        db.session.remove(prize)
        db.session.commit()

    @staticmethod
    def get_prize_from_name(prize_name):
        return Prizes.query.filter_by(name=prize_name).first()

    @staticmethod
    def get_prize_from_id(p_id):
        return Prizes.query.filter_by(id=p_id).first()

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(80), unique=True)
    correct_ans = db.Column(db.String(80))
    difficulty = db.Column(db.Integer)
    category = db.Column(db.String(80))
    wrong_ans = db.relationship("WrongAnswers", backref=db.backref('questions', lazy=True))
    fk_games = db.Column(db.Integer, db.ForeignKey('games.id'))

    def __init__(self, question, correct_ans, difficulty, category):
        self.question = question
        self.correct_ans = correct_ans
        self.difficulty = difficulty
        self.category = category

    @staticmethod
    def add_question(question, correct_ans, difficulty, category):
        question = Questions(question, correct_ans, difficulty, category)
        db.session.add(question)
        db.session.commit()

    @staticmethod
    def remove_question(q_id):
        question = Questions.query.filter_by(id=q_id).first()
        db.session.remove(question)
        db.session.commit()

    @staticmethod
    def get_all_questions():
        return Questions.query.all()

    def add_wrong_ans(self, text):
        w = WrongAnswers(text, self.id)
        db.session.add(w)
        db.session.commit()


class WrongAnswers(db.Model):
    __tablename__ = 'wrong_answers'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    answer_text = db.Column(db.String(80))

    def __init__(self, a_text, q_id):
        self.question_id = q_id
        self.answer_text = a_text

    @staticmethod
    def get_wrong_answers(question_id):
        wrong_answers = WrongAnswers.query.filter_by(question_id=question_id).all()
        return wrong_answers

    @staticmethod
    def add_wrong_answers(answer_text, q_id):
        wrong_answer = WrongAnswers(answer_text, q_id)
        db.session.add(wrong_answer)
        db.session.commit()

    @staticmethod
    def remove_wrong_answers(wa_id):
        wa = WrongAnswers.query.filter_by(id=wa_id).first()
        db.session.remove(wa)
        db.session.commit()

    @staticmethod
    def get_all_wrong_answers():
        return WrongAnswers.query.all()


if __name__ == '__main__':
    init_db()
