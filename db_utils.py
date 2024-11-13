from config import USER, HOST, PASSWORD
import mysql.connector


class DbConnectionError(Exception):
    pass


# Standard Connect to DB Function which can be used throughout.

def _connect_to_db(db_name):
    """
    Connect to a database
    :param db_name:name of the database you want to connect to
    :return:a connection object
    """
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def _map_values(schedule):
    mapped = []
    for item in schedule:
        mapped.append({
            'bookingdate': item[0],
            'teacher_id': item[1],
            'teacher inst': item[2],
            '10-11': 'Not Available' if item[3] == 1 else 'Available',
            '11-12': 'Not Available' if item[5] == 1 else 'Available',
            '12-13': 'Not Available' if item[7] == 1 else 'Available',
            '13-14': 'Not Available' if item[9] == 1 else 'Available',
            '14-15': 'Not Available' if item[11] == 1 else 'Available',
            '15-16': 'Not Available' if item[13] == 1 else 'Available',
            '16-17': 'Not Available' if item[15] == 1 else 'Available',
            '17-18': 'Not Available' if item[17] == 1 else 'Available'
        })
    return mapped


def get_t_list(inst):
    try:
        # Set up a connection to our DB
        db_name = "musicschool"
        db_connection = _connect_to_db(db_name)
        # Set up a cursor object that will execute queries and retrieve query results
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")
        query = """SELECT 
        teacher_id, teacher_first_name, teacher_last_name, teacher_instrument 
        FROM teachers 
        WHERE teacher_instrument = '{}'""".format(inst)
        cur.execute(query)
        result = cur.fetchall()  # This is a list with db records where each record is a tuple
        # Iterate over result set and print them out
        print(result)
        return result
        # Close the cursor object
        cur.close()
    except Exception:
        raise DbConnectionError("Failed to read data from the DB")
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection is closed')


def get_availability(teacher_id):
    availability = []
    try:
        # Set up a connection to our DB
        db_name = "musicschool"
        db_connection = _connect_to_db(db_name)
        # Set up a cursor object that will execute queries and retrieve query results
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        query = """SELECT * FROM bookings 
        WHERE teacher_id = '{}'""".format(teacher_id)

        cur.execute(query)
        result = cur.fetchall()  # This is a list with db records where each record is a tuple

        availability = _map_values(result)
        print(availability)
        return availability
        # Close the cursor object
        cur.close()
    except Exception:
        raise DbConnectionError("Failed to read data from the DB")
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection is closed')


def add_booking(_date, teacher_id, time, student_id):
    try:
        # Set up a connection to our DB
        db_name = "musicschool"
        db_connection = _connect_to_db(db_name)
        # Set up a cursor object that will execute queries and retrieve query results
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        query = """
        UPDATE bookings
        SET
            `{time}` = 1,
            `{time_id}` = '{student_id}'
        WHERE bookingdate = '{date}' AND teacher_id = '{teacher_id}'
        """.format(time=time, time_id=time + '-student-id', student_id=student_id, date=_date, teacher_id=teacher_id)
        cur.execute(query)
        db_connection.commit()
        print("You have booked your lesson for {time} on {_date}.".format(time=time, _date=_date))
        cur.close()
    except Exception:
        raise DbConnectionError("Failed to read data from the DB")
    finally:
        if db_connection:
            db_connection.close()
            print('DB connection is closed')
