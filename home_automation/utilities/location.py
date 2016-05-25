from home_automation.models.device import Device


def get_device_ids_for_location(location_id):
    devices = Device.query.filter_by(location_id=location_id).all()
    device_ids = []
    for device in devices:
        device_ids.append(device.id)
    return device_ids
