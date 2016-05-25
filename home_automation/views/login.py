from flask import jsonify
from home_automation.utilities.user import get_user_detail_from_email
from home_automation.utilities.user import validate_login


def login(request):
    login_success = False
    user_details = None
    print "Login Request : ", request
    if 'email' in request.form:
        email = request.form['email']
        print email
        if 'password' in request.form:
            password = request.form['password']
            print password
            if validate_login(email, password):
                print "get details"
                user_details = get_user_detail_from_email(email)
                print "got details"
                login_success = True
    response = {'success': login_success, 'details': user_details}
    json_response = jsonify(response)
    return json_response