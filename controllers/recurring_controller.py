from flask import Flask, Blueprint, redirect, render_template, request


from models.booking import Booking
from models.member import Member
from models.course import Course
from models.recurring import Recurring

import repositories.booking_repository as booking_repo
import repositories.member_repository as member_repo
import repositories.course_repository as course_repo
import repositories.recurring_repository as recurring_repo

recurring_blueprint = Blueprint("recurring", __name__)

@recurring_blueprint.route("/courses/<id>/new_date.html", methods = ["POST"])
def add_recurring_date(id):
    date = request.form["course_date"]
    time = request.form["course_time"]
    course_id = id
    recurring = Recurring(date, time, course_id)
    recurring_repo.save(recurring)
    recurring_courses = recurring_repo.select_all()
    return render_template("/courses/recurring.html",recurring_courses =recurring_courses)