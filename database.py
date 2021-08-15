from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def db_init(backend):
    db.init_app(backend)
    with backend.app_context():
        db.create_all()


class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    txt = db.Column(db.String(12000), nullable=False)
    find_word= db.Column(db.String(50), nullable=False)
    replaced_word = db.Column(db.String(100), nullable=False)
    

def __init__(self, txt, find_word, replaced_word):
        self.txt = txt
        self.find_word = find_word
        self.replaced_word = replaced_word


