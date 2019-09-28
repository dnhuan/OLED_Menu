import time
import datetime
import subprocess
import utils as u
import config as c


def shell(cmd):
    return(subprocess.check_output(cmd, shell = True ))

def get_ip():
    cmd = "hostname -I"
    return shell(cmd).split(" ")

def get_max_ip_len():
    tmp = 0
    ip_list = get_ip()
    for i in range(len(ip_list)):
        tmp = max(tmp, len(ip_list[i]))
    return tmp


def sysinfos(channel):
    _id = 0
    i = u.v6
    if channel == 0:
        if u.page != _id:
            #init
            u.page = _id
            u.cursor = 0
        now = datetime.datetime.now()
        today_time = now.strftime("%H:%M:%S")
        today_date = now.strftime("%d %b %y")
        try:
	        IP1, IP2, IP3 = get_ip()
        except:
	        IP1= get_ip()[0]
	        IP2= "Nan"
	        IP3= "Nan"
        cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell = True )
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell = True )
        cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
        Disk = subprocess.check_output(cmd, shell = True )
        u.gui_buffer = [
            str(CPU),
            str(MemUsage),
            str(Disk),
            "IP1: " + str(IP1)[i:i+14],
            "IP2: " + str(IP2)[i:i+14],
            "IP3: " + str(IP3)[i:i+14],
            today_date + " " + today_time,
        ]

    elif channel == c.KEY_PRESS_PIN:
        sysinfos(0)

    elif channel == c.KEY1_PIN:
        sysinfos(0)

    elif channel == c.KEY_LEFT_PIN:
        if u.v6 > 0:
            u.v6 -= 1
        sysinfos(0)

    elif channel == c.KEY_RIGHT_PIN:
        if u.v6 < get_max_ip_len() - 1:
            u.v6 += 1
        sysinfos(0)

    elif channel == c.KEY2_PIN:
        mainmenu(0)


def select_module(_id):
    if   _id == 0:
        #system info
        sysinfos(0)

    elif _id == 1:
        return 0

    elif _id == 2:
        return 0

    elif _id == 3:
        return 0

    elif _id == 4:
        return 0

    elif _id == 5:
        shell("sudo poweroff")

    elif _id == 6:
        shell("sudo reboot")

def mainmenu(channel):
    _id = -1
    if channel == 0:
        if u.page != _id:
            #init
            u.page = _id
            u.cursor = 0
        for index in range(7):
            i = index + u.cursor
            if index == 0:
                u.gui_buffer[index] = "> " + str(u.mainmenu_list[i] if i < len(u.mainmenu_list) else "")
            else:
                u.gui_buffer[index] = "  " + str(u.mainmenu_list[i] if i < len(u.mainmenu_list) else "")

    elif channel == c.KEY_UP_PIN:
        if u.cursor > 0:
            u.cursor -= 1
            mainmenu(0)

    elif channel == c.KEY_DOWN_PIN:
        if u.cursor < len(u.mainmenu_list) - 1:
            u.cursor += 1
            mainmenu(0)

    elif channel == c.KEY_LEFT_PIN:
        return 0
    elif channel == c.KEY_RIGHT_PIN:
        return 0

    elif channel == c.KEY_PRESS_PIN:
        select_module(u.cursor)

    elif channel == c.KEY1_PIN:
        select_module(u.cursor)

    elif channel == c.KEY2_PIN:
        return 0
    elif channel == c.KEY3_PIN:
        return 0

def key_handler(channel):
    if u.page == -1:
        mainmenu(channel)
    if u.page == 0:
        u.pending = True
        sysinfos(channel)
