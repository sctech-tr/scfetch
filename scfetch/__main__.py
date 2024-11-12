# --- BEGIN RANDOM IMPORTS NO ONE READS ---

# these are the imports for the color and effects
from colorist import Color, Effect

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
    print(f"{Effect.BOLD}{Color.CYAN}{get_username()}{Color.OFF}{Effect.OFF}@{Effect.BOLD}{Color.CYAN}{get_machine_name()}{Color.OFF}{Effect.OFF}") # what
    print(f"{Color.CYAN}{'=' * 50}{Color.OFF}")
    # i had to test this a million times to get the space count working
    print(f"{Effect.BOLD}{Color.CYAN}OS{Color.OFF}{Effect.OFF}:               {get_os_info()}")
    print(f"{Effect.BOLD}{Color.CYAN}Host{Color.OFF}{Effect.OFF}:             {get_pc_model()}")
    print(f"{Effect.BOLD}{Color.CYAN}Kernel{Color.OFF}{Effect.OFF}:           {get_kernel_ver()}")
    print(f"{Effect.BOLD}{Color.CYAN}Uptime{Color.OFF}{Effect.OFF}:           {get_uptime()}")
    print(f"{Effect.BOLD}{Color.CYAN}Arch{Color.OFF}{Effect.OFF}:             {get_arch()}")
    print(f"{Effect.BOLD}{Color.CYAN}Shell{Color.OFF}{Effect.OFF}:            {get_shell()}")
    print(f"{Effect.BOLD}{Color.CYAN}Resolution{Color.OFF}{Effect.OFF}:       {get_screen_resolution()}")
    print(f"{Effect.BOLD}{Color.CYAN}CPU{Color.OFF}{Effect.OFF}:              {get_cpu_info()}")
    print(f"{Effect.BOLD}{Color.CYAN}GPU{Color.OFF}{Effect.OFF}:              {get_gpu_info()}")
    print(f"{Effect.BOLD}{Color.CYAN}RAM{Color.OFF}{Effect.OFF}:              {get_ram()}")
    print(f"{Effect.BOLD}{Color.CYAN}DE/WM{Color.OFF}{Effect.OFF}:            {get_wm()}")
    print(f"{Effect.BOLD}{Color.CYAN}Battery{Color.OFF}{Effect.OFF}:          {get_battery_status()}")
    print(f"{Effect.BOLD}{Color.CYAN}Disk Usage{Color.OFF}{Effect.OFF}:       {get_disk_usage()}")
    print(f"{Effect.BOLD}{Color.CYAN}Python Version{Color.OFF}{Effect.OFF}:   {get_python_version()}")
    print(f"{Effect.BOLD}{Color.CYAN}Locale{Color.OFF}{Effect.OFF}:           {get_locale()}")
    print(f"{Effect.BOLD}{Color.CYAN}Local IP{Color.OFF}{Effect.OFF}:         {get_private_ip()}")
    print(f"{Effect.BOLD}{Color.CYAN}Public IP{Color.OFF}{Effect.OFF}:        {get_public_ip()}")
    print(f"{Effect.BOLD}{Color.CYAN}MAC Address{Color.OFF}{Effect.OFF}:      {get_mac_address()}")
    print(f"{Color.RED}IIII{Color.OFF}{Color.YELLOW}IIII{Color.OFF}{Color.GREEN}IIII{Color.OFF}{Color.CYAN}IIII{Color.OFF}{Color.BLUE}IIII{Color.OFF}{Color.MAGENTA}IIII{Color.OFF}{Color.BLUE}IIII{Color.OFF}{Color.CYAN}IIII{Color.OFF}{Color.GREEN}IIII{Color.OFF}{Color.YELLOW}IIII{Color.OFF}{Color.RED}IIII{Color.OFF}")
    print(f"{Color.RED}IIII{Color.OFF}{Color.YELLOW}IIII{Color.OFF}{Color.GREEN}IIII{Color.OFF}{Color.CYAN}IIII{Color.OFF}{Color.BLUE}IIII{Color.OFF}{Color.MAGENTA}IIII{Color.OFF}{Color.BLUE}IIII{Color.OFF}{Color.CYAN}IIII{Color.OFF}{Color.GREEN}IIII{Color.OFF}{Color.YELLOW}IIII{Color.OFF}{Color.RED}IIII{Color.OFF}")
if __name__ == "__main__":
    main()
