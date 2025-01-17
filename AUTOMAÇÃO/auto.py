import pyautogui
import time
import pandas as pd

#1 logar

#entra no sistema
pyautogui.PAUSE = 1
pyautogui.press("win") # -> pressiona 
pyautogui.write("Opera") # -> escreve
pyautogui.press("enter")
time.sleep(5)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#email
time.sleep(2)
pyautogui.click(x=768, y=494)
pyautogui.write("leandrade@gmail.com")

#senha
pyautogui.press("tab")
pyautogui.write("eutomeiumprejuizocomo")

#completar login
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)
#2 insirir dados
tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=753, y=344)
    # codigo
    cod = tabela.loc[linha, "codigo"]
    pyautogui.write(str(cod))
    pyautogui.press("tab")
    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    # tipo
    tp = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tp))
    pyautogui.press("tab")
    # categoria
    cat = tabela.loc[linha, "categoria"]
    pyautogui.write(str(cat))
    pyautogui.press("tab")
    # preco_unitario
    pu =tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(pu))
    pyautogui.press("tab")
    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(obs))  
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(10000)
