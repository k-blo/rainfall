# rainfall

A rainfall animation for CLI / unix terminals written in python.

![](rainfall.gif?raw=true)

The rain changes intensity over time.


## Installation


### Debian

Download [rainfall.deb](/alpin111/rainfall/releases/download/v0.3/rainfall.deb) and run:
`sudo dpkg -i rainfall.deb`

uninstall with `sudo apt remove rainfall`


### Fedora

Download [rainfall.rpm](alpin111/rainfall/releases/download/v0.3/rainfall.rpm) and run:
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
`rainfall i=10`

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

- Jonatha Gabriel[j0ng4b](https://github.com/j0ng4b)
- reddit [r/unixporn](https://old.reddit.com/r/unixporn/comments/v0vadk/oc_rain_animation_for_cli_that_changes_intensity/)

