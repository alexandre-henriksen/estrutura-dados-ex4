import os

# ──────────────────────────────────────────────
# Configurações
# ──────────────────────────────────────────────

from config import CAMINHO_MOCHILA01
from config import CAMINHO_MOCHILA02
from config import CAMINHO_MOCHILA1000
from config import CAMINHO_MOCHILA2500
from config import CAMINHO_MOCHILA5000
from config import OUTPUT_DIR
from mochila import knapsack, recuperar_itens

# ──────────────────────────────────────────────
# Utilitários
# ──────────────────────────────────────────────
def preparar_dados(texto):
    
    dados = [tuple(map(int, linha.split())) for linha in texto.splitlines()]

    # capacidade (segundo elemento da primeira tupla)
    capacidade = dados[0][1]

    # itens (ignora a primeira linha)
    itens = dados[1:]

    # separação em vetores
    pesos = [p for p, v in itens]
    valores = [v for p, v in itens]
    
    return capacidade, pesos, valores


def carregar_instancias(caminho_arquivo):
    with open(caminho_arquivo, "r") as f:
        texto = f.read()  # lê tudo como uma string única

    return texto

def salvar_resultados_txt(resultados):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    caminho_saida = os.path.join(OUTPUT_DIR, "resultados.txt")

    with open(caminho_saida, "w", encoding="utf-8") as f:

        for problema, dados in resultados.items():

            # título do problema (usa a chave diretamente)
            f.write(f"Problema: {problema}\n")

            f.write("Instância - solução\n")

            for instancia, valor in dados.items():
                f.write(f"{instancia} - {valor}\n")

            f.write("\n")  # linha em branco entre blocos

# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────
def main():
    
    # 1. Produção de resultados para as instâncias
         
    instancias = [
        ("mochila01", CAMINHO_MOCHILA01),
        ("mochila02", CAMINHO_MOCHILA02),
        ("mochila1000", CAMINHO_MOCHILA1000),
        ("mochila2500", CAMINHO_MOCHILA2500),
        ("mochila5000", CAMINHO_MOCHILA5000),
    ]


    ## 1.1. Mochila Inteira
    resultados = {
        "Problema da Mochila Inteira": {}
    }
   
    for nome, caminho in instancias:
        
        texto = carregar_instancias(CAMINHO_MOCHILA01)

        capacidade, pesos, valores = preparar_dados(texto)

        valor_max, k = knapsack(pesos, valores, M)

        itens = recuperar_itens(k, pesos, M)

        print("Valor máximo:", )
        print("Itens escolhidos (índices):", itens)

        resultados["Problema da Mochila Inteira"][nome] = valor_max, itens
    
    print("\nResultados finais Mochila Inteira:")
    print(resultados)

    # 2. Salvar resultados 
    
    salvar_resultados_txt(resultados)  


if __name__ == "__main__":
    main()
knapsack, recuperar_itens