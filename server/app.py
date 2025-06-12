from flask import Flask,make_response
from flask_migrate import Migrate
from models import db,Student,Subject,Teacher

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://user_one:1234@localhost:5432/schooldb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False

migrate = Migrate(app,db)

db.init_app(app)


@app.route('/')
def index():
    return("<p>Welcome to the school management app</p>")

@app.route('/students/<int:id>')
def view_student(id):
    student = Student.query.filter(Student.id == id).first()

    if student:
        # convert list into string separated by comma
        subjects = ",".join([subject.name for subject in student.subjects])
        teachers = ",".join([teacher.name for teacher in student.teachers])

        response_body = f"<p>I am  {student.name} aged {student.age}  learning {subjects} taught by {teachers}</p>"
        response_status = 200
    else:
        response_body = f"<p>This students dont exist</p>"    
        response_status = 404
    response = make_response(response_body,response_status)  
    return response   
   
@app.route('/subjects/<int:id>')
def view_subject(id):
    subject = Subject.query.filter(Subject.id == id).first()

    if subject:
        students = ",".join([student.name for student in subject.students])   
        teachers = ",".join([teacher.name for teacher in subject.teachers])

        response_body = (
            f"<p>Subject: {subject.name}<br>"
            f"Students: {students}<br>"
            f"Teachers: {teachers}</p>"
        )
          
        response_status = 200
    else:
        response_body = f"<p>This subject dont exist</p>"    
        response_status = 404
    response = make_response(response_body,response_status)  
    return response    





if __name__ == "__main__":
    app.run(port=5555,debug=True)