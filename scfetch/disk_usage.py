import shutil

def get_disk_usage():
    try:
        total, used, free = shutil.disk_usage("/")
        return f"Used: {used // (2**30)}GB / Free: {free // (2**30)}GB"
    except Exception:
        return "CONTACT DEV WITH ERRCODE: disk_usage_info_threw_exception"