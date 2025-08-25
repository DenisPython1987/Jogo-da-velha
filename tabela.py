import os
import printcores as prt

#Aqui eu crio a tabela base do jogo.
tabela = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def apagar_tela():
    "Função para limpar a tela do terminal"

    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')

def mostrar_tabela():
    "função para mostrar tabela"

    apagar_tela()
    print(
        f'|{prt.verde(tabela[0])} | {prt.verde(tabela[1])} | {prt.verde(tabela[2])} |\n'
        f'|{prt.verde(tabela[3])} | {prt.verde(tabela[4])} | {prt.verde(tabela[5])} |\n'
        f'|{prt.verde(tabela[6])} | {prt.verde(tabela[7])} | {prt.verde(tabela[8])} |'
    )