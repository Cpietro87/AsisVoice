from models.db import db
from uuid import uuid4

class Student(db.Model):
    __tablename__ = "student"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    course_id = db.Column(db.String(36), db.ForeignKey('course.id'), nullable=False)

    voice_sample = db.Column(db.String(200), nullable=True)
    state = db.Column(db.String(20), default='active', nullable=False)

    assistances = db.relationship('Assistance', backref='student', lazy=True)



    def __init__(self, name, surname, dni, course_id, state='active', voice_sample=None):
        self.name = name
        self.surname = surname
        self.dni = dni
        self.course_id = course_id
        self.state = state
        self.voice_sample = voice_sample

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'dni': self.dni,
            'course_id': self.course_id,
            'voice_sample': self.voice_sample,
            'state': self.state
        }