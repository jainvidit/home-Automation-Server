import random
import string

from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):

        form_excluded_columns = ['password']

        def on_model_change(self, form, model, is_created=False):
            password = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
            print 'on model change'
            print password
            #TODO: send password via mail to user
            model.set_password(password)