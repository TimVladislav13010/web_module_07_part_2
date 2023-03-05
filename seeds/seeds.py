from datetime import datetime

from src.models import Teacher, Student, Discipline, Grade, Group
from src.db import session


def create():
    return {"teacher": create_teacher,
            "student": create_student,
            "group": create_group,
            "discipline": create_discipline,
            "grade": create_grade}


def create_teacher(value):
    teacher = Teacher(fullname=str(value))
    session.add(teacher)
    session.commit()
    return f"Teacher create: {value}"


def create_student(value):
    student = Student(fullname=str(value))
    session.add(student)
    session.commit()
    return f"Student create: {value}"


def create_group(value):
    group = Group(name=str(value))
    session.add(group)
    session.commit()
    return f"Group create: {value}"


def create_discipline(value):
    discipline = Discipline(name=str(value))
    session.add(discipline)
    session.commit()
    return f"Discipline create: {value}"


def create_grade(value):
    try:
        grade = Grade(grade=float(value))
    except ValueError as er:
        return f"Grade must be int or float"
    session.add(grade)
    session.commit()
    return f"Grade create: {value}"


def update():
    return {"teacher": update_teacher,
            "student": update_student,
            "group": update_group,
            "discipline": update_discipline,
            "grade": update_grade}


def update_teacher(id_, value):
    teacher = session.query(Teacher).get(id_)

    try:
        teacher.fullname = value
    except AttributeError:
        return f"Failed: Teacher must be created."

    session.add(teacher)
    session.commit()
    return f"Teacher {id_}, update {value}."


def update_student(id_, value):
    student = session.query(Student).get(id_)

    try:
        student.fullname = value
    except AttributeError:
        return f"Failed: Student must be created."

    session.add(student)
    session.commit()
    return f"Student {id_}, update {value}."


def update_group(id_, value):
    group = session.query(Group).get(id_)

    try:
        group.name = value
    except AttributeError:
        return f"Failed: Group must be created."

    session.add(group)
    session.commit()
    return f"Group {id_}, update {value}."


def update_discipline(id_, value):
    discipline = session.query(Discipline).get(id_)

    try:
        discipline.name = value
    except AttributeError:
        return f"Failed: Discipline must be created."

    session.add(discipline)
    session.commit()
    return f"Discipline {id_}, update {value}."


def update_grade(id_, value):
    grade = session.query(Grade).get(id_)

    try:
        grade.date_of = datetime.now()
        grade.grade = float(value)
    except Exception:
        return f"Failed: Grade must be created. Or must be float."

    session.add(grade)
    session.commit()
    return f"Grade {id_}, update {value}."

