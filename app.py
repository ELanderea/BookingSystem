from flask import Flask, jsonify, request
from db_utils import get_t_list, get_availability, add_booking

app = Flask(__name__)


# API Landing Page

@app.route('/')
def home():
    return "Welcome to Music School!"

# Listing teachers by Instrument for Students to View

@app.route('/teachers/<instrument>')
def teachers(instrument):
    inst = get_t_list(instrument)
    return jsonify(inst)


# Getting Information About Availability for a Specific Teacher

@app.route('/availability/<teacher_id>')
def availability(teacher_id):
    res = get_availability(teacher_id)
    return jsonify(res)


# Booking a Lesson for a Specific Teacher

@app.route('/booking/<student_id>', methods=['PUT'])
def book_lesson():
    booking = request.get_json()
    add_booking(
        _date=booking['_date'],
        teacher_id=booking['teacher_id'],
        time=booking['time'],
        student_id=booking['student_id']
    )
    return booking



if __name__ == '__main__':
    app.run(debug=True, port=5020)
