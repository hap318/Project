import keyboard as keyboard
import pyautogui

poi = [(255, 187, 125),
       (255, 220, 152),
       (255, 215, 146),
       (255, 218, 147),
       (255, 216, 148)]

while True:
    screen = pyautogui.screenshot()
    for x in range(550, 1350, 4):
        for y in range(140, 930, 4):
            color = screen.getpixel((x, y))
            if (color == i for i in poi):
                pyautogui.click(x, y)
            # elif color == (107,163,248):
            #     pyautogui.click(x, y)




