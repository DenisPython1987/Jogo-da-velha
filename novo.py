import numero as nu
import printcores as prt

#Aqui eu crio a tabela base do jogo.
tabela = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#Aqui eu crio a lista que vai receber os números jogados
preenchidos = []

#Aqui eu crio o loop principal
while True:

    #Aqui eu crio o loop do primeiro jogador.
    while True:
        #jogador O

        #Aqui eu crio a tabela principal.
        print(
            f'|{tabela[0]} | {tabela[1]} | {tabela[2]} |\n'
            f'|{tabela[3]} | {tabela[4]} | {tabela[5]} |\n'
            f'|{tabela[6]} | {tabela[7]} | {tabela[8]} |'
        )

        """Aqui eu crio um bloco try-except para garantir que o usuário não 
        digite nada além de números de 1 a 9"""
        try:

            #Aqui o Python pergunta ao usuário o número em que ele vai jogar.
            num = int(input('Qual casa você vai preencher?'))

            #Aqui eu verifico se o número já foi jogado.
            if num in preenchidos:
                print('Essa casa já está ocupada! Escolha outra')
                continue

            #Aqui eu verifico se o número ainda não foi jogado e
            #já atribuo o "O" azul e quebro o while.
            elif num not in preenchidos:
                tabela[num - 1] == prt.azul("O")
                preenchidos.append(num)
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
