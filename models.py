
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    _tablename_ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(50))
    image = db.Column(db.String(255))
    description = db.Column(db.Text)

    def _repr_(self):
        return f'<Course {self.name}>'

class Instructor(db.Model):
    _tablename_ = 'instructors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def _repr_(self):
        return f'<Instructor {self.name}>'

class Lecture(db.Model):
    _tablename_ = 'lectures'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    course = db.relationship('Course', backref=db.backref('lectures', lazy=True))
    instructor = db.relationship('Instructor', backref=db.backref('lectures', lazy=True))

    def _repr_(self):
        return f'<Lecture {self.course.name} by {self.instructor.name} on {self.date} at {self.time}>'