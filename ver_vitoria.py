import printcores as prt


def vitoria(lista):
    """Função para verificar a vitória"""

    """Aqui eu verifico as linhas. A lógica é somar 1 para o segundo item e 
    2 para o terceiro item, o item um é o próprio i"""
    for i in range(3):
        if lista[i] == prt.vermelho("X") and lista[i + 1] == prt.vermelho("X") and lista[i + 2] == prt.vermelho("X"):
            return prt.vermelho("X")
    
    """Aqui eu verifico as diagonais. A lógica é que as diagonais são uma soma entre 
    números de 0 a 4 e o 2 e o 4"""
    for j in range(0, 4):
        if j % 2 == 0:
            if lista[j] == prt.vermelho("X") and lista[j + 2] == prt.vermelho("X") and lista[j + 4] == prt.vermelho("X"):
                return prt.vermelho("X")
            
    """Aqui eu verifico as colunas. A lógica é que as colunas são uma sequência 
    de somas de números de 0 a 2 e os números 3 e 6"""
    for g in range(0, 2):
        if lista[g] == prt.vermelho("X") and lista[g + 3] == prt.vermelho("X") and lista[g + 6] == prt.vermelho("X"):
            return prt.vermelho("X")

    """Aqui eu verifico as linhas. A lógica é somar 1 para o segundo item e 
    2 para o terceiro item, o item um é o próprio i"""
    for i in range(3):
        if lista[i] == prt.azul("O") and lista[i + 1] == prt.azul("O") and lista[i + 2] == prt.azul("O"):
            return prt.azul("O")
        
    """Aqui eu verifico as diagonais. A lógica é que as diagonais são uma soma entre 
    números de 0 a 4 e o 2 e o 4"""
    for j in range(0, 4):
        if j % 2 == 0:
            if lista[j] == prt.azul("O") and lista[j + 2] == prt.azul("O") and lista[j + 4] == prt.azul("O"):
                return prt.azul("O")
            
    """Aqui eu verifico as colunas. A lógica é que as colunas são uma sequência 
    de somas de números de 0 a 2 e os números 3 e 6"""
    for g in range(0, 2):
        if lista[g] == prt.azul("O") and lista[g + 3] == prt.azul("O") and lista[g + 6] == prt.azul("O"):
            return prt.azul("O")