import platform

def get_os_info():
    return platform.system() + " " + platform.release()
