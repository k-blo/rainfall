#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

import time
import random
import os
import sys


colors = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "reset": "\u001b[0m",

    "b_black": "\u001b[30;1m",
    "b_red": "\u001b[31;1m",
    "b_green": "\u001b[32;1m",
    "b_yellow": "\u001b[33;1m",
    "b_blue": "\u001b[34;1m",
    "b_magenta": "\u001b[35;1m",
    "b_cyan": "\u001b[36;1m",
    "b_white": "\u001b[37;1m",

    "Reset": "\u001b[0m",
}

def Colored(string, color):
    return string if "-m" in sys.argv else ( colors[color] + string + colors["Reset"])


def Clear_Screen():
    print("\033[2J") # erase saved lines
    print("\033[3J") # erase entire screen
    print("\033[H") # moves cursor to home position


def Get_Arguments():
    args_dict = {"colors": []}
    if sys.argv:
        for arg in sys.argv:
            if "-i=" in arg:
                args_dict["intensity"] = int(arg.split("-i=")[1])
            if "-t=" in arg:
                args_dict["timing"] = float(arg.split("-t=")[1])
            if arg in colors:
                args_dict["colors"].append(arg)
    if not args_dict["colors"]:
        del args_dict["colors"]
    return args_dict


def New_Drop():
    for i in range(intensity):
        shape = random.choice(DROPSHAPES)
        color = random.choice(drop_colors)

        raindrop = {
            "shape": Colored(shape, color),
            "x": random.randint(0, xmax),
            "y": 0,
        }
        rainfall.append(raindrop)

def Rain():
    ## iterate over every line
    for i in range(ymax):
        line = " "*xmax

        ### to avoid splicing of ansi codes, splice in the drops from the end of the line
        this_line_raindrops = [raindrop for raindrop in rainfall if raindrop["y"] == i]
        this_line_raindrops.sort(key=lambda y: y["x"])
        this_line_raindrops.reverse()

        ## insert new drops and shift existing drops
        for raindrop in this_line_raindrops:
            x = raindrop["x"]
            line = line[:x] + raindrop["shape"] +line[x:]

        print(line)

    ### update raindrop positions
    for raindrop in rainfall:
        raindrop["y"] += 1

        ## once a raindrop reaches the ground, they splash
        if raindrop["y"] > ymax-2:
            raindrop["shape"] = Colored("o", random.choice(drop_colors))

        # raindrops outside the window evaporate
        if raindrop["y"] > ymax:
            rainfall.remove(raindrop)

    New_Drop()



def Weather_Forecast():
    global weather
    global intensity

    weather += 1
    if weather == 100:
        weather = 0
        intensity += random.choice([-1,1])
        if intensity < 1:
            intensity = 1
        if intensity > 10:
            intensity = 10


size = os.get_terminal_size()
xmax = size.columns
ymax = int(size.lines)

weather = 0
rainfall = []
DROPSHAPES =["|", "│", "┃", "╽", "╿", "║", "┆", "┇", "┊", "┋", "╵", "╹", "╻"]

args = Get_Arguments()
intensity = args.get("intensity", 1)
timing = args.get("timing", 0.08)
drop_colors = args.get("colors", ["blue", "b_blue"])



print('\033[?25l', end="") ## hides the cursor
New_Drop()

try:
    while True:
        Rain()
        time.sleep(timing)
        Clear_Screen()
        Weather_Forecast()

except KeyboardInterrupt:
    Clear_Screen()
    print('\033[?25h', end="") # makes cursor visible again


















