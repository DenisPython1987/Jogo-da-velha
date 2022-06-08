# exercício do jogo da velha
from lib import numero, printcores


def tabela():
    print(f'{pos[0][0]:^3}\033[34m|\033[m{pos[0][1]:^3}\033[34m|\033[m{pos[0][2]:^3}')
    printcores.azul(f'{"-" * 3}+{"-" * 3}+{"-" * 3}')
    print(f'{pos[1][0]:^3}\033[34m|\033[m{pos[1][1]:^3}\033[34m|\033[m{pos[1][2]:^3}')
    printcores.azul(f'{"-" * 3}+{"-" * 3}+{"-" * 3}')
    print(f'{pos[2][0]:^3}\033[34m|\033[m{pos[2][1]:^3}\033[34m|\033[m{pos[2][2]:^3}')


cont = 0
pos = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

while True:
    tabela()

    while True:
        jogador1 = numero.digiteint('\033[35mJOGADOR 1 = Em qual posição você quer jogar? \033[m')
        if 0 < jogador1 > 9:
            printcores.vermelho('Opção inválida! Digite um número de 1 a 9.')
            continue
        if jogador1 == 1:
            if pos[0][0] == ' \033[32mX\033[m ' or pos[0][0] == ' \033[35mO\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[0][0] = ' \033[35mO\033[m '
            break
        elif jogador1 == 2:
            if pos[0][1] == ' \033[32mX\033[m ' or pos[0][1] == ' \033[35mO\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[0][1] = ' \033[35mO\033[m '
            break
        elif jogador1 == 3:
            if pos[0][2] == ' \033[32mX\033[m ' or pos[0][2] == ' \033[35mO\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[0][2] = ' \033[35mO\033[m '
            break
        elif jogador1 == 4:
            if pos[1][0] == ' \033[32mX\033[m ' or pos[1][0] == ' \033[35mO\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[1][0] = ' \033[35mO\033[m '
            break
        elif jogador1 == 5:
            if pos[1][1] == ' \033[32mX\033[m ' or pos[1][1] == ' \033[35mO\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[1][1] = ' \033[35mO\033[m '
            break
        elif jogador1 == 6:
            if pos[1][2] == ' \033[32mX\033[m ' or pos[1][2] == ' \033[35mO\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[1][2] = ' \033[35mO\033[m '
            break
        elif jogador1 == 7:
            if pos[2][0] == ' \033[32mX\033[m ' or pos[2][0] == ' \033[35mO\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[2][0] = ' \033[35mO\033[m '
            break
        elif jogador1 == 8:
            if pos[2][1] == ' \033[32mX\033[m ' or pos[2][1] == ' \033[35mO\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[2][1] = ' \033[35mO\033[m '
            break
        elif jogador1 == 9:
            if pos[2][2] == ' \033[32mX\033[m ' or pos[2][2] == ' \033[35mO\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[2][2] = ' \033[35mO\033[m '
            break

    if pos[0][0] == ' \033[35mO\033[m ' and pos[0][1] == ' \033[35mO\033[m ' and pos[0][2] == ' \033[35mO\033[m ':
        printcores.roxo('jogador 1 venceu!')
        tabela()
        break
    elif pos[1][0] == ' \033[35mO\033[m ' and pos[1][1] == ' \033[35mO\033[m ' and pos[1][2] == ' \033[35mO\033[m ':
        printcores.roxo('jogador 1 venceu!')
        tabela()
        break
    elif pos[2][0] == ' \033[35mO\033[m ' and pos[2][1] == ' \033[35mO\033[m ' and pos[2][2] == ' \033[35mO\033[m ':
        printcores.roxo('jogador 1 venceu!')
        tabela()
        break
    elif pos[0][0] == ' \033[35mO\033[m ' and pos[1][0] == ' \033[35mO\033[m ' and pos[2][0] == ' \033[35mO\033[m ':
        printcores.roxo('jogador 1 venceu!')
        tabela()
        break
    elif pos[0][1] == ' \033[35mO\033[m ' and pos[1][1] == ' \033[35mO\033[m ' and pos[2][1] == ' \033[35mO\033[m ':
        printcores.roxo('jogador 1 venceu!')
        tabela()
        break
    elif pos[0][2] == ' \033[35mO\033[m ' and pos[1][2] == ' \033[35mO\033[m ' and pos[2][2] == ' \033[35mO\033[m ':
        printcores.roxo('jogador 1 venceu!')
        tabela()
        break
    elif pos[0][0] == ' \033[35mO\033[m ' and pos[1][1] == ' \033[35mO\033[m ' and pos[2][2] == ' \033[35mO\033[m ':
        printcores.roxo('jogador 1 venceu!')
        tabela()
        break
    elif pos[2][0] == ' \033[35mO\033[m ' and pos[1][1] == ' \033[35mO\033[m ' and pos[0][2] == ' \033[35mO\033[m ':
        printcores.roxo('jogador 1 venceu!')
        tabela()
        break
    cont += 1
    if cont >= 9:
        tabela()
        printcores.verde('Tivemos um empate!!!')
        break

    tabela()

    while True:
        jogador2 = numero.digiteint('\033[32mJOGADOR 2 = Em qual posição você quer jogar?\033[m ')
        if 0 < jogador2 > 9:
            printcores.vermelho('Opção inválida! Digite um número de 1 a 9.')
            continue
        if jogador2 == 1:
            if pos[0][0] == ' \033[35mO\033[m ' or pos[0][0] == ' \033[32mX\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[0][0] = ' \033[32mX\033[m '
            break
        elif jogador2 == 2:
            if pos[0][1] == ' \033[35mO\033[m ' or pos[0][1] == ' \033[32mX\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[0][1] = ' \033[32mX\033[m '
            break
        elif jogador2 == 3:
            if pos[0][2] == ' \033[35mO\033[m ' or pos[0][2] == ' \033[32mX\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[0][2] = ' \033[32mX\033[m '
            break
        elif jogador2 == 4:
            if pos[1][0] == ' \033[35mO\033[m ' or pos[1][0] == ' \033[32mX\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[1][0] = ' \033[32mX\033[m '
            break
        elif jogador2 == 5:
            if pos[1][1] == ' \033[35mO\033[m ' or pos[1][1] == ' \033[32mX\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[1][1] = ' \033[32mX\033[m '
            break
        elif jogador2 == 6:
            if pos[1][2] == ' \033[35mO\033[m ' or pos[1][2] == ' \033[32mX\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[1][2] = ' \033[32mX\033[m '
            break
        elif jogador2 == 7:
            if pos[2][0] == ' \033[35mO\033[m ' or pos[2][0] == ' \033[32mX\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[2][0] = ' \033[32mX\033[m '
            break
        elif jogador2 == 8:
            if pos[2][1] == ' \033[35mO\033[m ' or pos[2][1] == ' \033[32mX\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[2][1] = ' \033[32mX\033[m '
            break
        elif jogador2 == 9:
            if pos[2][2] == ' \033[35mO\033[m ' or pos[2][2] == ' \033[32mX\033[m ':
                printcores.vermelho('Esta casa já está ocupada, escolha outra!')
                continue
            pos[2][2] = ' \033[32mX\033[m '
            break

    if pos[0][0] == ' \033[32mX\033[m ' and pos[0][1] == ' \033[32mX\033[m ' and pos[0][2] == ' \033[32mX\033[m ':
        print('jogador 2 venceu!')
        tabela()
        break
    elif pos[1][0] == ' \033[32mX\033[m ' and pos[1][1] == ' \033[32mX\033[m ' and pos[1][2] == ' \033[32mX\033[m ':
        print('jogador 2 venceu!')
        tabela()
        break
    elif pos[2][0] == ' \033[32mX\033[m ' and pos[2][1] == ' \033[32mX\033[m ' and pos[2][2] == ' \033[32mX\033[m ':
        print('jogador 2 venceu!')
        tabela()
        break
    elif pos[0][0] == ' \033[32mX\033[m ' and pos[1][0] == ' \033[32mX\033[m ' and pos[2][0] == ' \033[32mX\033[m ':
        print('jogador 2 venceu!')
        tabela()
        break
    elif pos[0][1] == ' \033[32mX\033[m ' and pos[1][1] == ' \033[32mX\033[m ' and pos[2][1] == ' \033[32mX\033[m ':
        print('jogador 2 venceu!')
        tabela()
        break
    elif pos[0][2] == ' \033[32mX\033[m ' and pos[1][2] == ' \033[32mX\033[m ' and pos[2][2] == ' \033[32mX\033[m ':
        print('jogador 2 venceu!')
        tabela()
        break
    elif pos[0][0] == ' \033[32mX\033[m ' and pos[1][1] == ' \033[32mX\033[m ' and pos[2][2] == ' \033[32mX\033[m ':
        print('jogador 2 venceu!')
        tabela()
        break
    elif pos[2][0] == ' \033[32mX\033[m ' and pos[1][1] == ' \033[32mX\033[m ' and pos[0][2] == ' \033[32mX\033[m ':
        print('jogador 2 venceu!')
        tabela()
        break
    cont += 1
