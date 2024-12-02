import json
import os
import platform

def get_config_path():
    config_paths = {
        "Windows": os.path.expanduser("~/"),
        "Linux": os.path.expanduser("~/.config/"),
        "Darwin": os.path.expanduser("~/.config/")
    }
    
    # get the base config path for the current OS
    base_path = config_paths.get(platform.system())
    
    if not base_path:
        raise OSError(f"CONTACT DEV WITH ERRCODE: get_config_path_threw_exception_unsupported_os")
    
    # create the directory if it doesn't exist
    os.makedirs(base_path, exist_ok=True)
    return os.path.join(base_path, "scfetch.json")

def read_config():
    default_config = {"color": "cyan"}
    
    try:
        config_path = get_config_path()
        
        # if file doesn't exist, create it with default content
        if not os.path.exists(config_path):
            write_config(default_config)
            return default_config
        
        # read and parse the config file
        with open(config_path, "r") as f:
            config = json.load(f)
        
        # validate config
        if not isinstance(config, dict):
            return default_config
        
        # ensure color is set, use default if not
        config.setdefault("color", "cyan")
        
        return config
    
    except json.JSONDecodeError:
        print(f"CONTACT DEV WITH ERRCODE: read_config_threw_exception_json_decode_error")
        return default_config
    except PermissionError:
        print(f"CONTACT DEV WITH ERRCODE: read_config_threw_exception_permission_error")
        return default_config
    except OSError:
        print(f"CONTACT DEV WITH ERRCODE: read_config_threw_exception_os_error")
        return default_config
    
def write_config(config):
    try:
        config_path = get_config_path()
        
        # validate config before writing
        if not isinstance(config, dict):
            config = {"color": "cyan"}
        
        # ensure color is valid
        valid_colors = ["red", "yellow", "green", "cyan", "blue", "magenta", "white"]
        if config.get("color") not in valid_colors:
            config["color"] = "cyan"
        
        # write config with proper permissions
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    
    except (PermissionError, OSError):
        print(f"CONTACT DEV WITH ERRCODE: write_config_threw_exception_permission_error")