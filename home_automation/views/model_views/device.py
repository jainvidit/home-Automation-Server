from flask_admin.contrib.sqla import ModelView

class DeviceView(ModelView):
  column_display_pk = True
