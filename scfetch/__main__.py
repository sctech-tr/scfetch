# --- BEGIN RANDOM IMPORTS NO ONE READS ---

# these are the imports for the color and effects
from colorist import Color, Effect

# these are the imports for the config
import json
import os
import platform

# these are the imports for the fetch
from .os_info import get_os_info
from .python_version import get_python_version
from .cpu import get_cpu_info
from .user import get_username
from .machine_name import get_machine_name
from .arch import get_arch
from .private_ip import get_private_ip
from .public_ip import get_public_ip
from .kernel_ver import get_kernel_ver
from .mac import get_mac_address
from .ram import get_ram
from .pc import get_pc_model
from .gpu import get_gpu_info
from .uptime import get_uptime
from .shell import get_shell
from .screen_resolution import get_screen_resolution
from .disk_usage import get_disk_usage
from .battery import get_battery_status
from .locale_info import get_locale
from .de_wm import get_wm

# --- END RANDOM IMPORTS NO ONE READS ---

# real fetch
def main():
    color_raw = "cyan"
    config_paths = {
        "Windows": "%USERPROFILE%/scfetch.json",
        "Linux": "~/.config/scfetch.json",
        "Darwin": "~/.config/scfetch.json"
    }

    config_path = os.path.expanduser(config_paths.get(platform.system(), ""))
    if not config_path:
        print("CONTACT DEV WITH ERRCODE: config_threw_exception_unsupported_os")
        exit(1)

    if not os.path.exists(config_path):
        with open(config_path, "w") as f:
            json.dump({"color": "cyan"}, f)
    else:
        with open(config_path, "r") as f:
            color_raw = json.load(f).get("color", "cyan")

    color_map = {
        "red": Color.RED,
        "yellow": Color.YELLOW,
        "green": Color.GREEN,
        "cyan": Color.CYAN,
        "blue": Color.BLUE,
        "magenta": Color.MAGENTA,
        "white": Color.WHITE
    }
    color = color_map.get(color_raw, Color.CYAN)
    print(f"{Effect.BOLD}{color}{get_username()}{Color.OFF}{Effect.OFF}@{Effect.BOLD}{color}{get_machine_name()}{Color.OFF}{Effect.OFF}") # what
    print(f"{color}{'=' * 50}{Color.OFF}")
    # i had to test this a million times to get the space count working
    print(f"{Effect.BOLD}{color}OS{Color.OFF}{Effect.OFF}:               {get_os_info()}")
    print(f"{Effect.BOLD}{color}Host{Color.OFF}{Effect.OFF}:             {get_pc_model()}")
    print(f"{Effect.BOLD}{color}Kernel{Color.OFF}{Effect.OFF}:           {get_kernel_ver()}")
    print(f"{Effect.BOLD}{color}Uptime{Color.OFF}{Effect.OFF}:           {get_uptime()}")
    print(f"{Effect.BOLD}{color}Arch{Color.OFF}{Effect.OFF}:             {get_arch()}")
    print(f"{Effect.BOLD}{color}Shell{Color.OFF}{Effect.OFF}:            {get_shell()}")
    print(f"{Effect.BOLD}{color}Resolution{Color.OFF}{Effect.OFF}:       {get_screen_resolution()}")
    print(f"{Effect.BOLD}{color}CPU{Color.OFF}{Effect.OFF}:              {get_cpu_info()}")
    print(f"{Effect.BOLD}{color}GPU{Color.OFF}{Effect.OFF}:              {get_gpu_info()}")
    print(f"{Effect.BOLD}{color}RAM{Color.OFF}{Effect.OFF}:              {get_ram()}")
    print(f"{Effect.BOLD}{color}DE/WM{Color.OFF}{Effect.OFF}:            {get_wm()}")
    print(f"{Effect.BOLD}{color}Battery{Color.OFF}{Effect.OFF}:          {get_battery_status()}")
    print(f"{Effect.BOLD}{color}Disk Usage{Color.OFF}{Effect.OFF}:       {get_disk_usage()}")
    print(f"{Effect.BOLD}{color}Python Version{Color.OFF}{Effect.OFF}:   {get_python_version()}")
    print(f"{Effect.BOLD}{color}Locale{Color.OFF}{Effect.OFF}:           {get_locale()}")
    print(f"{Effect.BOLD}{color}Local IP{Color.OFF}{Effect.OFF}:         {get_private_ip()}")
    print(f"{Effect.BOLD}{color}Public IP{Color.OFF}{Effect.OFF}:        {get_public_ip()}")
    print(f"{Effect.BOLD}{color}MAC Address{Color.OFF}{Effect.OFF}:      {get_mac_address()}")
    print(f"{Color.RED}■■■■{Color.OFF}{Color.YELLOW}■■■■{Color.OFF}{Color.GREEN}■■■■{Color.OFF}{Color.CYAN}■■■■{Color.OFF}{Color.BLUE}■■■■{Color.OFF}{Color.MAGENTA}■■■■{Color.OFF}{Color.BLUE}■■■■{Color.OFF}{Color.CYAN}■■■■{Color.OFF}{Color.GREEN}■■■■{Color.OFF}{Color.YELLOW}■■■■{Color.OFF}{Color.RED}■■■■{Color.OFF}")
    print(f"{Color.RED}■■■■{Color.OFF}{Color.YELLOW}■■■■{Color.OFF}{Color.GREEN}■■■■{Color.OFF}{Color.CYAN}■■■■{Color.OFF}{Color.BLUE}■■■■{Color.OFF}{Color.MAGENTA}■■■■{Color.OFF}{Color.BLUE}■■■■{Color.OFF}{Color.CYAN}■■■■{Color.OFF}{Color.GREEN}■■■■{Color.OFF}{Color.YELLOW}■■■■{Color.OFF}{Color.RED}■■■■{Color.OFF}")

if __name__ == "__main__":
    main()