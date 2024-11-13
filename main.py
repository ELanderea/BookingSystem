import requests
import json
from db_utils import get_t_list, add_booking




def get_teacher_list(inst):
    result = requests.get(
        'http://127.0.0.1:5020/teachers/{}'.format(inst),
        headers={'content-type': 'application/json'}
    )
    return result.json()

def get_availability_by_tid(teacher_id):
    result = requests.get(
        'http://127.0.0.1:5020/availability/{}'.format(teacher_id),
        headers={'content-type': 'application/json'}
    )
    return result.json()


def add_new_booking(date, teacher_id, time, student_id):
    booking = {
         "_date": date,
         "teacher_id": teacher_id,
         "time": time,
         "student_id": student_id,
    }

    result = requests.put(
        'http://127.0.0.1:5020/booking',
        headers={'content-type': 'application/json'},
        data=json.dumps(booking)
    )

    return result.json()


def run():
    print('############################')
    print('Welcome to Music School!')
    print('############################')
    print()
    inst = input('What instrument would you like to learn? (trumpet/violin/flute/drums/voice) ')
    print (get_teacher_list(inst))
    teacher_id = input('Please enter the id number of the teacher that you wish to book: ')
    print('####### AVAILABILITY #######')
    print(get_availability_by_tid(teacher_id))
    place_booking = input('Would you like to book an appointment (y/n)?  ')

    book = place_booking == 'y'
    if book:
        cust = input('Enter your student id number: ')
        _date = input('Choose the date you would like to book (e.g. 2024-09-01): ')
        time = input('Choose time based on availability (e.g 15-16): ')
        add_booking(_date, teacher_id, time, cust)
        print("Booking is Successful")
        print()

    print()
    print('See you soon!')




if __name__ == '__main__':
    run()