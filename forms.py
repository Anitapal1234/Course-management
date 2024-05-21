from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, TimeField, SubmitField
from wtforms.validators import DataRequired

class CourseForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    level = StringField('Level')
    image = StringField('Image')
    description = StringField('Description')
    submit = SubmitField('Submit')

class InstructorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LectureForm(FlaskForm):
    course_id = IntegerField('Course ID', validators=[DataRequired()])
    instructor_id = IntegerField('Instructor ID', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    time = TimeField('Time', validators=[DataRequired()])
    submit = SubmitField('Submit')