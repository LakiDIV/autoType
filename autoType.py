import pyautogui
import time

# Input
text = input("Text: ")
value = int(input("Loop: "))
sec = int(input("Delay (sec) - "))

# Delay
for i in reversed(range(sec)):
    print(f"Start in {i} seconds...")
    time.sleep(1)

# Loop
count = 1
while count <= value:
    pyautogui.typewrite(text)
    pyautogui.press("enter")
    count += 1
