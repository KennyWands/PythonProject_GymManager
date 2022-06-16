class Recurring:
    def __init__(self, get_course_date, get_course_time, get_course, get_id=None):
        self.course_date = get_course_date
        self.course_time = get_course_time
        self.course = get_course
        self.id = get_id
