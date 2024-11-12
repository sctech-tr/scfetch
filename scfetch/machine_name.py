import platform

def get_machine_name():
    return platform.uname().node