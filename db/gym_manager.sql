DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS members;

CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    membership BOOL,
    active BOOL
);
CREATE TABLE courses(
    id SERIAL PRIMARY KEY,
    activity VARCHAR (255),
    grade INT,
    capacity INT,
    running BOOL,
    course_date DATE,
    course_time TIME

);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    member_id SERIAL REFERENCES members(id),
    course_id SERIAL REFERENCES courses(id)
);

SELECT members.name, courses.activity FROM members -- get these
INNER JOIN bookings                                 -- via
ON bookings.member_id = members.id
INNER JOIN courses
ON courses.id = bookings.course_id;
