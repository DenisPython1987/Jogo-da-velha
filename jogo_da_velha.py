def posição(lista, pos, símbolo):
    for i in range(0, 3):
        for j in range(0, 3):
            if lista[i][j] == pos:
                lista[i][j] = símbolo
                return 

def verifica_vitória(lista, símbolo):
    if (lista[0][0] == símbolo and lista[1][1] == símbolo and lista[2][2] == símbolo) or (lista[0][2] == símbolo and lista[1][1] == símbolo and lista[2][0] == símbolo) or (lista[0][0] == símbolo and lista[0][1] == símbolo and lista[0][2] == símbolo) or (lista[1][0] == símbolo and lista[1][1] == símbolo and lista[1][2] == símbolo) or (lista[2][0] == símbolo and lista[2][1] == símbolo and lista[2][2] == símbolo) or (lista[0][0] == símbolo and lista[1][0] == símbolo and lista[2][0] == símbolo) or (lista[0][1] == símbolo and lista[1][1] == símbolo and lista[2][1] == símbolo) or (lista[0][2] == símbolo and lista[1][2] == símbolo and lista[2][2] == símbolo):
        return True
    return False
        
def mostra_grade():
    saudação = "\033[35mJOGO DA VELHA"
    print(f"{saudação:^40}")
    print("-*-" * 20)
    print("\033m")
    for i in range(0, 3):
        for m in grade[i]:
            print(f"\033[35m{m}\033[m", end="         ")
        print("\n")
    print("\033[35m-*-" * 20)
    print("\033[m")
        

grade = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
vitória = False

while True:
    mostra_grade()
    while True:
        try:
            jogador_1 = int(input("\033[36mJOGADOR 1 - Escolha uma posição: \033[m"))
            if jogador_1 < 1 or jogador_1 > 9:
                print("\033[31mOpção inválida! Digite um número inteiro entre 1 e 9\033[m.")
                continue
            if 0 < jogador_1 < 10:
                posição(grade, jogador_1, '\033[36mX\033[m')
                break
        except ValueError:
            print("\033[31mOpção inválida! Digite um número inteiro entre 1 e 9\033[m.")
            continue
    vitória = verifica_vitória(grade, '\033[36mX\033[m')
    if vitória:
        mostra_grade()
        print("\033[32mO jogador 1 GANHOU, PARABÉNS!\033[m")
        break
    mostra_grade()
    while True:
        try:
            jogador_2 = int(input("\033[34mJOGADOR 2 - Escolha sua posição: \033[m"))
            if jogador_2 < 1 or jogador_2 > 9:
                print("\033[31mOpção inválida! Digite um número inteiro entre 1 e 9\033[m.")
                continue
            if 0 < jogador_2 < 10:
                posição(grade, jogador_2, "\033[34mO\033[m")
                break
        except ValueError:
            print("\033[31mOpção inválida! Digite um número inteiro entre 1 e 9\033[m.")
            continue
    vitória = verifica_vitória(grade, "\033[34mO\033[m")
    if vitória:
        mostra_grade()
        print("\033[32mO jogador 2 GANHOU, PARABÉNS!\033[m")
        break
    