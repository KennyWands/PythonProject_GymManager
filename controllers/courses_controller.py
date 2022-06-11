from flask import Flask, Blueprint, redirect, render_template, request


from models.booking import Booking
from models.member import Member
from models.course import Course
import repositories.booking_repository as booking_repo
import repositories.member_repository as member_repo
import repositories.course_repository as course_repo

courses_blueprint = Blueprint("courses", __name__)


@courses_blueprint.route("/courses")
def bookings():
    courses = course_repo.select_all()
    return render_template("courses/index.html", courses=courses)
