"""
Using pyautogui library

PyAutoGUI lets your Python scripts control the mouse and keyboard to automate interactions with other applications. The API is designed to be simple. PyAutoGUI works on Windows, macOS, and Linux, and runs on Python 2 and 3.
"""

import pyautogui

#----------------------------------------------------------------------------------------
# Using screenshot
#----------------------------------------------------------------------------------------
my_screenshot = pyautogui.screenshot()  # type: ignore
my_screenshot.save('/home/juan/Descargas/programacion/ejemplos_python/screen_one.png')

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------