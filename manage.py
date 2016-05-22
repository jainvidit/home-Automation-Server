from home_automation import manager
from home_automation import current_app as app

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    manager.run()
