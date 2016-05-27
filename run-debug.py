from home_automation import current_app
from home_automation.models import db

if __name__ == "__main__":
    with current_app.app_context():
        db.create_all()
    current_app.run(host='0.0.0.0', debug=True)