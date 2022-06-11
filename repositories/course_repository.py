from db.run_sql import run_sql
from models.course import Course


def save(course):
    sql = """INSERT INTO courses (activity, grade, capacity, running, course_date, course_time) 
    VALUES (%s, %s, %s,%s, %s, %s) RETURNING id"""
    values = [
        course.activity,
        course.grade,
        course.capacity,
        course.running,
        course.course_date,
        course.course_time,
    ]
    results = run_sql(sql, values)
    id = results[0]["id"]
    course.id = id


def select_all():
    courses_list = []
    sql = "SELECT * FROM courses"
    results = run_sql(sql)
    for result in results:
        course = Course(
            result["activity"],
            result["grade"],
            result["capacity"],
            result["course_date"],
            result["course_time"],
        )
        courses_list.append(course)
    return courses_list


def delete_all():
    sql = "DELETE FROM courses"
    run_sql(sql)

    # delete by id
    #edit