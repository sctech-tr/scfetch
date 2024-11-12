import platform
import re

def get_os_info():
    system = platform.system()
    
    if system == "Linux":
        try:
            with open("/etc/os-release") as f:
                os_info = {}
                for line in f:
                    # Skip empty lines and comments
                    if not line.strip() or line.startswith("#"):
                        continue
                    
                    # Match key-value considering quotes
                    match = re.match(r'([^=]+)=(?:"([^"]*)|([^"\n]*))', line.strip())
                    if match:
                        key = match.group(1)
                        # Use quoted value if present, otherwise use unquoted value
                        value = match.group(2) if match.group(2) is not None else match.group(3)
                        os_info[key] = value
            
            # Get name and version with fallbacks
            name = os_info.get("PRETTY_NAME", os_info.get("NAME", "Linux"))
            # If PRETTY_NAME was used, return it directly as it includes version
            if "PRETTY_NAME" in os_info:
                return name
                
            version = os_info.get("VERSION", os_info.get("VERSION_ID", ""))
            return f"{name} {version}".strip()
                
        except Exception as e:
            return "CONTACT DEV WITH ERRCODE: os_info_threw_exception"
            
    elif system == "Windows":
        return platform.system() + " " + platform.release()
        
    elif system == "Darwin":
        version = platform.mac_ver()[0]
        return f"macOS {version}"
    else:
        return "CONTACT DEV WITH ERRCODE: os_info_threw_exception_unsupported_platform"