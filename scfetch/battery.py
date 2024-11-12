import platform
import psutil

def get_battery_status():
    try:
        if platform.system() in ["Linux", "Darwin", "Windows"]:
            battery = psutil.sensors_battery()
            if battery is None:
                return "You don't have a battery. Are you a desktop user?" # are you?
            status = "Charging" if battery.power_plugged else "Discharging"
            return f"{battery.percent}%, {status}"
        else:
            return "CONTACT DEV WITH ERRCODE: battery_info_threw_exception_unsupported_platform"
    except Exception:
        return "CONTACT DEV WITH ERRCODE: battery_info_threw_exception"