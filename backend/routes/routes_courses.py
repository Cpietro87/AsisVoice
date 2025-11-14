from flask import Blueprint, request, jsonify

courses = Blueprint('courses', __name__)

@courses.route('/courses', methods=['GET'])

def get_courses():
    courses = [
        {"id": 1, "name": "Introduction to Python"},
        {"id": 2, "name": "Advanced Flask Development"},
        {"id": 3, "name": "Data Science with Python"}
    ]
    return jsonify(courses)