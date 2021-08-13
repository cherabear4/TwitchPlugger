import pyautogui
import time
import keyboard

text_file = open("config.txt", "r")
lines = text_file.readline()
print(lines)
text_file.close()


def plug():
    if keyboard.is_pressed('ctrl+shift'):
        while True:
            pyautogui.press('enter')
            time.sleep(.3)
            pyautogui.write('go follow me on ' + 'twitch ' +
                            '@' + lines)
            pyautogui.press('enter')


plug()
