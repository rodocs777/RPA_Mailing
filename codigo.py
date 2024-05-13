import pyautogui
import time
pyautogui.PAUSE = 0.3

# abrir o winscp
pyautogui.press("win")
pyautogui.write("winscp")
pyautogui.press("enter")
time.sleep(5)


# abrir pasta da verifone
(x=673, y=526)
pyautogui.scroll(5000)