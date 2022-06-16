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
    courses = course_repo.select_all()
    bookings = booking_repo.select_all()
    return render_template("/bookings/index.html", courses=courses, bookings=bookings)


@bookings_blueprint.route("/bookings/new_booking.html", methods=["GET"])
def get_new_booking():
    members = member_repo.select_all()
    courses = course_repo.select_all()
    return render_template(
        "/bookings/new_booking.html",
        members=members,
        courses=courses,
        bookings=bookings,
    )


@bookings_blueprint.route("/bookings/add_new", methods=["POST"])
def add_new_booking():
    member_id = request.form["member.id"]
    course_id = request.form["course.id"]
    member = member_repo.select(member_id)
    course = course_repo.select(course_id)

    booking = Booking(member, course)
    not_full = booking_repo.save(booking)
    if not_full == False:
        return render_template("/bookings/full.html")
    return redirect("/bookings")


@bookings_blueprint.route("/bookings/<id>/show.html", methods=["GET"])
def get_course_members(id):
    course = course_repo.select(id)
    members = booking_repo.select_by_course(id)

    return render_template("/bookings/show.html", course=course, members=members)


@bookings_blueprint.route("/bookings/<activity>/show_by_name.html", methods=["GET"])
def get_course_members_activity(activity):
    course = course_repo.select_by_activity(activity)
    members = booking_repo.select_by_name(activity)

    return render_template("/bookings/show.html", course=course, members=members)
