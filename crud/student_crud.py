from models.student import Student, Course

def create_student(db, data):
    student = Student(name=data.name)
    student.courses = [Course(title=title) for title in data.courses]
    db.add(student)
    db.commit()
    return student

def get_students(db):
    return db.query(Student).all()

def get_student(db, student_id):
    return db.query(Student).filter(Student.id == student_id).first()

def delete_student(db, student_id):
    student = get_student(db, student_id)
    if not student:
        return None
    db.delete(student)
    db.commit()
    return True

def update_student(db, student_id, data):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        return None

    student.name = data.name
    student.courses.clear()

    for title in data.courses:
        student.courses.append(Course(title=title))

    db.commit()
    db.refresh(student)
    return student