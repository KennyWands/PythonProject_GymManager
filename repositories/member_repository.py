from db.run_sql import run_sql
from models.member import Member


def save(member):
    sql = (
        "INSERT INTO members (name, membership, active) VALUES (%s, %s,%s) RETURNING id"
    )
    values = [member.name, member.membership, member.active]
    results = run_sql(sql, values)
    id = results[0]["id"]
    member.id = id
    ###
    return member


def delete(id):
    sql = "DELETE  FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


def select(id):
    sql = "SELECT * FROM members WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]
    member = Member(
        result["name"], result["membership"], result["active"], result["id"]
    )
    return member


def select_by_name(name):
    sql = "SELECT * FROM members WHERE name = %s "
    value = [name]
    result = run_sql(sql, value)[0]
    member = Member(
        result["name"], result["membership"], result["active"], result["id"]
    )
    return member


def select_all():
    member_list = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for result in results:
        member = Member(
            result["name"], result["membership"], result["active"], result["id"]
        )
        member_list.append(member)
    return member_list


def update(member):
    sql = """UPDATE members SET (name, membership, active) 
        =(%s, %s, %s) WHERE id = %s"""
    values = [member.name, member.membership, member.active, member.id]
    run_sql(sql, values)


def get_courses(member):
    member_courses = []
    sql = "SELECT * FROM courses where members_id = %s"
    values = [member.id]
    results = run_sql(sql, values)
    for result in results:
        course = """Course( row["course.activity"],
        row ["course.grade"],
        row ["course.capacity"],
        row ["course.running"],
        row ["course.course_date"],
        row ["course.course_time"],
        row ["course.bookings"],
        row ["course.recurring"]
    )"""
    member_courses.append(course)
    return member_courses
