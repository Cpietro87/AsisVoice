from flask import Blueprint, request, jsonify

assistance = Blueprint('assistance', __name__, url_prefix='/assistance')

@assistance.route('/', methods=['GET'])
def get_assistances():
    return "List of assistances"