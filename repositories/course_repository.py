from db.run_sql import run_sql
from models.course import Course

from flask import Flask, Blueprint, redirect, render_template, request
import datetime


def save(course):
    sql = """INSERT INTO courses (activity, grade, capacity,
     running, course_date, course_time, bookings, recurring) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"""
    values = [
        course.activity,
        course.grade,
        course.capacity,
        course.running,
        course.course_date,
        course.course_time,
        course.bookings,
        course.recurring,
    ]
    results = run_sql(sql, values)
    id = results[0]["id"]
    course.id = id


def delete(id):
    sql = "DELETE  FROM courses WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM courses"
    run_sql(sql)


def select(id):
    sql = "SELECT * FROM courses WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]
    course = Course(
        result["activity"],
        result["grade"],
        result["capacity"],
        result["running"],
        result["course_date"],
        result["course_time"],
        result["bookings"],
        result["recurring"],
        result["id"],
    )
    return course


def select_by_activity(activity):
    sql = "SELECT * FROM courses WHERE activity = %s "
    value = [activity]
    result = run_sql(sql, value)[0]
    course = Course(
        result["activity"],
        result["grade"],
        result["capacity"],
        result["running"],
        result["course_date"],
        result["course_time"],
        result["bookings"],
        result["recurring"],
        result["id"],
    )
    return course


def select_all():
    courses_list = []
    sql = "SELECT * FROM courses"
    results = run_sql(sql)
    for result in results:
        course = Course(
            result["activity"],
            result["grade"],
            result["capacity"],
            result["running"],
            result["course_date"],
            result["course_time"],
            result["bookings"],
            result["recurring"],
            result["id"],
        )
        courses_list.append(course)
    return courses_list


def update(course):
    sql = """UPDATE courses SET (activity, grade, capacity,running, 
             course_date, course_time, bookings, recurring) 
             =(%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"""
    values = [
        course.activity,
        course.grade,
        course.capacity,
        course.running,
        course.course_date,
        course.course_time,
        course.bookings,
        course.recurring,
        course.id,
    ]
    print("hello")
    run_sql(sql, values)


def update_bookings(id):
    sql = "UPDATE courses SET bookings=bookings+1  WHERE id = %s"
    value = [id]
    run_sql(sql, value)


def update_course(id):
    activity = request.form["activity"]
    print(activity)
    grade = request.form["grade"]
    print(grade)
    capacity = request.form["capacity"]
    print(capacity)
    running = request.form["running"]
    print(running)
    date = request.form["course_date"]
    print(f"date from HTML {date}")
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    year_ = int(year)
    month_ = int(month)
    day_ = int(day)
    print(year_)
    print(month_)
    print(day_)
    course_date = datetime.date(year_, month_, day_)
    print(f"date after convert{course_date}")

    print("8888888888888888888")
    time = request.form["course_time"]
    print(time)
    hour = time[0:2]
    minute = time[3:5]
    second = time[6:8]
    hour_ = int(hour)
    minute_ = int(minute)
    second_ = int(second)
    print(hour)
    print(minute)
    print(second)

    course_time = datetime.time(hour_, minute_, second_)
    # course_date = request.form["course_date"]
    # print(course_date)
    # course_time = request.form["course_time"]
    bookings = request.form["bookings"]
    recurring = request.form["recurring"]
    course = Course(
        activity,
        grade,
        capacity,
        running,
        course_date,
        course_time,
        bookings,
        recurring,
        id,
    )
    print(f"****************{course.activity}")
    # course_repo.
    update(course)
