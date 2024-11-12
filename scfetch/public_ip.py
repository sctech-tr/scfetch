import requests
import platform

def get_public_ip():
    try:
        if platform.system() in ["Linux", "Darwin", "Windows"]:
            response = requests.get("https://api64.ipify.org?format=json")
            if response.status_code == 200:
                return response.json()["ip"]
            return "Ipify down, wait for it to come back up"
        else:
            return "CONTACT DEV WITH ERRCODE: public_ip_info_threw_exception_unsupported_platform"
    except Exception:
        return "CONTACT DEV WITH ERRCODE: public_ip_info_threw_exception"