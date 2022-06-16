from flask import Flask, Blueprint, redirect, render_template, request
import datetime

from models.booking import Booking
from models.member import Member
from models.course import Course
import repositories.booking_repository as booking_repo
import repositories.member_repository as member_repo
import repositories.course_repository as course_repo
import repositories.recurring_repository as recurring_repo

courses_blueprint = Blueprint("courses", __name__)

# show all courses
@courses_blueprint.route("/courses")
def bookings():
    courses = course_repo.select_all()
    return render_template("/courses/index.html", courses=courses)


# choose by
@courses_blueprint.route("/courses/search.html")
def update_courses():
    courses = course_repo.select_all()
    return render_template("/courses/search.html", courses=courses)


# choices
@courses_blueprint.route("/courses/<activity>/get_by_name.html", methods=["GET"])
def get_course_by_name(activity):
    course = course_repo.select_by_activity(activity)
    return render_template("courses/show.html", course=course)


@courses_blueprint.route("/courses/<id>/show.html", methods=["GET"])
def get_course(id):
    course = course_repo.select(id)
    return render_template("/courses/show.html", course=course)


# @courses_blueprint.route("/course/<id>/recurring.html", methods=["POST"])
# def this_wont_work(id):
#     course_repo.update_course(id)

#     return redirect("/courses")

# update course
##########
@courses_blueprint.route("/course/<id>", methods=["POST"])
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
    course_date =datetime.date(year_, month_, day_)
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

    course_time =datetime.time(hour_, minute_, second_)
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
    
    course_repo.update(course)
    print(f"****************{recurring}")
    if recurring:
        return render_template("/courses/new_date.html", course =course)
    return redirect("/courses")
    
@courses_blueprint.route("/courses/<id>/new_date.html")
def do_stuff():

     return redirect("/courses")




#########
@courses_blueprint.route("/course/<id>/delete.html", methods=["POST"])
def delete_course(id):
    print("kill em all")
    print(id)

    course_repo.delete(id)
    return redirect("/courses")


@courses_blueprint.route("/courses/recurring.html", methods=["GET"])
def show_recurring():
    recurring_courses = recurring_repo.select_all()
    return render_template(
        "/courses/recurring.html", recurring_courses=recurring_courses
    )


@courses_blueprint.route("/courses/new.html", methods=["GET"])
def new_course():
    return render_template("courses/new.html")


@courses_blueprint.route("/courses/update.html", methods=["POST"])
def create_course():
    activity = request.form["activity"]
    grade = request.form["grade"]
    capacity = request.form["capacity"]
    running = request.form["running"]
    course_date = request.form["course_date"]
    course_time = request.form["course_time"]
    bookings = None
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
    )
    course = course_repo.save(course)
    courses = course_repo.select_all()
    return render_template("courses/index.html", courses=courses)


