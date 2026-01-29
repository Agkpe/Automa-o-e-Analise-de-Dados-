# Automatização de tarefas (POWER UP) - Cadastro de itens
# Passo 1 - Acessar o sistema da empresa
# Passo 2 - Fazer login
# Passo 3 - Abrir a base de dados 
# Passo 4 - Cadastrar 1 produto 
# Passo 5 - Repete passo 4 até acabar lista de itens
#Importando biblioteca 
import pyautogui   # Biblioteca para automatização
import time

    
# Passo 1 - Acessar o sistema da empresa 
# abrir o navegador
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")
time.sleep (2)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep (5)

# Passo 2 - Fazer login
# Fazer cadastro
pyautogui.click(x=1175, y=467)
time.sleep (2)
email = "emailaleatorio@gmail.com"
pyautogui.write(email)

time.sleep(2)
pyautogui.press("tab") # passa para o prox campo
senha = "senhamtdificil"
pyautogui.write(senha)

pyautogui.press("enter")
time.sleep(2)

#Passo 3 - Abrir a base do produto  - Pip install pandas openpyxl
#  Pandas - Banco de dados
#  Openpyxl - Pandas trabalha com Excel
import pandas

tabela = pandas.read_csv("produtos (1).csv") # Importando / Lê arquivo para dentro de um código

print(tabela)

for linhas in tabela.index:   # Passo 5 - Para cada linha na tabela. (index) representa indice - número da linha / linha = index / O index foi escolhido pq cada linha repreta um item

    # Passo 4 - Cadastrar um produto
    pyautogui.click(x=993, y=329) # Seleciona  campo cód produto
    #codigo
    codigo = tabela.loc[linhas, "codigo"]  # Para localizar a coluna "codigo" na tabela / Tabela no python, procura informação em colchete
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    marca = tabela.loc[linhas, "marca"] # localizar a coluna "marca" e etc / o loc é responsável por localizar a linha e a coluna pedida
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo do produto
    tipo = tabela.loc[linhas, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #categoria do produto
    categoria = str(tabela.loc[linhas, "categoria"])  # o str utilizado transforma o número em sting, para que o programa o leia como algo de se ler e não de fazer conta
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #preço unitário
    preco = str(tabela.loc[linhas, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    #Custo 
    custo = str(tabela.loc[linhas, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #obs
    obs = str(tabela.loc[linhas, "obs"])
    if obs != "nan":        # Se a observação for diferente de "nan"
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter") # clica em enviar
    time.sleep(7)
    #Voltar para o inicio da tela
    pyautogui.scroll(10000)
# Passo 5 - Repetir passo 4 até a base de dados acabar

#Informação extra, caso queira pocurar aba no excel, colocar/  pandas.read_excel(sheet_name=nomedaba)