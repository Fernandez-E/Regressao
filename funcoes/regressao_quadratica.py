from funcoes.dados import dados_arquivo
import numpy as np

def reg_quadratica(arquivo):
    variaveis, dados = dados_arquivo(arquivo)
    melhor_r2 = 0
    melhor_indice = ''
    c=1
    
    for i in range(1, len(variaveis)):
        Y = dados[0]   
        X = dados[i]
        n = len(X)
        
        x2 = [x**2 for x in X]
        x3 = [x**3 for x in X]
        x4 = [x**4 for x in X]
        xy = [x*y for x, y in zip(X, Y)]
        x2y = [(x**2)*y for x, y in zip(X, Y)]
        
        matrizA = np.array([
                        [n, sum(X), sum(x2)], 
                        [sum(X), sum(x2), sum(x3)],
                        [sum(x2), sum(x3), sum(x4)]
                        ])
        
        matrizB = np.array([sum(Y), sum(xy), sum(x2y)])
        
        # print(matrizA)
        # print(matrizB)
        
        matrizA_inversa = np.linalg.inv(matrizA)
        
        # print(matrizA_inversa)
        
        coeficientes = np.dot(matrizA_inversa,matrizB)
        
        a0 = float(coeficientes[0])
        a1 = float(coeficientes[1])
        a2 = float(coeficientes[2])
        
        
        y_est = [(a0 + x*a1 + x**2*a2) for x in X]
        y_med = sum(Y) / len(Y)
        
        # print(y_est)
        
        VE = [(y-y_med)**2 for y in y_est]
        VT = [(y-y_med)**2 for y in Y]
        
        r2 = sum(VE)/sum(VT)
        
        print(f'{c:>3}: {variaveis[i]:^7} | R2: {r2:.2f} | T = {a0:.4f} + {a1:.4f} x {variaveis[i]} + {a2:.4f} x {variaveis[i]}^2')
        c+=1
        # print(r2)
        
        if r2 > melhor_r2:
            melhor_r2 = r2
            melhor_indice = variaveis[i]
    return melhor_indice, melhor_r2
    