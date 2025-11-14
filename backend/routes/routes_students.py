from flask import Blueprint, request, jsonify
from models.students import Student


students = Blueprint('students', __name__)

@students.route('/students', methods=['GET'])
def get_students():
    return jsonify({'message': 'List of students'}), 200