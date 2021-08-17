import pyautogui
import time
import keyboard

text_file = open("config.txt", "r")
lines = text_file.readline()
text_file.close()


def main():
    while True:
        if keyboard.is_pressed('-'):
            pyautogui.press('enter')
            time.sleep(.3)
            pyautogui.write(lines)
            pyautogui.press('enter')


while True:
    main()