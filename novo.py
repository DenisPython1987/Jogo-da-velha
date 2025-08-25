import printcores as prt
import ver_vitoria
import tabela as tab

#Aqui eu crio uma flag para marcar a vitória de um dos dois lados.
vitoria_empate = True

#Aqui eu crio um contador para verificar um empate.
cont = 0

#Aqui eu crio a tabela principal.
tab.mostrar_tabela()

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
            if tab.tabela[num - 1] in [str(i) for i in range(1, 10)]:
                tab.tabela[num - 1] = prt.azul("O")   
                cont += 1

                #Aqui eu chamo a função para mostrar a tabela
                tab.mostrar_tabela()
                break
            else:
                print("Essa casa já está ocupada!")


        #Aqui eu crio um except para caso o usuário digite algo além de números    
        except ValueError:
            print('Você precisa digitar um número inteiro\n')
            continue

        #Aqui eu crio um except para caso o usuário digite algo que não seja de
        #1 a 9.
        except IndexError:
            print('Você tem que digitar um número de 1 a 9')
            continue
    
    """Aqui eu chamo a função 'Ver_vitória' e conetor com a tabela da função 
    'Tabela'"""
    vit = ver_vitoria.vitoria(tab.tabela)

    #Aqui eu verifico a vitória do azul
    if vit == prt.azul('O'):
        print("Jogador O ganhou ")
        vitoria_empate = False
        break  
    
    #Aqui eu verifico o empate
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
            if tab.tabela[num - 1] in [str(i) for i in range(1, 10)]:
                tab.tabela[num - 1] = prt.vermelho('X')
                cont += 1

                #Aqui eu chamo a função de mostrar a tabela
                tab.mostrar_tabela()
                break
            else:
                print("Essa casa já está ocupada!")


        #Aqui eu crio um except para caso o usuário digite algo além de números    
        except ValueError:
            print('Você precisa digitar um número inteiro\n')
            continue

        #Aqui eu crio um except para caso o usuário digite algo que não seja de
        #1 a 9.
        except IndexError:
            print('Você tem que digitar um número de 1 a 9')
            continue
    #Aqui eu chamo a função 'Ver_vitoria' e conecto com a tabela da função 'tabela'
    vit = ver_vitoria.vitoria(tab.tabela)

    #Aqui eu verifico a vitória do jogador vermelho
    if vit == prt.vermelho('X'):
        print("Jogador X ganhou ")
        vitoria_empate = False
        break  

    #Aqui eu verifico o empate
    if cont == 9:
        print("Empate")
        vitoria_empate = False
        break
