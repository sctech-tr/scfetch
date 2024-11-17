# --- BEGIN RANDOM IMPORTS NO ONE READS ---

# these are the imports for the color and effects
from colorist import Color, Effect

# these are the imports for the config
import json
import os
import platform

# these are the imports for the fetch
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

def define_ascii():
    lines = []
    if platform.system() == "Windows":
        lines = [
            f"{Color.BLUE}                    ....,,:;+ccllll  {Color.OFF}",
            f"{Color.BLUE}     ...,,+:;  clllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE},cclllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}                                     {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}llllllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}`'ccllllllllll  lllllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}      `' ''*::  :ccllllllllllllllll  {Color.OFF}",
            f"{Color.BLUE}                      ````'' *::cll  {Color.OFF}"
        ]
    elif platform.system() == "Linux":
        lines = [
            f"{Color.BLACK}            a8888b.         {Color.OFF}",
            f"{Color.BLACK}          d888888b.         {Color.OFF}",
            f"{Color.BLACK}          8P'YP'Y88         {Color.OFF}",
            f"{Color.BLACK}          8|{Color.OFF}{Color.WHITE}O{Color.OFF}{Color.BLACK}||{Color.OFF}{Color.WHITE}O{Color.OFF}{Color.BLACK}|88         {Color.OFF}",
            f"{Color.BLACK}          8{Color.OFF}{Color.YELLOW}'    .{Color.OFF}{Color.BLACK}88         {Color.OFF}",
            f"{Color.BLACK}          8{Color.OFF}{Color.YELLOW}`._.'{Color.OFF}{Color.BLACK} Y8.        {Color.OFF}",
            f"{Color.BLACK}        d/      `8b.        {Color.OFF}",
            f"{Color.BLACK}      .dP   .     Y8b.      {Color.OFF}",
            f"{Color.BLACK}      d8:'   '   `::88b.    {Color.OFF}",
            f"{Color.BLACK}     d8'           `Y88b    {Color.OFF}",
            f"{Color.BLACK}    :8P     '       :888    {Color.OFF}",
            f"{Color.BLACK}     8a.    :      _a88P    {Color.OFF}",
            f"{Color.BLACK}   {Color.OFF}{Color.YELLOW}._/'Y{Color.OFF}{Color.BLACK}aa_     :.{Color.OFF}{Color.YELLOW} -----    {Color.OFF}",
            rf"{Color.BLACK}   {Color.OFF}{Color.YELLOW}\    YP'      `{Color.OFF}{Color.YELLOW}|     `.  {Color.OFF}",
            rf"{Color.BLACK}   {Color.OFF}{Color.YELLOW}/     \.{Color.OFF}{Color.BLACK}_____.d{Color.OFF}{Color.YELLOW}|    {Color.OFF}{Color.YELLOW} .'  {Color.OFF}",
            f"{Color.BLACK}   {Color.OFF}{Color.YELLOW}`--..__){Color.OFF}{Color.BLACK}888888P{Color.OFF}{Color.YELLOW}`._.'     {Color.OFF}",
            f"{Color.BLACK}                            {Color.OFF}",
            f"{Color.BLACK}                            {Color.OFF}"
        ]
    elif platform.system() == "Darwin":
        lines = [
            f"{Color.RED}              ___           {Color.OFF}",
            f"{Color.RED}           ⢀⣴⣿⣿⡿           {Color.OFF}",
            f"{Color.RED}          ⢀⣾⣿⣿⠟⠁           {Color.OFF}",
            f"{Color.RED}  ⢀⣠⣤⣤⣤⣀⣀⠈⠋⠉⣁⣠⣤⣤⣤⣀⡀      {Color.OFF}",
            f"{Color.RED} ⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦.   {Color.OFF}",
            f"{Color.RED}⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀  {Color.OFF}",
            f"{Color.RED}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀  {Color.OFF}",
            f"{Color.RED}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀  {Color.OFF}",
            f"{Color.RED}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀  {Color.OFF}",
            f"{Color.RED}⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀  {Color.OFF}",
            f"{Color.RED} ⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁  {Color.OFF}",
            f"{Color.RED}  ⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀  {Color.OFF}",
            f"{Color.RED}    ⠈⠙⢿⣿⣿⣿⠿⠟⠛⠻⠿⣿⣿⣿⡿⠋⠀⠀⠀ {Color.OFF}",
            f"{Color.RED}                           {Color.OFF}",
            f"{Color.RED}                           {Color.OFF}",
            f"{Color.RED}                           {Color.OFF}",
            f"{Color.RED}                           {Color.OFF}",
            f"{Color.RED}                           {Color.OFF}"
        ]
    return lines

# real fetch
def main():

    # ascii art
    lines = define_ascii()

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

    # i had to test this a million times to get the space count working
    print(f"                            {Effect.BOLD}{color}{get_username()}{Color.OFF}{Effect.OFF}@{Effect.BOLD}{color}{get_machine_name()}{Color.OFF}{Effect.OFF}")
    print(f"                            {color}{'=' * 50}{Color.OFF}")
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