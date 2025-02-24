import uiautomation as uiauto
import time
import webbrowser
import os
import platform
import pygetwindow as gw
import pyautogui as pag

from zoom import automate_zoom, close_zoom, open_zoom

close_zoom()
time.sleep(5)
open_zoom('6943008774', '8TarnQ')
automate_zoom()