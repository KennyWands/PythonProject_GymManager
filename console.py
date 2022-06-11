import pdb
import datetime

from models.booking import Booking
import repositories.booking_repository as booking_repo

from models.course import Course
import repositories.course_repository as course_repo

from models.member import Member
import repositories.member_repository as member_repo

booking_repo.delete_all()
course_repo.delete_all()
member_repo.delete_all()

member_1 = Member("alison", True)
member_repo.save(member_1)

member_2 = Member("Bob", False)
member_repo.save(member_2)

member_3 = Member("Cammy", True)
member_repo.save(member_3)

d = datetime.date(2020, 5, 17)
t = datetime.time(9, 1, 00)
course_1 = Course("Aerobics", 1, 10, True, d, t)
course_repo.save(course_1)

course_2 = Course("BoxFit", 2, 20, True, d, t)
course_repo.save(course_2)

course_3 = Course("CrossFit", 3, 30, True, d, t)
course_repo.save(course_3)

booking_1 = Booking(member_1, course_1)
booking_repo.save(booking_1)

booking_2 = Booking(member_2, course_2)
booking_repo.save(booking_2)
