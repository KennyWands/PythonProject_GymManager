from db.run_sql import run_sql
from models.booking import Booking


def save(booking):
    sql = """INSERT INTO bookings (member_id, course_id)
    VALUES (%s, %s) RETURNING id"""
    values = [booking.member.id, booking.course.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    booking.id = id
    return booking


# delete all
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)



