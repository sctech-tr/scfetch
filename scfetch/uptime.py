import time
import platform
import subprocess

def get_uptime():
    try:
        if platform.system() == "Linux":
            with open("/proc/uptime", "r") as f:
                uptime_seconds = float(f.readline().split()[0])
                days = int(uptime_seconds // (24 * 3600))
                hours = int((uptime_seconds % (24 * 3600)) // 3600)
                minutes = int((uptime_seconds % 3600) // 60)
                return f"{days}d {hours}h {minutes}m"
        elif platform.system() == "Windows":
            import ctypes
            uptime_ms = ctypes.windll.kernel32.GetTickCount64()
            uptime_seconds = uptime_ms / 1000
            days = int(uptime_seconds // (24 * 3600))
            hours = int((uptime_seconds % (24 * 3600)) // 3600)
            minutes = int((uptime_seconds % 3600) // 60)
            return f"{days}d {hours}h {minutes}m"
        elif platform.system() == "Darwin":
            output = subprocess.check_output("sysctl -n kern.boottime", shell=True)
            boottime = float(output.split()[3].strip(","))
            uptime_seconds = time.time() - boottime
            days = int(uptime_seconds // (24 * 3600))
            hours = int((uptime_seconds % (24 * 3600)) // 3600)
            minutes = int((uptime_seconds % 3600) // 60)
            return f"{days}d {hours}h {minutes}m"
        else:
            return "CONTACT DEV WITH ERRCODE: uptime_info_threw_exception_unsupported_platform"
    except Exception:
        return "CONTACT DEV WITH ERRCODE: uptime_info_threw_exception"
