#automação de tarefas e bots
#bibliotecas = pacotes de códigos
#pip install pyautogui
#passo 1 entrar no sistema da empresa 
#passo 2 fazer login
# abrir a base de dados
#cadastrar pdroduto
#repetir o passo 4 até acabar a lista de produtos
# biblioteca time carrega o tempo
import pyautogui
import time 
#pyautogui.click = click
#pyautogui.write = escreve texto
#pyautogui.press= aperta tecla
#pyautogui.hotkey = aperta atalho

#passo 1 entrar no sistema da empresa 
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
#fazer pausa maior pro site carregar
time.sleep(3)

#passo 2 fazer login
#clicar no campo de email
pyautogui.click(x=674, y=447)
pyautogui.write("teste123@gmail.com")
#passar pro proximo campo
pyautogui.press("tab")
pyautogui.write("senha123")
#passar para o botao
pyautogui.press("tab")
pyautogui.press("enter")
#fazer pausa maior pro site carregar
time.sleep(4)
# abrir a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)
#para cada linha da minha tabela
for linha in tabela.index:
    
    #cadastrar pdroduto
    pyautogui.click(x = 682, y=301)
    #localizar tabela
    codigo = str(tabela.loc[linha,"codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #categoria
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #preço
    preco = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    #custo
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #obs
    obs = str(tabela.loc[linha,"obs"])
    pyautogui.write(obs)
    pyautogui.press("tab") #passar pro botao enviar

    pyautogui.press("enter")#clicou no enviar
    #voltar pro inicio da  tela
    pyautogui.scroll(5000)

#repetir o passo 4 até acabar a lista de produtos
#repetir processo

