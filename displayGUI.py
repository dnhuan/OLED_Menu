#!/usr/bin/python
# -*- coding:utf-8 -*-\
from __future__ import print_function

import time

import SH1106
import utils as u

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


## Init SPI
disp = SH1106.SH1106()
disp.Init()
disp.clear()

## Init fonts
font = ImageFont.load_default()

image = Image.new('1', (disp.width, disp.height), 1)
draw = ImageDraw.Draw(image)

def blank_display():
    draw.rectangle((0,0,disp.width-1,disp.height-1), outline=1, fill=1)

def show_display():
    disp.ShowImage(disp.getbuffer(image))


## Menu
padding = -2
top = padding
bottom = disp.height - padding
line1 = top
line2 = top+8
line3 = top+16
line4 = top+25
line5 = top+34
line6 = top+43
line7 = top+52

def display_text(l1,l2,l3,l4,l5,l6,l7):
    draw.text((0, line1), l1, font=font, fill=0)
    draw.text((0, line2), l2, font=font, fill=0)
    draw.text((0, line3), l3, font=font, fill=0)
    draw.text((0, line4), l4, font=font, fill=0)
    draw.text((0, line5), l5, font=font, fill=0)
    draw.text((0, line6), l6, font=font, fill=0)
    draw.text((0, line7), l7, font=font, fill=0)

def handle_display():
    ## parse data from gui_buffer
    display_text(
        u.gui_buffer[0],
        u.gui_buffer[1],
        u.gui_buffer[2],
        u.gui_buffer[3],
        u.gui_buffer[4],
        u.gui_buffer[5],
        u.gui_buffer[6]
    )

def init():
    while 1:
        if u.display_on_off == True:
            blank_display()
            handle_display() # Customzie display
            show_display()
            u.already = False
        else:
            if u.already == False:
                blank_display()
                show_display()
                u.already = True
            time.sleep(0.5)

