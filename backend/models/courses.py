from models.db import db
from uuid import uuid4

class Course(db.Model):
    __tablename__ = "course"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    name = db.Column(db.String(100), nullable=False)
    shift = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    teacher_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)

    students = db.relationship('Student', backref='course', lazy=True)
    assistances = db.relationship('Assistance', backref='course', lazy=True)

    def __init__(self, name, shift, year, teacher_id):
        self.name = name
        self.shift = shift
        self.year = year
        self.teacher_id = teacher_id


    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'shift': self.shift,
            'year': self.year,
            'teacher_id': self.teacher_id
        }
    