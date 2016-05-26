from home_automation.models.device import Device
from home_automation.models import db


def get_status_for_device(device_id):
    device = Device.query.filter_by(id=device_id).first()
    status = device.status
    return status


def set_status_for_device(device_id, status):
    device = Device.query.get(device_id)
    device.status = bool(status)
    try:
        db.session.commit()
        return True
    except Exception, e:
        print(e)
        return False
