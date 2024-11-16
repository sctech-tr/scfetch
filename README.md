# scfetch
the ultimate successor to neofetch and betterfetch
## installation
for latest release:
```bash
pip install scfetch
```
for latest commit:
```bash
pip install git+https://github.com/sctech-tr/scfetch.git
```
## usage
```bash
scfetch
```
## what does it show
- os
- host
- kernel
- uptime
- arch
- shell
- resolution
- cpu
- gpu
- ram
- de/wm
- battery
- disk usage
- python version
- locale
- private ip
- public ip
- mac address
- colored bar to identify terminal colors
## config
define custom theme colors in ~/.config/scfetch.json  
available colors: red, green, yellow, blue, magenta, cyan, white
```json
{"color": "cyan"}
```
## public todo
- [ ] add parameters for colors
- [ ] hide/show for each field via config file
- [ ] update detection
- [ ] website
- [ ] distro ascii art (low priority)
## example output
### on linux:
```
sctech@multipurpose-device
==================================================
OS:               Fedora Linux 41 (KDE Plasma)
Host:             GE60 0NC\0ND
Kernel:           6.11.5-300.fc41.x86_64
Uptime:           0d 0h 26m
Arch:             x86_64
Shell:            bash
Resolution:       1920x1080
CPU:              Intel(R) Core(TM) i7-3630QM CPU @ 2.40GHz
GPU:              NVIDIA Corporation GK107M [GeForce GTX 660M] (rev a1)
RAM:              7.64 GB
DE/WM:            KDE
Battery:          You don't have a battery. Are you a desktop user?
Disk Usage:       Used: 140GB / Free: 79GB
Python Version:   3.13.0
Locale:           tr_TR
Local IP:         192.168.1.114
Public IP:        REDACTED FOR PRIVACY
MAC Address:      REDACTED FOR PRIVACY
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
```
### on windows:
```
sctech@windows-pc
==================================================
OS:               Windows 10
Host:             Nitro AN515-54
Kernel:           10
Uptime:           0d 0h 26m
Arch:             AMD64
Shell:            cmd.exe
Resolution:       1920x1080
CPU:              Intel64 Family 6 Model 158 Stepping 10, GenuineIntel
GPU:              Intel(R) UHD Graphics 630
RAM:              15.85 GB
DE/WM:            Windows Explorer
Battery:          96%, Charging
Disk Usage:       Used: 172 GB / Free: 64 GB
Python Version:   3.13.0
Locale:           en_US
Local IP:         192.168.56.1
Public IP:        REDACTED FOR PRIVACY
MAC Address:      REDACTED FOR PRIVACY
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
```
