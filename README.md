# rainfall

A rainfall animation for CLI / unix terminals written in python.

![](rainfall.gif?raw=true)

The rain changes intensity over time.


## Installation


### Debian

Download [rainfall.deb](rainfall.deb?raw=true) and run:
`sudo dpkg -i rainfall.deb`

uninstall with `sudo apt remove rainfall`


### Fedora

Download [rainfall.rpm](rainfall.rpm?raw=true) and run:
`sudo rpm -i rainfall.rpm`

uninstall with `sudo dnf remove rainfall`


### Arch

Link to [AUR package](https://aur.archlinux.org/packages/rainfall)


### without installation

Download [rainfall.py](source/rainfall.py?raw=true) and run
`python3 rainfall.py` or just `rainfall.py`


## How to use

to start, run:
`rainfall`

to stop, `CTRL+C`


make light or heavy rain by adding a parameter between 1-10:
`rainfall 10`

monochrome option:
`rainfall -m`

