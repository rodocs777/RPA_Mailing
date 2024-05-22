# _*_ coding: utf-8 _*_

import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 0.4


# pyautogui.press("win") --> tecla
# pyautogui.write("winscp")
# pyautogui.click --> mouse
# pyautogui.click(clicks=2)

# pyautogui.press("enter")
# time.sleep(5)

# pyautogui.hotkey('win', 'e')
# pyautogui.hotkey('win', 'up')
# pyautogui.hotkey('win', 'e')

# pyautogui.hotkey -> combinação de teclas
# button="center", button="left", button="right"

NUMERO_DE_REPETICOES = 999

def funcao_para_repetir():

    time.sleep(5)

    pyautogui.click(clicks=3) ## seleciona numeros
    pyautogui.hotkey('ctrl', 'c')

    pyautogui.click(x=320, y=174) ## procura numeros no whats
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("enter") ## procura numeros

    time.sleep(2)

    pyautogui.click(x=1100, y=973) ## barra de conversa
    pyperclip.copy('''Olá, tudo bem? 

JÁ VISITOU UM APARTAMENTO DECORADO?

    Sou o Rodolfo, Consultor SETE pela Imobiliária Abyara. 
Dedicado em realizar sonhos há mais de 10 anos 🙏

📍Há interesse em adquirir apartamentos na planta, seja do projeto "Minha Casa, Minha Vida", de Médio ou Alto padrão?

 ✅ O financiamento pela Caixa, possui subsídios disponíveis para abater e oferecer a melhor taxa de juros 

🎯 Informe pontos de interesse como: região, dormitórios, vagas na garagem, suíte ou itens de lazer, que te mando as opções!
    

🆙 Podemos agendar uma visita em um dos nossos empreendimentos para conversarmos melhor?
                   
      Estou disponível para qualquer informação. Tudo de bom!! 🙌😃''')
    
    pyautogui.hotkey('ctrl', 'v')
    # pyautogui.press('enter')


    pyautogui.hotkey('win', 'e')
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'l')
    pyperclip.copy('C:/python/imagem')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'c') ## copia imagens
    pyautogui.hotkey('alt', 'f4')
    pyautogui.click(x=1100, y=973) ## barra de conversa
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1.5)
    pyautogui.press('enter')


for numero in range(0, NUMERO_DE_REPETICOES):
    funcao_para_repetir