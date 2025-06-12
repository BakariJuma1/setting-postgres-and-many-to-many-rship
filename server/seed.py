from app import app
from models import db, Student, Subject, Teacher

with app.app_context():
    db.drop_all()
    db.create_all()

    student1 = Student(name='joe', age=20)
    student2 = Student(name='Brian', age=24)

    subject1 = Subject(name='Math')
    subject2 = Subject(name='English')

    teacher1 = Teacher(name='Ken')
    teacher2 = Teacher(name='Kuria')

    # Assign relationships (only from one direction)
    student1.subjects.append(subject1)
    student1.teachers.append(teacher1)

    student2.subjects.extend([subject1, subject2])
    student2.teachers.append(teacher2)

    subject1.teachers.append(teacher1)  # ✅ Fine to do this once

    db.session.add_all([student1, student2, subject1, subject2, teacher1, teacher2])
    db.session.commit()
