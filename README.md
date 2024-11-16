# Music School Booking System

## Overview

This project is an API designed to function as a booking system for a music school, facilitating seamless student-teacher interactions. The core scenario for this implementation is set before the first week of a new term, where students, equipped with unique IDs, need to view the list of available teachers, check their availability, and book their first lessons.

## Key Features

- **Database Structure**: The database schema is contained in `musicschool.sql`, comprising three tables: `students`, `teachers`, and `bookings`. This structure ensures normalized data storage and efficient query handling.
- **Modular Code Design**: Essential database operations are implemented as modular functions within `db_utils.py`, ensuring maintainable and scalable code.
- **Flask API**: The `app.py` file establishes RESTful API endpoints using Flask for seamless data access and bookings.
- **Client-Side Interaction**: The `main.py` file acts as the client interface, simulating user interaction with the API.

## Configuration Note

The `config.py` file includes placeholders for host, user, and password details. Update these fields with your specific database credentials before running the system.

## Database Design

The system uses three tables:

1. **`students`**: Holds student records.
2. **`teachers`**: Stores information about teachers and their specialties.
3. **`bookings`**: Manages lesson booking data.

This structure enables effective data relationships and optimal performance.

## Core Functions

### `db_utils.py`

1. **`_connect_to_db()`**: Establishes a connection to the database and returns a connection object. It uses `mysql.connector` and incorporates basic exception handling.
2. **`get_t_list(instrument)`**: Queries the `teachers` table to return a list of teachers for a specified instrument.
3. **`get_availability(teacher_id)`**: Retrieves a specific teacher's availability from the `bookings` table, mapping results to indicate slots as "Available" or "Not Available."
4. **`add_booking(student_id, teacher_id, time_slot)`**: Adds a new booking record into the `bookings` table.

### Exception Handling

All database functions include basic error handling for operational robustness.

## API Endpoints

The `app.py` file establishes endpoints for interaction with the booking system:

- **Homepage** (`@app.route('/')`): Welcomes students to the system.
- **Get Teacher List** (`@app.route('/teachers/<instrument>')`): Uses `get_t_list` to return a list of teachers for a specific instrument in JSON format.
- **Check Availability** (`@app.route('/availability/<teacher_id>')`): Uses `get_availability` to return a teacher’s availability based on their ID in JSON format.
- **Create Booking** (`@app.route('/booking/<student_id>', methods=['PUT'])`): Uses `add_booking` to create a new booking for a student, with results returned in JSON format.

## Client-Side Interaction (`main.py`)

The `main.py` file simulates user interaction with the API, demonstrating the following flow:

1. **Display Teacher List**: Retrieves and displays teachers for a specific instrument.
2. **Check Availability**: Shows a teacher's availability based on their ID.
3. **Create a Booking**: Prompts the user to create a booking and submits it via the API.

### Functions:

- **`get_teacher_list(instrument)`**: Sends a GET request to the API to retrieve the teacher list.
- **`get_availability_by_tid(teacher_id)`**: Sends a GET request for teacher availability.
- **`add_new_booking(student_id, teacher_id, time_slot)`**: Sends a PUT request to create a new booking.

## Future Enhancements

With more development time, potential improvements could include:

- Viewing all bookings for a specific student.
- The ability to cancel or modify bookings.
- Generating payslips for teachers based on completed lessons.
