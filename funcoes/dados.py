def dados_arquivo(arquivo):
    with open(arquivo, "r") as f:
        linhas = f.readlines()
                
        variaveis = linhas[0].strip().split('\t')
        dados = [[] for _ in range(len(variaveis))]

        for linha in linhas[1:]:
            linha = linha.strip()
            if not linha:
                continue
            valores = linha.split("\t")

            for i in range(len(variaveis)):
                dados[i].append(float(valores[i]))

    return variaveis, tuple(dados)