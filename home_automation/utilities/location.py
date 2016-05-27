from home_automation.models.device import Device


def get_devices_for_location(location_id):
    devices = Device.query.filter_by(location_id=location_id).all()
    device_list = []
    for device in devices:
        device_list.append({'id':device.id,'name':device.name,'status':device.status})
    return device_list
