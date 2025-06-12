from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,String,Integer,MetaData,ForeignKey

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

# association table between students and subjects stores 
student_subject = db.Table(
    'student_subject',
    metadata,
    db.Column('student_id',db.Integer,ForeignKey(
        'students.id'),primary_key=True),
    db.Column('subject_id',db.Integer,ForeignKey(
        'subjects.id'),primary_key=True)
)

# association table between subjects and teachers
subject_teacher = db.Table(
    'subject_teacher',
    metadata,
    db.Column('subject_id',db.Integer,ForeignKey(
        'subjects.id'),primary_key=True),
    db.Column('teacher_id',db.Integer,ForeignKey(
        'teachers.id'),primary_key=True)
)

# association table between students and teachers 
student_teachers = db.Table(
    'student_teacher',
    metadata,
    db.Column('student_id',db.Integer,ForeignKey(
        'students.id'),primary_key=True),
    db.Column('teacher_id',db.Integer,ForeignKey(
        'teachers.id'),primary_key=True)
)
class Student(db.Model):
    __tablename__ = "students"

    id = Column(Integer(),primary_key=True)
    name = Column(String())
    age = Column(String())

    subjects = db.relationship(
        'Subject',secondary=student_subject,back_populates='students'
    )
    teachers = db.relationship(
        'Teacher',secondary=student_teachers,back_populates='students'
    )

class Subject(db.Model):
    __tablename__ = "subjects"

    id =Column(Integer(),primary_key=True)
    name = Column(String())
 

    students = db.relationship(
        'Student',secondary=student_subject,back_populates='subjects'
    )
    teachers = db.relationship(
        'Teacher',secondary=subject_teacher,back_populates='subjects'
    )

class Teacher(db.Model):
    __tablename__ = "teachers"

    id =Column(Integer(),primary_key=True)
    name = Column(String())
   

    students = db.relationship(
        'Student',secondary=student_teachers,back_populates='teachers'
    )
    subjects = db.relationship(
        'Subject',secondary=subject_teacher,back_populates='teachers'
    )