# _*_ coding: utf-8 _*_

import pyautogui
import time

pyautogui.PAUSE = 0.3

NUMERO_DE_REPETICOES = 999

def funcao_para_repetir():
    time.sleep(5.0)

    pyautogui.click(clicks=3)  # Seleciona números
    pyautogui.hotkey('ctrl', 'c')

    pyautogui.click(x=320, y=174)  # Procura números no WhatsApp
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("enter")  # Procura números

    time.sleep(1.5)

    pyautogui.click(x=1218, y=632) # ok do não achou número

for numero in range(NUMERO_DE_REPETICOES):
    funcao_para_repetir()