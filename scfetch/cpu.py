import platform
import subprocess

def get_cpu_info():
    system = platform.system()
    if system == "Windows":
        return platform.uname().processor
    elif system == "Linux":
        # Linux: Reading from /proc/cpuinfo
        with open("/proc/cpuinfo", "r") as f:
            for line in f:
                if "model name" in line:
                    return line.split(":")[1].strip()
    elif system == "Darwin":  # MacOS
        return subprocess.check_output(["sysctl", "-n", "machdep.cpu.brand_string"]).decode().strip()
    else:
        return "CONTACT DEV WITH ERRCODE: cpu_info_threw_exception_unsupported_platform"