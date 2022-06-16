from unittest import result
from db.run_sql import run_sql

from models.booking import Booking
from models.member import Member
from models.course import Course
from models.recurring import Recurring

import repositories.member_repository as member_repo
import repositories.course_repository as course_repo


def save(recurring):
    sql = """INSERT INTO recurring_events(course_date, course_time)
             VALUES (%s, %s) RETURNING id"""
    values = [recurring.course_date, recurring.course_time]
    result = run_sql(sql, values)
    id = result[0]["id"]
    recurring.id = id


def select_all():
    recurring_list = []
    sql = "SELECT * FROM recurring_events"
    results = run_sql(sql)
    for result in results:
        course = course_repo.select(result["course_id"])
        event = Recurring(
            result["course_date"], result["course_time"], course, result["course_id"]
        )
        recurring_list.append(event)
        print(f"************{recurring_list[0].course_date}")
    return recurring_list
