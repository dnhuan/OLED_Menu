already = False
display_on_off = True
page = -1
cursor = 0
gui_buffer = []
mainmenu_list = {}
brightness = 0
v6 = 0 #ipv6 len index

def init():
    global already, display_on_off, cursor, mainmenu_list, gui_buffer, v6, brightness
    already = False
    display_on_off = True
    page = -1
    cursor = 0
    v6 = 0
    brightness = 0
    gui_buffer = ["","","","","","",""]
    mainmenu_list = [
        "System info",          #   0
        "%Connect to wifi%",    #   1
        "b",                    #   2
        "c",                    #   3
        "d",                    #   4
        "Shutdown",             #   5
        "Reboot",               #   6
        "Reset all configs"     #   7
    ]