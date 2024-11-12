import platform
import subprocess

def get_gpu_info():
    system = platform.system()
    if system == "Windows":
        return subprocess.check_output("wmic path win32_VideoController get name", shell=True).decode().split('\n')[1].strip()
    elif system == "Linux":
        return subprocess.check_output("lspci | grep ' VGA '", shell=True).decode().split(':')[-1].strip()
    elif system == "Darwin":  # MacOS
        return subprocess.check_output("system_profiler SPDisplaysDataType | grep 'Chipset Model'", shell=True).decode().split(": ")[-1].strip()
    else:
        return "CONTACT DEV WITH ERRCODE: gpu_info_threw_exception_unsupported_platform"
