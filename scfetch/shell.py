import os
import platform

def get_shell():
    try:
        if platform.system() in ["Linux", "Darwin"]:
            return os.path.basename(os.environ.get("SHELL", "Unknown"))
        elif platform.system() == "Windows":
            return os.path.basename(os.environ.get("COMSPEC", "cmd.exe"))
        else:
            return "CONTACT DEV WITH ERRCODE: shell_info_threw_exception_unsupported_platform"
    except Exception:
        return "CONTACT DEV WITH ERRCODE: shell_info_threw_exception"