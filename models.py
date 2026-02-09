from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Doc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), unique=True, nullable=False)
    def __repr__(self):
        return f'<Doc {self.title}>'
