from home_automation.models.user import User
from home_automation.models.location import Location


def validate_login(email, password):
    user = User.query.filter_by(email=email).first()
    if user != None:
        return user.check_password(password)
    return False


def get_locations_for_user(user_id):
    locations = Location.query.filter_by(user_id=user_id).all()
    location_list = []
    for location in locations:
        location_list.append({'id':location.id, 'name':location.name})
    return location_list


def get_user_detail_from_email(email_id):
    user = User.query.filter_by(email=email_id).first()
    user_detail = {'user_id': user.id,
                   'user_name': user.name,
                   'user_email': email_id}
    return user_detail
