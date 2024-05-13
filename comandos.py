pyintaller --onefile -w codigo.py


-w = se tem janela de interacao com user





import pyautogui
import time
pyautogui.PAUSE = 1



pyautogui.hotkey('win', 'e')
pyautogui.hotkey('win', 'up')
pyautogui.hotkey('win', 'e')



pyautogui.write
pyautogui.press (tecla)
pyautogui.click
pyautogui.hotkey -> combinação de teclas
button="center", button="left", button="right"
pyautogui.click(clicks=2)



#maximizar
pyautogui.hotkey('win','up')


#selecionar linha
Clique no começo da linha e digite 
pyautogui.hotkey('shift','down')


# comentar tudo
seleciona
control k c
# descomentar
control k u



pyautogui.press -- pressiona teclado
pyautogui.click -- mouse



pyautogui.click(clicks=2)



___________

Repete


# Passo 4: Cadastrar um produto
linha = 0

# clicar no campo de código
pyautogui.click(x=745, y=362)

# pegar da tabeba o valor que quero preencher
codigo = tabela.loc[linha, "codigo"]

# preencher campo
pyautogui.write(str(codigo))



--------------


Ir para a barra de endereço	Ctrl + l ou Alt + d ou F6

pyautogui.hotkey('ctrl', 'l')

https://support.google.com/chrome/answer/157179?hl=pt-BR&co=GENIE.Platform%3DDesktop#zippy=%2Catalhos-de-guias-e-janelas%2Catalhos-de-recursos-do-google-chrome%2Catalhos-da-barra-de-endere%C3%A7o