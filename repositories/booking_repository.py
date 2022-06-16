from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member
from models.course import Course
import repositories.member_repository as member_repo
import repositories.course_repository as course_repo


def save(booking):

    sql = """INSERT INTO bookings (member_id, course_id)
             VALUES (%s, %s) RETURNING id"""
    values = [booking.member.id, booking.course.id]

    course = course_repo.select(booking.course.id)
    print(course.bookings)
    print(course.capacity)
    if course.bookings < course.capacity:
        course_repo.update_bookings(booking.course.id)
        print(f"course booking after if{course.bookings}")
        results = run_sql(sql, values)
        id = results[0]["id"]
        booking.id = id
        return booking
    else:
        print("heyyyy")
        return False
    


# def save(booking):
#     sql = """INSERT INTO bookings (member_id, course_id)
#              VALUES (%s, %s) RETURNING id"""
#     values = [booking.member.id, booking.course.id]
#     results = run_sql(sql, values)
#     id = results[0]["id"]
#     booking.id = id
#     return booking

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = member_repo.select(result["member_id"])
    course = course_repo.select(result["course_id"])
    booking = Booking(member, course, result["id"])
    return booking


def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results:
        member = member_repo.select(result["member_id"])
        course = course_repo.select(result["course_id"])
        booking = Booking(member, course, result["id"])
        bookings.append(booking)
    return bookings

def select_by_course(id):
    members_on_course = []
    sql = "SELECT member_id FROM bookings WHERE course_id = %s"
    value = [id]
    results = run_sql(sql,value) 
    for result in results:
        member = member_repo.select(result["member_id"])
       
        members_on_course.append(member)
    return members_on_course

def select_by_name(activity):
    course =course_repo.select_by_activity(activity)
    members_on_course = []
    sql = "SELECT member_id FROM bookings WHERE course_id = %s"
    value = [course.id]
    results = run_sql(sql,value) 
    for result in results:
        member = member_repo.select(result["member_id"])
      
        members_on_course.append(member)
    return members_on_course
    
    




   