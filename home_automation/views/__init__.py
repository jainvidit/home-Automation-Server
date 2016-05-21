from flask import Blueprint
from flask import request
from flask import jsonify
from home_automation.models.user import User
from home_automation.models.location import Location


app = Blueprint('', __name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def valid_login(email, password):
    #TODO: use check_password from user class to chack for password(after bug fix)
    if User.query.filter_by(email=email,password=password).first() != None:
        return True
    return False


def get_user_details(email_id):
    user = User.query.filter_by(email=email_id).first()
    user_detail = {'user_id':user.id,'user_name':user.name,'user_email':email_id}
    locations = Location.query.filter_by(user_id=user.id).all()
    location_ids = []
    print type(locations[0])
    for location in locations:
        location_ids.append(location.id)
    print "loop done"
    user_detail['locations']=location_ids
    return user_detail

@app.route('/login', methods=['POST'])
def login():
    login_success = False
    user_details = None
    print "Login Request : ", request
    if 'email' in request.form:
        email = request.form['email']
        print email
        if 'password' in request.form:
            password = request.form['password']
            print password
            if valid_login(email, password):
                print "get details"
                user_details = get_user_details(email)
                print "got details"
                login_success = True
    response = {'success': login_success, 'details': user_details}
    return jsonify(response)
