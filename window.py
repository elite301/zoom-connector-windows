import time
import pygetwindow as gw

def is_window_open(window_title_substring):
    windows = gw.getWindowsWithTitle(window_title_substring)
    if windows:
        print(f"Window with title containing '{window_title_substring}' is open.")
        return True
    else:
        print(f"No window with title containing '{window_title_substring}' is open.")
        return False

def getActiveWindowTitle():
    return gw.getActiveWindow().title

def getWindowBySubTitle(window_title_substring):
  for title in gw.getAllTitles():
    if window_title_substring in title:
      return True
  return False

def checkWindowByTime(window_title, limit = 5, time_interval = 5):
  for _ in range(limit):
    if getWindowBySubTitle(window_title):
      return True
    else:
      time.sleep(time_interval)
  return False

def activeWindowBySubTitle(window_title_substring):
  for title in gw.getAllTitles():
    if window_title_substring in title:
      gw.getWindowsWithTitle(title)[0].activate()
      return True
  return False