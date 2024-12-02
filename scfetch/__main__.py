# --- BEGIN RANDOM IMPORTS NO ONE READS ---

# these are the imports for the arguments
import argparse

# these are the imports for the color and effects
from colorist import Color, Effect

# these are the imports for the ascii art
from scfetch.ascii import define_ascii

# these are the imports for the config
from scfetch.config import read_config

# these are the imports for the fetch
import platform
from scfetch.os_info import get_os_info
from scfetch.python_version import get_python_version
from scfetch.cpu import get_cpu_info
from scfetch.user import get_username
from scfetch.machine_name import get_machine_name
from scfetch.arch import get_arch
from scfetch.private_ip import get_private_ip
from scfetch.public_ip import get_public_ip
from scfetch.kernel_ver import get_kernel_ver
from scfetch.mac import get_mac_address
from scfetch.ram import get_ram
from scfetch.pc import get_pc_model
from scfetch.gpu import get_gpu_info
from scfetch.uptime import get_uptime
from scfetch.shell import get_shell
from scfetch.screen_resolution import get_screen_resolution
from scfetch.disk_usage import get_disk_usage
from scfetch.battery import get_battery_status
from scfetch.locale_info import get_locale
from scfetch.de_wm import get_wm

# --- END RANDOM IMPORTS NO ONE READS ---

# real fetch
def main():
    # parse the arguments
    parser = argparse.ArgumentParser(description="minimal fetch program")
    parser.add_argument("--color", type=str, help="specify the theme color")
    args = parser.parse_args()

    # define the ascii art
    lines = define_ascii()
    # read the config
    config = read_config()

    # get the color from the config or argument
    if args.color:
        color_raw = args.color
    else: # if no argument, use the config
        color_raw = config.get("color", "cyan")
    
    # map the color to the colorist color
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

    # i had to test this a million times to get the space count working. still broken on macOS :(
    # DONT CHANGE THE SPACES!!!!!!!!! IT WILL BREAK AND PYTHON WILL BLAME ME FOR MAKING AWFUL CODE!!!!!!!
    if platform.system() == "Linux":
        print(f"                            {Effect.BOLD}{color}{get_username()}{Color.OFF}{Effect.OFF}@{Effect.BOLD}{color}{get_machine_name()}{Color.OFF}{Effect.OFF}")
        print(f"                            {color}{'=' * 50}{Color.OFF}")
    elif platform.system() == "Windows":
        print(f"                                     {Effect.BOLD}{color}{get_username()}{Color.OFF}{Effect.OFF}@{Effect.BOLD}{color}{get_machine_name()}{Color.OFF}{Effect.OFF}")
        print(f"                                     {color}{'=' * 50}{Color.OFF}")
    elif platform.system() == "Darwin":
        print(f"                          {Effect.BOLD}{color}{get_username()}{Color.OFF}{Effect.OFF}@{Effect.BOLD}{color}{get_machine_name()}{Color.OFF}{Effect.OFF}")
        print(f"                          {color}{'=' * 50}{Color.OFF}")
    print(f"{lines[0]}{Effect.BOLD}{color}OS{Color.OFF}{Effect.OFF}:               {get_os_info()}")
    print(f"{lines[1]}{Effect.BOLD}{color}Host{Color.OFF}{Effect.OFF}:             {get_pc_model()}")
    print(f"{lines[2]}{Effect.BOLD}{color}Kernel{Color.OFF}{Effect.OFF}:           {get_kernel_ver()}")
    print(f"{lines[3]}{Effect.BOLD}{color}Uptime{Color.OFF}{Effect.OFF}:           {get_uptime()}")
    print(f"{lines[4]}{Effect.BOLD}{color}Arch{Color.OFF}{Effect.OFF}:             {get_arch()}")
    print(f"{lines[5]}{Effect.BOLD}{color}Shell{Color.OFF}{Effect.OFF}:            {get_shell()}")
    print(f"{lines[6]}{Effect.BOLD}{color}Resolution{Color.OFF}{Effect.OFF}:       {get_screen_resolution()}")
    print(f"{lines[7]}{Effect.BOLD}{color}CPU{Color.OFF}{Effect.OFF}:              {get_cpu_info()}")
    print(f"{lines[8]}{Effect.BOLD}{color}GPU{Color.OFF}{Effect.OFF}:              {get_gpu_info()}")
    print(f"{lines[9]}{Effect.BOLD}{color}RAM{Color.OFF}{Effect.OFF}:              {get_ram()}")
    print(f"{lines[10]}{Effect.BOLD}{color}DE/WM{Color.OFF}{Effect.OFF}:            {get_wm()}")
    print(f"{lines[11]}{Effect.BOLD}{color}Battery{Color.OFF}{Effect.OFF}:          {get_battery_status()}")
    print(f"{lines[12]}{Effect.BOLD}{color}Disk Usage{Color.OFF}{Effect.OFF}:       {get_disk_usage()}")
    print(f"{lines[13]}{Effect.BOLD}{color}Python Version{Color.OFF}{Effect.OFF}:   {get_python_version()}")
    print(f"{lines[14]}{Effect.BOLD}{color}Locale{Color.OFF}{Effect.OFF}:           {get_locale()}")
    print(f"{lines[15]}{Effect.BOLD}{color}Local IP{Color.OFF}{Effect.OFF}:         {get_private_ip()}")
    print(f"{lines[16]}{Effect.BOLD}{color}Public IP{Color.OFF}{Effect.OFF}:        {get_public_ip()}")
    print(f"{lines[17]}{Effect.BOLD}{color}MAC Address{Color.OFF}{Effect.OFF}:      {get_mac_address()}")
    print(f"                            {Color.RED}■■■■{Color.OFF}{Color.YELLOW}■■■■{Color.OFF}{Color.GREEN}■■■■{Color.OFF}{Color.CYAN}■■■■{Color.OFF}{Color.BLUE}■■■■{Color.OFF}{Color.MAGENTA}■■■■{Color.OFF}{Color.BLUE}■■■■{Color.OFF}{Color.CYAN}■■■■{Color.OFF}{Color.GREEN}■■■■{Color.OFF}{Color.YELLOW}■■■■{Color.OFF}{Color.RED}■■■■{Color.OFF}")
    print(f"                            {Color.RED}■■■■{Color.OFF}{Color.YELLOW}■■■■{Color.OFF}{Color.GREEN}■■■■{Color.OFF}{Color.CYAN}■■■■{Color.OFF}{Color.BLUE}■■■■{Color.OFF}{Color.MAGENTA}■■■■{Color.OFF}{Color.BLUE}■■■■{Color.OFF}{Color.CYAN}■■■■{Color.OFF}{Color.GREEN}■■■■{Color.OFF}{Color.YELLOW}■■■■{Color.OFF}{Color.RED}■■■■{Color.OFF}")

if __name__ == "__main__":
    main()