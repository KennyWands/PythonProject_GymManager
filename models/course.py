class Course:
    def __init__(
        self,
        get_activity,
        get_grade,
        get_capacity,
        get_running,
        get_course_date,
        get_course_time,
        get_bookings,
        get_recurring,
        get_id=None,
    ):
        self.activity = get_activity
        self.grade = get_grade
        self.capacity = get_capacity
        self.running = get_running
        self.course_date = get_course_date
        self.course_time = get_course_time
        self.bookings = get_bookings
        self.recurring = get_recurring
        self.id = get_id
