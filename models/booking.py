class Booking:
    def __init__(self, get_member, get_course, get_id=None):
        self.member = get_member
        self.course = get_course
        self.id = get_id
