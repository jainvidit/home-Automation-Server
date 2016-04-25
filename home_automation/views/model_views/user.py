from flask_admin.contrib.sqla import ModelView

class UserView(ModelView):

        form_excluded_columns = ['password']

        def on_model_change(self, form, model, is_created=False):
            #TODO: generate random password and mail to user
            model.password = "hello"