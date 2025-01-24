# rainfall

A rainfall animation for CLI / unix terminals written in python.

![](rainfall.gif?raw=true)

The rain changes intensity over time.


## Installation


### Debian

Download [rainfall.deb](https://github.com/alpin111/rainfall/releases/download/v1.0.1/rainfall_1.0.1_amd64.deb) and run:
`sudo dpkg -i rainfall.deb`

uninstall with `sudo apt remove rainfall`


### Fedora

Download [rainfall.rpm](https://github.com/alpin111/rainfall/releases/download/v1.0.1/rainfall-1.0.1-1.el7.x86_64.rpm) and run:
`sudo rpm -i rainfall.rpm`

uninstall with `sudo dnf remove rainfall`


### Arch

Link to [AUR package](https://aur.archlinux.org/packages/rainfall)

`yay -S rainfall`


### without installation

Download [rainfall.py](source/rainfall.py?raw=true) and run
`python3 rainfall.py` or just `rainfall.py`


## How to use

to start, run:
`rainfall`

to stop, `CTRL+C`

make light or heavy rain by adding a parameter between 1-10:
`rainfall -i=10`

change the speed of frame re-rendering in seconds:
`rainfall -t=0.12`
the default is `0.08`

monochrome option:
`rainfall -m`

colors:
`rainfall green cyan red`

### valid colors:

black
red
green
yellow
blue
magenta
cyan
white

#### bright variants:

b_black
b_red
b_green
b_yellow
b_blue
b_magenta
b_cyan
b_white


## unofficial contributors

- Jonatha Gabriel [j0ng4b](https://github.com/j0ng4b)

