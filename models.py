from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(20))
    students = db.relationship('Students', backref='subjects', lazy=True)
    teachers = db.relationship('Teachers', backref='subjects', lazy=True)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"))  # Correct ForeignKey


class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"))


