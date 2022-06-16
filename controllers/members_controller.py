from flask import Flask, Blueprint, redirect, render_template, request


from models.booking import Booking
from models.member import Member
from models.course import Course
import repositories.booking_repository as booking_repo
import repositories.member_repository as member_repo
import repositories.course_repository as course_repo

members_blueprint = Blueprint("members", __name__)

# show all members
@members_blueprint.route("/members")
def members():
    members = member_repo.select_all()
    return render_template("members/index.html", members=members)


# choose by
@members_blueprint.route("/members/search.html")
def update_member():
    members = member_repo.select_all()
    return render_template("members/search.html", members=members)


# choices
@members_blueprint.route("/members/<id>/show.html", methods=["GET"])
def get_member(id):
    member = member_repo.select(id)
    return render_template("/members/show.html", member=member)


@members_blueprint.route("/members/<name>/get_by_name.html", methods=["GET"])
def get_member_by_name(name):
    member = member_repo.select_by_name(name)
    return render_template("members/show.html", member=member)


# update member
@members_blueprint.route("/member/<id>", methods=["POST"])
def add_amended_member(id):
    name = request.form["name"]
    membership = request.form["membership"]
    active = request.form["active"]
    member = Member(name, membership, active, id)
    member_repo.update(member)
    return redirect("/members")


# delete member
@members_blueprint.route("/member/<id>/delete.html", methods=["POST"])
def delete_member(id):
    member_repo.delete(id)
    return redirect("/members")

#add member to course
@members_blueprint.route("/members/<id>/course", methods=["POST"])
def add_member_course():
    pass


@members_blueprint.route("/members/new.html", methods=["GET"])
def new_member():

    return render_template("members/new.html", members=members)


@members_blueprint.route("/members/add.html", methods=["POST"])
def create_member():
    name = request.form["name"]
    membership = request.form["membership"]
    active = request.form["active"]
    member = Member(name, membership, active)
    member = member_repo.save(member)
    members = member_repo.select_all()
    return render_template("members/index.html", members=members)
