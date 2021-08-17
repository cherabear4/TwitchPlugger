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

def creator():
                print("""______          _    _               __                  _        _     _      _                       
| ___ \        | |  | |             / /                 | |      | |   | |    | |                      
| |_/ /_   _   | |_ | |___   __    / /    ___  ___ _   _| |_ __ _| |__ | | ___| |_ _   _ ___  ___ _ __ 
| ___ \ | | |  | __|| __\ \ / /   / /    / _ \/ __| | | | __/ _` | '_ \| |/ _ \ __| | | / __|/ _ \ '__|
| |_/ / |_| |  | |_ | |_ \ V /   / /    | (_) \__ \ |_| | || (_| | |_) | |  __/ |_| |_| \__ \  __/ |   
\____/ \__, |   \__(_)__| \_/   /_/      \___/|___/\__,_|\__\__,_|_.__/|_|\___|\__|\__,_|___/\___|_|   
        __/ |                                                                                          
       |___/   """)

creator()

while True:
    main()