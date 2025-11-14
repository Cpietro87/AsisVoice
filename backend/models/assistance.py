from models.db import db
from uuid import uuid4
from datetime import datetime, date

class Assistance(db.Model):
    __tablename__ = "assistance"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    student_id = db.Column(db.String(36), db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.String(36), db.ForeignKey('course.id'), nullable=False)

    status = db.Column(db.String(20), default='present', nullable=False)
    date = db.Column(db.Date, nullable=False)
    confidence_score = db.Column(db.Float, nullable=True)

    def __init__(self, student_id, course_id, date=None, status='present', confidence_score=None):
        self.student_id = student_id
        self.course_id = course_id
        self.date = date or date.today()
        self.status = status
        self.confidence_score = confidence_score


    def serialize(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'status': self.status,
            'date': self.date.isoformat(),
            'confidence_score': self.confidence_score
        }

