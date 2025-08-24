def vitoria(lista):
    """Função para verificar a vitória"""

    for i in range(3):
        if lista[i] == "X" and lista[i + 1] == "X" and lista[i + 2] == 'X':
            return 'X'
        
    for j in range(0, 4):
        if j % 2 == 0:
            if lista[j] == "X" and lista[j + 2] == "X" and lista[j + 4] == 'X':
                return 'X'

    for g in range(0, 2):
        if lista[g] == "X" and lista[g + 3] == "X" and lista[g + 6] == "X":
            return 'X'

    for i in range(3):
        if lista[i] == "O" and lista[i + 1] == "O" and lista[i + 2] == 'O':
            return 'O'
        
    for j in range(0, 4):
        if j % 2 == 0:
            if lista[j] == "O" and lista[j + 2] == "O" and lista[j + 4] == 'O':
                return 'O'

    for g in range(0, 2):
        if lista[g] == "O" and lista[g + 3] == "O" and lista[g + 6] == "O":
            return 'O'