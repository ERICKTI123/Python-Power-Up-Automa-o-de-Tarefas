import pyautogui # importando biblioteca de automações
import pandas as pd # importando pandas para abrir base de dados 


# entrar no site da empresa para cadastrar - https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.PAUSE = 1.5

# entrar no navegador 
pyautogui.click(x=790, y=752)
pyautogui.hotkey("ctrl", "t")
pyautogui.write(" https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


# fazer loggin na página

# apertando no "email"
pyautogui.click(x=406, y=414)
pyautogui.write("-------------------") # e-mail

# apertando tab pra pular para o campo senha e logo em seguida escrever a senha, depois apertar o enter 
pyautogui.press("tab")
pyautogui.write("---------") # senha
pyautogui.press("enter")

# importar a base de dados 
arquivo = pd.read_csv("Produtos.csv")
print(arquivo)

for linha in arquivo.index:

    # cadastrar os produtos 
    # código
    codigo = arquivo.loc[linha, "codigo"]
    pyautogui.click(x=567, y=304)
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = arquivo.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = arquivo.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = arquivo.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preço
    preco_unitario = arquivo.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = arquivo.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs 
    obs = arquivo.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    
    # apertar o enter
    pyautogui.press("enter")
    pyautogui.scroll(5000)




