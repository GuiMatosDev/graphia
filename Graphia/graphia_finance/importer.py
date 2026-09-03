import pandas as pd

#Funciona expecificamente para o extrato csv para pessoa física
def importar_csv_nubank(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo)

    #Colunas esperadas
    c_esperada = [
        "Data", 
        "Valor", 
        "Identificador",    
        "Descrição"
    ]

    #Checagem Colunas 
    for coluna in c_esperada: 
        if coluna not in df.columns:
            raise ValueError(
                f"Columa não encontrada: {coluna}"
            )

    #Armazenando todas as movimentações do extrato 
    movimentacoes = []

    for _, linha in df.iterrows():
        movimentacao = {
            "data": linha["Data"],
            "valor": linha["Valor"],
            "identificador": linha["Identificador"],
            "descricao": linha["Descrição"]
        }

        movimentacoes.append(movimentacao)

    return movimentacoes



    