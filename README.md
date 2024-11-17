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
- os logo (win, mac, linux)
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
- [x] distro ascii art (low priority)
