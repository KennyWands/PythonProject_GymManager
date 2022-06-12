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
