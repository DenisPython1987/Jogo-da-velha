import printcores as prt
import ver_vitoria

#Aqui eu crio a tabela base do jogo.
tabela = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#Aqui eu crio uma flag para marcar a vitória de um dos dois lados.
vitoria_empate = True

#Aqui eu crio um contador para verificar um empate.
cont = 0

#Aqui eu crio a tabela principal.
print(
    f'|{tabela[0]} | {tabela[1]} | {tabela[2]} |\n'
    f'|{tabela[3]} | {tabela[4]} | {tabela[5]} |\n'
    f'|{tabela[6]} | {tabela[7]} | {tabela[8]} |'
)
#Aqui eu crio o loop principal
while vitoria_empate:

    #Aqui eu crio o loop do primeiro jogador.
    while True:
        #jogador O
        

        """Aqui eu crio um bloco try-except para garantir que o usuário não 
        digite nada além de números de 1 a 9"""
        try:

            #Aqui o Python pergunta ao usuário o número em que ele vai jogar.
            num = int(input('(Jogador O) Qual casa você vai preencher?'))

            #Aqui eu verifico se o número já foi jogado.
            if tabela[num - 1] not in [str(i) for i in range(1, 10)]:
                print("Essa casa já está ocupada!")
                continue


            #Aqui eu verifico se o número ainda não foi jogado e
            #já atribuo o "O" azul e quebro o while.
            elif tabela[num - 1] != "O":
                tabela[num - 1] = "O"
                cont += 1
                print(
                    f'|{tabela[0]} | {tabela[1]} | {tabela[2]} |\n'
                    f'|{tabela[3]} | {tabela[4]} | {tabela[5]} |\n'
                    f'|{tabela[6]} | {tabela[7]} | {tabela[8]} |'
                )
                break

        #Aqui eu crio um except para caso o usuário digite algo além de números    
        except ValueError:
            print('Você precisa digitar um número inteiro\n')
            continue

        #Aqui eu crio um except para caso o usuário digite algo que não seja de
        #1 a 9.
        except IndexError:
            print('Você tem que digitar um número de 1 a 9')
            continue
    vit = ver_vitoria.vitoria(tabela)
    if vit == 'O':
        print("Jogador O ganhou ")
        vitoria_empate = False
        break  

    if cont == 9:
        print("Empate")
        vitoria_empate = False
        break 
    

            #Aqui eu crio o loop do segundo jogador.
    while True:
        #jogador X
       

        """Aqui eu crio um bloco try-except para garantir que o usuário não 
        digite nada além de números de 1 a 9"""
        try:

            #Aqui o Python pergunta ao usuário o número em que ele vai jogar.
            num = int(input('(Jogador X) Qual casa você vai preencher?'))

            #Aqui eu verifico se o número já foi jogado.
            if tabela[num - 1] not in [str(i) for i in range(1, 10)]:
                print("Essa casa já está ocupada!")
                continue


            #Aqui eu verifico se o número ainda não foi jogado e
            #já atribuo o "O" azul e quebro o while.
            elif tabela[num - 1] != 'X':
                tabela[num - 1] = "X"
                cont += 1
                print(
                    f'|{tabela[0]} | {tabela[1]} | {tabela[2]} |\n'
                    f'|{tabela[3]} | {tabela[4]} | {tabela[5]} |\n'
                    f'|{tabela[6]} | {tabela[7]} | {tabela[8]} |'
                )
                break

        #Aqui eu crio um except para caso o usuário digite algo além de números    
        except ValueError:
            print('Você precisa digitar um número inteiro\n')
            continue

        #Aqui eu crio um except para caso o usuário digite algo que não seja de
        #1 a 9.
        except IndexError:
            print('Você tem que digitar um número de 1 a 9')
            continue

    vit = ver_vitoria.vitoria(tabela)
    if vit == 'X':
        print("Jogador X ganhou ")
        vitoria_empate = False
        break  

    if cont == 9:
        print("Empate")
        vitoria_empate = False
        break
