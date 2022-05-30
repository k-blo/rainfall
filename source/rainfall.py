#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

import time
import random
import os
import sys



# ANSI escape codes
colors = {
    "Blue": "\u001b[34m",
    "Bright Blue": "\u001b[34;1m",
    "Reset": "\u001b[0m",
}

def Colored(string, color):
    return string if "-m" in sys.argv else ( colors[color] + string + colors["Reset"])
    #return ( colors[color] + string + colors["Reset"])


def new_drop():
    for i in range(intensity):
        shape = random.choice(DROPSHAPES)
        color = random.choice(["Blue", "Bright Blue"])

        raindrop = {
            "shape": Colored(shape, color),
            "x": random.randint(0, xmax),
            "y": 0,
        }
        rainfall.append(raindrop)

def rain():
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
            raindrop["shape"] = Colored("o", random.choice(["Blue", "Bright Blue"]))

        # raindrops outside the window evaporate
        if raindrop["y"] > ymax:
            rainfall.remove(raindrop)

    new_drop()



def weather_forecast():
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
ymax = int(size.lines * 0.6)

weather = 0
rainfall = []
DROPSHAPES =["|", "│", "┃", "╽", "╿", "║", "┆", "┇", "┊", "┋", "╵", "╹", "╻"]

intensity = 1
if len(sys.argv) > 1:
    intensity = (int(sys.argv[2]) if len(sys.argv)>2 else 1) if sys.argv[1]=="-m" else int(sys.argv[1])




print('\033[?25l', end="") ## hides the cursor
new_drop()

try:
    while True: 
        rain()
        time.sleep(0.08)
        print("\033[2J") # erase saved lines
        print("\033[3J") # erase entire screen
        print("\033[H") # moves cursor to home position
        weather_forecast()

except KeyboardInterrupt:
    print("\033[2J") # erase saved lines
    print("\033[3J") # erase entire screen
    print("\033[H") # moves cursor to home position
    print('\033[?25h', end="") # makes cursor visible again


















