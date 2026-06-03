def knapsack(pesos, valores, M):
    '''
    Args
    pesos: lista de pesos
    valores: lista de valores
    M: capacidade da mochila

    Returns
    k[n][M]: valor máximo que pode ser colocado na mochila
    k = matriz resultante do algoritmo de programação dinâmica
    '''   
    n = len(pesos)

    # Criar matriz k com (n+1) linhas e (M+1) colunas (preenchida com zeros)
    # k[i][m] = valor máximo usando os i primeiros itens e capacidade m
    # É a tabela de memória onde o algoritmo irá armazenar os resultados intermediários
    k = [[0 for m in range(M + 1)] for i in range(n + 1)]

    # Loop sobre os itens
    for i in range(0, n + 1):

        # Loop sobre a capacidade da mochila
        for m in range(0, M + 1):

            # Caso base: sem itens ou capacidade zero
            if i == 0 or m == 0:
                k[i][m] = 0

            # Se o item cabe na mochila
            elif pesos[i - 1] <= m:

                valor_incluindo = valores[i - 1] + k[i - 1][m - pesos[i - 1]]
                valor_excluindo = k[i - 1][m]

                k[i][m] = max(valor_incluindo, valor_excluindo)

            # Se o item NÃO cabe
            else:
                k[i][m] = k[i - 1][m]

    return k[n][M], k


def recuperar_itens(k, pesos, M):
    """
    Recupera os índices dos itens selecionados na mochila

    k      -> matriz resultante do algoritmo de programação dinâmica
    pesos  -> lista de pesos
    M      -> capacidade da mochila

    return -> lista com índices dos itens escolhidos
    """

    n = len(pesos)
    itens_escolhidos = []

    i = n
    m = M

    # Percorre a matriz de trás para frente
    while i > 0 and m > 0:

        # Se o valor mudou, significa que o item foi incluído
        if k[i][m] != k[i - 1][m]:
            itens_escolhidos.append(i - 1)  # índice do item
            m -= pesos[i - 1]               # reduz a capacidade

        # Vai para o item anterior
        i -= 1
        
    # Na instância de entrada, os itens possuem índices de 1 a n, já que a primeira linha contém o valor de n e M
    # Vamos acrescentar 1 para que os índices dos itens comecem em 1
    
    itens_escolhidos = [i + 1 for i in itens_escolhidos]

    # inverter para ordem original
    return itens_escolhidos[::-1]