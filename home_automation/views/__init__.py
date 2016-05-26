from flask import Blueprint
from flask import jsonify
from flask import request

from home_automation.utilities.device import *
from home_automation.utilities.location import get_device_ids_for_location
from home_automation.utilities.user import get_location_ids_for_user
from home_automation.views.login import login

app = Blueprint('', __name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['POST'])
def login_view():
    return login(request)


@app.route('/user/<user_id>/locations', methods=['GET'])
def get_location_list_for_user_id(user_id):
    locations = get_location_ids_for_user(user_id)
    response = {"location_list": locations}
    json_response = jsonify(response)
    return json_response


@app.route('/location/<location_id>/devices', methods=['GET'])
def get_device_list_for_user_id():
    devices = get_device_ids_for_location(location_id)
    response = {"device_list": devices}
    json_response = jsonify(response)
    return json_response


@app.route('/device/<int:device_id>/get_status', methods=['GET'])
def get_status_for_device_id(device_id):
    status = get_status_for_device(device_id)
    response = '0'
    if status:
        response = '1'
    return response

@app.route('/device/<int:device_id>/set_status/<int:status>', methods=['GET'])
def set_status_for_device_id(device_id, status):
    res = set_status_for_device(device_id, status)
    if res:
        return 'Success'
    else:
        return 'Error'

