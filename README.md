# scfetch
minimal fetch program written in python for linux, mac and windows.
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
## args
- `--color`: specify the theme color. available colors: red, green, yellow, blue, magenta, cyan, white  
example:
```bash
scfetch --color red
```
## config
define custom theme colors in ~/.config/scfetch.json (~/scfetch.json for windows)
available colors: red, green, yellow, blue, magenta, cyan, white
```json
{"color": "cyan"}
```
## public todo
- [x] add parameters for colors
- [ ] add parameters for ascii art
- [ ] update detection (get via pip)
- [x] distro ascii art (low priority)
