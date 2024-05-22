# _*_ coding: utf-8 _*_

import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 0.3


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


    pyautogui.click(x=320, y=174)
    pyautogui.hotkey('ctrl', 'v')


    pyautogui.press("enter") ## procura numeros

    time.sleep(2)

    pyautogui.click(x=1100, y=973) ## barra de conversa


    pyperclip.copy('''Olá, tudo bem?

    Sou o *Rodolfo*, Consultor *SETE* pela Imobiliária Abyara. 
Dedicado em realizar sonhos *há mais de 10 anos*.

    Gostaria de saber se há interesse em adquirir apartamentos na planta, seja do projeto *"Minha Casa, Minha Vida"*, ou de *Médio* e *Alto padrão*?

    Pode utilizar o financiamento pela *Caixa*, que possui subsídios disponíveis para abater e oferecer a melhor *taxa de juros.*

    Por favor, informe *pontos de interesse* como: *região, dormitórios, vagas na garagem, suíte ou itens de lazer*, que te mando as opções!


    Podemos *agendar* uma visita em um dos nossos *empreendimentos* para conversarmos melhor?
                   
                   Obrigado e espero seu interesse! Tudo de bom ")''')
    
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.press("enter")




for numero in range(0, NUMERO_DE_REPETICOES):
    funcao_para_repetir()