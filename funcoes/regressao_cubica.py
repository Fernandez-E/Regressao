from funcoes.dados import dados_arquivo
import numpy as np

def reg_cubica(arquivo):
    variaveis, dados = dados_arquivo(arquivo)
    melhor_r2, melhor_mae, melhor_rmse, melhor_mse, melhor_r2a = 0, 0, 0, 0, 0
    melhores_indices = ''
    c=1
    
    for i in range(1, len(variaveis)):
        Y = dados[0]   
        X = dados[i]
        n = len(X)
        
        x2 = [x**2 for x in X]
        x3 = [x**3 for x in X]
        x4 = [x**4 for x in X]
        x5 = [x**5 for x in X]
        x6 = [x**6 for x in X]
        xy = [x*y for x, y in zip(X, Y)]
        x2y = [(x**2)*y for x, y in zip(X, Y)]
        x3y = [(x**3)*y for x, y in zip(X, Y)]
        
        matrizA = np.array([
                        [sum(x6), sum(x5), sum(x4), sum(x3)],
                        [sum(x5), sum(x4), sum(x3), sum(x2)],
                        [sum(x4), sum(x3), sum(x2), sum(X)],
                        [sum(x3), sum(x2), sum(X), n]
                        ])
        
        matrizB = np.array([sum(x3y), sum(x2y), sum(xy), sum(Y)])
        
        # print(matrizA)
        # print(matrizB)
        
        matrizA_inversa = np.linalg.inv(matrizA)
        
        # print(matrizA_inversa)
        
        coeficientes = np.dot(matrizA_inversa,matrizB)
        
        a0 = float(coeficientes[0])
        a1 = float(coeficientes[1])
        a2 = float(coeficientes[2])
        a3 = float(coeficientes[3])
        
        
        y_est = [(a0*x**3 + a1*x**2 + a2*x + a3) for x in X]
        y_med = sum(Y) / len(Y)

        # residuos
        residuos = [(y - y_mod) for y, y_mod in zip(Y, y_est)]
        
        mae = sum(abs(r) for r in residuos) / n
        mse = sum(r**2 for r in residuos) / n
        rmse = mse**0.5
        
        # print(y_est)
        
        VE = [(y-y_med)**2 for y in y_est]
        VT = [(y-y_med)**2 for y in Y]
        
        r2 = sum(VE)/sum(VT)
        
        p = 1
        r2_ajustado = 1 - (1 - r2) * (n - 1) / (n - p - 1)
        
        print(f'{c:>3}: {variaveis[i]:^7} | R2: {r2:.2f} | R2a: {r2_ajustado:^6.2f} | MAE: {mae:^6.2f} | MSE: {mse:^6.2f} | RMSE: {rmse:^6.2f} | T = {a0:.12f} x {variaveis[i]}^3 + {a1:.12f} x {variaveis[i]}^2 + {a2:.12f} x {variaveis[i]} + {a3:.12f}')
        c+=1
        # print(r2)
        
        if r2 > melhor_r2:
            melhor_r2 = r2
            melhor_indice = variaveis[i]
    return melhor_indice, melhor_r2
    