
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, Course, Instructor, Lecture

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///course_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/courses')
def courses():
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)

@app.route('/instructors')
def instructors():
    instructors = Instructor.query.all()
    return render_template('instructors.html', instructors=instructors)

@app.route('/lectures')
def lectures():
    lectures = Lecture.query.all()
    return render_template('lectures.html', lectures=lectures)

@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        name = request.form['name']
        level = request.form['level']
        image = request.form['image']
        description = request.form['description']
        course = Course(name=name, level=level, image=image, description=description)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('courses'))
    return render_template('add_course.html')

@app.route('/add_instructor', methods=['GET', 'POST'])
def add_instructor():
    if request.method == 'POST':
        name = request.form['name']
        instructor = Instructor(name=name)
        db.session.add(instructor)
        db.session.commit()
        return redirect(url_for('instructors'))
    return render_template('add_instructor.html')


from forms import LectureForm
@app.route('/add_lecture', methods=['GET', 'POST'])
def add_lecture():
    form = LectureForm()
    if form.validate_on_submit():
        lecture = Lecture(
            course_id=form.course_id.data,
            instructor_id=form.instructor_id.data,
            date=form.date.data,
            time=form.time.data
        )
        l_object = Lecture.query.all()
        for l in l_object:
            if l.instructor_id==form.instructor_id.data and l.date==form.date.data :
               return redirect(url_for('lectures'))
            
        db.session.add(lecture)
        db.session.commit()
        flash('Lecture added successfully.')
        return redirect(url_for('lectures'))
    courses = Course.query.all()
    instructors = Instructor.query.all()
    return render_template('add_lecture.html', form=form, courses=courses, instructors=instructors)
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
