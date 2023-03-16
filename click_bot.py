import pyautogui

clicked = False
while True:
    x, y = pyautogui.position()
    if pyautogui.mouseDown():
        clicked = True
        clicked_x, clicked_y = x, y
        print(f"Mouse clicked at position ({clicked_x}, {clicked_y})")
    if clicked and pyautogui.press('c'):
        pyautogui.moveTo(clicked_x, clicked_y)
        pyautogui.click()
        print(f"Mouse moved to ({clicked_x}, {clicked_y}) and clicked")
        clicked = False