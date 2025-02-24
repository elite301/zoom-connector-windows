import uiautomation as uiauto
import time
import webbrowser
import os
import platform
import pygetwindow as gw
import pyautogui as pag

from uia import clickControl, filterControl
from window import activeWindowBySubTitle, checkWindowByTime, getWindowBySubTitle

def open_zoom(meeting_id, password=None):
  zoom_url = f"zoommtg://zoom.us/join?confno={meeting_id}"
  
  if password:
    zoom_url += f"&pwd={password}"
  
  opened = webbrowser.open(zoom_url)
  print("WebBrowser: ", opened)

def close_zoom():
  if platform.system() == "Windows":
    # Close the Zoom application using the 'taskkill' command
    os.system('taskkill /f /im zoom.exe')
    print("Zoom application closed.")
  else:
    print("This script currently only supports Windows for closing Zoom.")

def automate_zoom():
  # if not checkWindowByTime("Zoom Meeting"):
  #   return False
  
  if checkWindowByTime("Personal Meeting Room"):
    activeWindowBySubTitle("Personal Meeting Room")
    pag.press('enter')
    print("Entered the Personal Meeting Room.")
  
  if checkWindowByTime("Choose one of the audio conference options"):
    gw.getWindowsWithTitle("Choose one of the audio conference options")[0].close()
    print("Closed 'Choose one of the audio conference options' window.")
  
  time.sleep(2)
  
  if gw.getActiveWindowTitle() == "Zoom Workplace": # Do you want to continue without audio?
    gw.getActiveWindow().close()
    print("Closed 'Do you want to continue without audio?' window.")
  
  activeWindowBySubTitle("Zoom Meeting")
  # Share the Screen
  pag.hotkey('alt', 's'); time.sleep(1)
  
  if checkWindowByTime("Select a window or an application that you want to share", 2):
    gw.getWindowsWithTitle("Select a window or an application that you want to share")[0].activate()
    pag.press('tab'); time.sleep(1)
    pag.press('enter')
    print("Shared the screen.")
    
  time.sleep(10)
      
  if checkWindowByTime("Screen sharing meeting controls", 2):
    
    wnd = gw.getWindowsWithTitle("Screen sharing meeting controls")[0]
    wnd.activate()
    
    print("Screen sharing meeting controls")

    control = uiauto.ControlFromHandle(wnd._hWnd)
    
    # Hide Video Panel
    clickControl(control, "More", "SplitButtonControl"); time.sleep(1)
    
    for _ in range(5):
      pag.press('down'); time.sleep(0.5)
      
    pag.press('enter'); time.sleep(0.5)
    
    print("Hide Video Panel")
    
    # Share Laptop Sound
    clickControl(control, "More", "SplitButtonControl"); time.sleep(1)
    
    for _ in range(7):
      pag.press('down'); time.sleep(0.5)
      
    pag.press('enter'); time.sleep(0.5)
    
    for _ in range(2):
      pag.press('down'); time.sleep(0.5)
      
    pag.press('enter'); time.sleep(0.5)
    
    print("Share Laptop Sound")
    
    # Auto Accept Panel
    clickControl(control, "More", "SplitButtonControl"); time.sleep(1)
    
    pag.press('up'); time.sleep(0.5)
      
    pag.press('enter'); time.sleep(0.5)
    
    pag.press('tab'); time.sleep(0.5)
      
    pag.press('enter'); time.sleep(0.5)
    
    print("Auto Accept Panel")
    
    # Share Clipboard
    clickControl(control, "More", "SplitButtonControl"); time.sleep(1)
    
    pag.press('up'); time.sleep(0.5)
      
    pag.press('enter'); time.sleep(0.5)
    
    pag.press('tab'); time.sleep(0.5)
    pag.press('tab'); time.sleep(0.5)
      
    pag.press('enter'); time.sleep(0.5)
    
    print("Share Clipboard")
    
def hide_zoom():
  if checkWindowByTime("Screen sharing meeting controls", 2):
    wnd = gw.getWindowsWithTitle("Screen sharing meeting controls")[0]
    wnd.activate()
    pag.hotkey('ctrl', 'shift', 'alt', 'h')
    wnd.hide()
def key_input(key):
  pag.press(key.split("+"))
  
def hotkey_input(key: str):
  print("Hotkey: ", key.split("+"))
  pag.hotkey(*key.split("+"))