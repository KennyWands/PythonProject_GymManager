from db.run_sql import run_sql
from models.member import Member


def save(member):
    sql = "INSERT INTO members (name, membership) VALUES (%s, %s) RETURNING id"
    values = [member.name, member.membership]
    results = run_sql(sql, values)
    id = results[0]["id"]
    member.id = id


def select_all():
    member_list = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for result in results:
        member = Member(result["name"], result["id"])
        member_list.append(member)


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)
