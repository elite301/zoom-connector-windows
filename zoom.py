import time
import webbrowser
import os
import platform
import pygetwindow as gw
import pyautogui as pag

from window import activeWindowBySubTitle, checkWindowByTime, getWindowBySubTitle

def open_zoom(meeting_id, password=None):
  zoom_url = f"zoommtg://zoom.us/join?confno={meeting_id}"
  
  if password:
    zoom_url += f"&pwd={password}"
  
  webbrowser.open(zoom_url)

def close_zoom():
  if platform.system() == "Windows":
    # Close the Zoom application using the 'taskkill' command
    os.system('taskkill /f /im zoom.exe')
    print("Zoom application closed.")
  else:
    print("This script currently only supports Windows for closing Zoom.")

def automate_zoom():
  if not checkWindowByTime("Zoom Meeting"):
    return False
  
  if checkWindowByTime("Choose one of the audio conference options", 2):
    gw.getWindowsWithTitle("Choose one of the audio conference options")[0].close()
    print("Closed 'Choose one of the audio conference options' window.")
  
  time.sleep(2)
  
  if gw.getActiveWindowTitle() == "Zoom Workplace": # Do you want to continue without audio?
    gw.getActiveWindow().close()
  
  activeWindowBySubTitle("Zoom Meeting")
  # Share the Screen
  pag.hotkey('alt', 's'); time.sleep(1)
  
  if checkWindowByTime("Select a window or an application that you want to share", 2):
    gw.getWindowsWithTitle("Select a window or an application that you want to share")[0].activate()
    pag.press('tab'); time.sleep(1)
    pag.press('enter')
    
  time.sleep(10)
      
  if checkWindowByTime("Screen sharing meeting controls", 2):
    gw.getWindowsWithTitle("Screen sharing meeting controls")[0].activate()
    
    for _ in range(3):
      pag.hotkey("shift", "tab"); time.sleep(0.5)
    
    # Hide Video Panel
    pag.press('enter'); time.sleep(0.5)
    
    for _ in range(5):
      pag.press('down'); time.sleep(0.5)
      
    pag.press('enter'); time.sleep(0.5)
    
    # Auto Accept Panel
    pag.press('enter'); time.sleep(0.5)
    
    pag.press('up'); time.sleep(0.5)
      
    pag.press('enter'); time.sleep(0.5)
    
    pag.press('tab'); time.sleep(0.5)
      
    pag.press('enter'); time.sleep(0.5)
    
    # Share Clipboard
    
    pag.press('enter'); time.sleep(0.5)
    
    pag.press('up'); time.sleep(0.5)
      
    pag.press('enter'); time.sleep(0.5)
    
    pag.press('tab'); time.sleep(0.5)
    pag.press('tab'); time.sleep(0.5)
      
    pag.press('enter'); time.sleep(0.5)
    
def hide_zoom():
  if checkWindowByTime("Screen sharing meeting controls", 2):
    gw.getWindowsWithTitle("Screen sharing meeting controls")[0].hide()
    pag.hotkey('ctrl', 'shift', 'alt', 'h')