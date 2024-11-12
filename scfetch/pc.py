import os
import platform

def get_pc_model():
    system = platform.system()

    try:
        if system == "Windows":
            return os.popen("wmic csproduct get name").read().splitlines()[1].strip()
        elif system == "Linux":
            with open("/sys/devices/virtual/dmi/id/product_name", "r") as f:
                return f.read().strip()
        elif system == "Darwin": # macos
            return os.popen("sysctl -n hw.model").read().strip()
    except Exception:
        return "CONTACT DEV WITH ERRCODE: pc_model_threw_exception_unsupported_platform"