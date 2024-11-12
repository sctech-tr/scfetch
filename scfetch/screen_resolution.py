import platform
import subprocess

def get_screen_resolution():
    try:
        if platform.system() == "Linux":
            output = subprocess.check_output("xrandr | grep '*' | awk '{print $1}'", shell=True)
            return output.decode().strip().splitlines()[0]
        elif platform.system() == "Windows":
            from screeninfo import get_monitors
            return f"{get_monitors()[0].width}x{get_monitors()[0].height}"
        elif platform.system() == "Darwin":
            output = subprocess.check_output("system_profiler SPDisplaysDataType | grep Resolution", shell=True)
            return output.decode().strip().split(": ")[1]
        else:
            return "CONTACT DEV WITH ERRCODE: screen_resolution_info_threw_exception_unsupported_platform"
    except Exception:
        return "CONTACT DEV WITH ERRCODE: screen_resolution_info_threw_exception"