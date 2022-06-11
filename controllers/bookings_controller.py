from flask import Flask, Blueprint, redirect, render_template, request


from models.booking import Booking
from models.member import Member
from models.course import Course
import repositories.booking_repository as booking_repo
import repositories.member_repository as member_repo
import repositories.course_repository as course_repo

bookings_blueprint = Blueprint("bookings", __name__)


@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repo.select_all()
    return render_template("bookings/index.html", bookings=bookings)
