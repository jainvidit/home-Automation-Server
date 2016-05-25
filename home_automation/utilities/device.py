from home_automation.models.device import Device


def get_status_for_device(device_id):
    device = Device.query.filter_by(id=device_id).first()
    status = device.status
    return status
