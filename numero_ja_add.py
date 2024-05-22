# _*_ coding: utf-8 _*_

import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 0.5

# NUMERO_DE_REPETICOES = 999

def funcao_para_repetir():
    time.sleep(5.0)

    pyautogui.click(x=1100, y=973)  # Barra de conversa
    mensagem = '''Olá, tudo bem? Bom início de noite!! 

*JÁ VISITOU UM APARTAMENTO DECORADO?*

    Sou o *Rodolfo*, Consultor *SETE 7* pela Imobiliária Abyara. 
Dedicado em realizar sonhos *há mais de 10 anos* 🙏

📍Há interesse em adquirir apartamentos na planta, seja do projeto *"Minha Casa, Minha Vida"*, de *Médio* ou *Alto padrão*?

 ✅ O financiamento pela *Caixa*, possui subsídios disponíveis para oferecer melhor *taxa de juros*.

🎯 Informe *pontos de interesse* como: *região, dormitórios, vagas na garagem, suíte ou itens de lazer* que te mando as opções!
    

🆙 Podemos *agendar* uma visita em um dos nossos *empreendimentos* para conversarmos melhor?
                   
      Estou disponível para qualquer informação. Tudo de bom!! 🙌😃'''
    pyperclip.copy(mensagem)
    pyautogui.hotkey('ctrl', 'v')
    # pyautogui.press('enter')  # Descomente se quiser enviar a mensagem automaticamente

    pyautogui.hotkey('win', 'e')
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'l')
    caminho = r'C:/python/imagem'  # Usando string raw
    pyperclip.copy(caminho)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'c')  # Copia imagens
    pyautogui.hotkey('alt', 'f4')
    pyautogui.click(x=1100, y=973)  # Barra de conversa
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.press('enter')

# for numero in range(NUMERO_DE_REPETICOES):
#    funcao_para_repetir()