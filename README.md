# PythonProject_GymManager
Gym management app 

To run the Program:

In the terminal type
1. 'CREATEDB gym_manager' to create the database
2. 'psql -d gym_manager -f db/gym_manager.sql' to link the database
3. 'python3 console.py' to populate the database with test data
4. 'flask run' to launch the server

In your browser navigate to '127.0.0.1:5002 '

Project Brief

Build an app allowing a local gym manage memberships and register members for courses.

## MVP

- The app should allow the gym to create and edit `Member`s.
- The app should allow the gym to create and edit `Course`s.
- The app should allow the gym to book `Member`s on specific `Course`s.
- The app should show a list of all upcoming `Course`s.
- The app should show all `Member`s that are booked in for a particular course.

## Inspired By

Glofox, Pike13

## Possible Extensions

- `Course`s could have a maximum capacity, and users can only be added while there is space remaining.
- The gym could be able to give its `Member`s Premium or Standard membership. Standard `Member`s can only be signed up for `Course`s during off-peak hours.
- The Gym could mark `Member`s and `Course`s as active/deactivated. Deactivated `Member`s/`Course`s will not appear when creating bookings.

Technologies:

Python
Flask
PSQL
