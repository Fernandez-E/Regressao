from funcoes.dados import dados_arquivo
import numpy as np

def reg_simples(arquivo):
    variaveis, dados = dados_arquivo(arquivo)
    melhor_r2 = 0
    melhor_indice = ''
    c=1
    
    for i in range(1, len(variaveis)):
        Y = dados[0]   
        X = dados[i]
        n = len(X)
        
        x2 = [x**2 for x in X]
        xy = [x*y for x, y in zip(X, Y)]
        
        matrizA = np.array([
                            [n, sum(X)], 
                        [sum(X), sum(x2)]
                        ])
        
        matrizB = np.array([sum(Y), sum(xy)])
        
        # print(matrizA)
        # print(matrizB)
        
        matrizA_inversa = np.linalg.inv(matrizA)
        
        # print(matrizA_inversa)
        
        coeficientes = np.dot(matrizA_inversa,matrizB)
        
        b = float(coeficientes[0])
        a = float(coeficientes[1])
        
        # print(a)
        # print(b)
        
        y_est = [a*x+b for x in X]
        y_med = sum(Y) / len(Y)
        
        # print(y_est)
        
        VE = [(y-y_med)**2 for y in y_est]
        VT = [(y-y_med)**2 for y in Y]
        
        r2 = sum(VE)/sum(VT)
        print(f'{c:>3}: {variaveis[i]:^7} | R2: {r2:.2f} | T = {a:.8f} x {variaveis[i]} + {b:.8f}')
        c+=1
        if r2 > melhor_r2:
            melhor_r2 = r2
            melhor_indice = variaveis[i]
    return melhor_indice, melhor_r2
    