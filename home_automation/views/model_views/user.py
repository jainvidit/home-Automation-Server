import random
import string
from home_automation.utilities.mailing import send_mail
from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):

        form_excluded_columns = ['password']
        column_exclude_list = ['password']

        def on_model_change(self, form, model, is_created=False):
            password = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
            subject = 'Login Credentials for Morld Account'
            message_content = "Your Login credentials are as below \r\n\r\n"\
                              + "Username : " + model.email + "\r\nPassword : " + password +\
                              "\r\n\r\nRegards,\r\nMorld Team"
            send_mail(model.email,subject,message_content)
            model.set_password(password)