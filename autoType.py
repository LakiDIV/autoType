import pyautogui
import time
import pyfiglet

# Intro
program_name = pyfiglet.figlet_format("autoType")
print(program_name + 'v0.1')

# Input
text = input("Text: ")

while True:
    try:
        value = int(input("Loop: "))
        break
    except ValueError:
        print("Use a valid input!")

while True:
    try:
        sec = int(input("Delay (sec) - "))
        break
    except ValueError:
        print("Use a valid input!")

press_enter = True

# Delay
for i in reversed(range(sec)):
    print(f"Start in {i} seconds...")
    time.sleep(1)

# Loop
count = 1
while count <= value:
    pyautogui.typewrite(text)
    if press_enter:
        pyautogui.press("enter")
    count += 1
