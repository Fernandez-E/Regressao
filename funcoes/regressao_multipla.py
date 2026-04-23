from funcoes.dados import dados_arquivo
import numpy as np

def reg_mult_2f(arquivo):
    variaveis, dados = dados_arquivo(arquivo)
    melhor_r2, melhor_mae, melhor_rmse, melhor_mse, melhor_r2a = 0, 0, 0, 0, 0
    melhores_indices = ''
    c=1
    
    for i in range(1, len(variaveis)-1):
        for j in range(i+1, len(variaveis)):
            Y = dados[0]   
            X1 = dados[i]
            X2 = dados[j]
            n = len(X1)
            
            x12 = [x**2 for x in X1]
            x22 = [x**2 for x in X2]
            x1x2 = [x1*x2 for x1, x2 in zip(X1,X2)]
            x1y = [x1*y for x1, y in zip(X1, Y)]
            x2y = [x2*y for x2, y in zip(X2, Y)]
            
            matrizA = np.array([
                        [n, sum(X1), sum(X2)], 
                        [sum(X1), sum(x12), sum(x1x2)],
                        [sum(X2), sum(x1x2), sum(x22)]
                        ])
        
            matrizB = np.array([sum(Y), sum(x1y), sum(x2y)])
        
            matrizA_inversa = np.linalg.inv(matrizA)
            
            coeficientes = np.dot(matrizA_inversa,matrizB)
        
            a0 = float(coeficientes[0])
            a1 = float(coeficientes[1])
            a2 = float(coeficientes[2])
        
            y_est = [(a0 + x1*a1 + x2*a2) for x1,x2 in zip(X1,X2)]
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
            
            # R2 ajustado
            p = 2
            r2_ajustado = 1 - (1 - r2) * (n - 1) / (n - p - 1)
        
            print(
                f'{c:>3}: {variaveis[i]:^7} + {variaveis[j]:^7} | '
                  f'R2: {r2:^6.2f} | R2a: {r2_ajustado:^6.2f} | MAE: {mae:^6.2f} | MSE: {mse:^6.2f} | RMSE: {rmse:^6.2f} |'
                  f'T = {a0:.4f} + {a1:.8f} x {variaveis[i]} + {a2:.8f} x {variaveis[j]}'
                )
            c+=1
            # print(r2)
        
            if r2 > melhor_r2:
                melhor_r2 = r2
                melhores_indices = [variaveis[i], variaveis[j]]
    return melhores_indices, melhor_r2
       
def reg_mult_3f(arquivo):
    variaveis, dados = dados_arquivo(arquivo)
    melhor_r2 = 0
    melhores_indices = ''
    c=1
    
    for i in range(1, len(variaveis)-2):
        for j in range(i+1, len(variaveis)-1):
            for k in range(j+1, len(variaveis)):
                Y = dados[0]
                X1 = dados[i]
                X2 = dados[j]
                X3 = dados[k]
                n = len(X1)
                
                x12 = [x**2 for x in X1]
                x22 = [x**2 for x in X2]
                x32 = [x**2 for x in X3]
                x1x2 = [x1*x2 for x1, x2 in zip(X1,X2)]
                x1x3 = [x1*x3 for x1, x3 in zip(X1,X3)]
                x2x3 = [x2*x3 for x2, x3 in zip(X2,X3)]
                x1y = [x1*y for x1, y in zip(X1, Y)]
                x2y = [x2*y for x2, y in zip(X2, Y)]
                x3y = [x3*y for x3, y in zip(X3, Y)]
                
                matrizA = np.array([
                        [n, sum(X1), sum(X2), sum(X3)], 
                        [sum(X1), sum(x12), sum(x1x2), sum(x1x3)],
                        [sum(X2), sum(x1x2), sum(x22), sum(x2x3)],
                        [sum(X3), sum(x1x3), sum(x2x3), sum(x32)]
                        ])
        
                matrizB = np.array([sum(Y), sum(x1y), sum(x2y), sum(x3y)])
        
                matrizA_inversa = np.linalg.inv(matrizA)
            
                coeficientes = np.dot(matrizA_inversa,matrizB)
        
                a0 = float(coeficientes[0])
                a1 = float(coeficientes[1])
                a2 = float(coeficientes[2])
                a3 = float(coeficientes[3])
        
                y_est = [(a0 + x1*a1 + x2*a2 + x3*a3) for x1, x2, x3 in zip(X1,X2,X3)]
                y_med = sum(Y) / len(Y)
        
                # print(y_est)
        
                VE = [(y-y_med)**2 for y in y_est]
                VT = [(y-y_med)**2 for y in Y]
        
                r2 = sum(VE)/sum(VT)
        
                print(f'{c:>3}: {variaveis[i]:^7} + {variaveis[j]:^7} + {variaveis[k]:^7} | R2: {r2:.2f} | T = {a0:.8f} + {a1:.8f} x {variaveis[i]} + {a2:.8f} x {variaveis[j]} + {a3:.8f} x {variaveis[k]}')
                c+=1
                # print(r2)
        
                if r2 > melhor_r2:
                    melhor_r2 = r2
                    melhores_indices = [variaveis[i], variaveis[j], variaveis[k]]
    return melhores_indices, melhor_r2

def reg_mult_4f(arquivo):
    variaveis, dados = dados_arquivo(arquivo)
    melhor_r2 = 0
    melhores_indices = ''
    c=1
    
    for i in range(1, len(variaveis)-3):
        for j in range(i+1, len(variaveis)-2):
            for k in range(j+1, len(variaveis)-1):
                for l in range(k+1, len(variaveis)):
                    Y = dados[0]
                    X1 = dados[i]
                    X2 = dados[j]
                    X3 = dados[k]
                    X4 = dados[l]
                    n = len(X1)
                    
                    x12 = [x**2 for x in X1]
                    x22 = [x**2 for x in X2]
                    x32 = [x**2 for x in X3]
                    x42 = [x**2 for x in X4]
                    x1x2 = [x1*x2 for x1, x2 in zip(X1,X2)]
                    x1x3 = [x1*x3 for x1, x3 in zip(X1,X3)]
                    x1x4 = [x1*x4 for x1, x4 in zip(X1,X4)]
                    x2x3 = [x2*x3 for x2, x3 in zip(X2,X3)]
                    x2x4 = [x2*x4 for x2, x4 in zip(X2,X4)]
                    x3x4 = [x3*x4 for x3, x4 in zip(X3,X4)]
                    x1y = [x1*y for x1, y in zip(X1, Y)]
                    x2y = [x2*y for x2, y in zip(X2, Y)]
                    x3y = [x3*y for x3, y in zip(X3, Y)]
                    x4y = [x4*y for x4, y in zip(X4, Y)]
                    
                    matrizA = np.array([
                            [n, sum(X1), sum(X2), sum(X3), sum(X4)], 
                            [sum(X1), sum(x12), sum(x1x2), sum(x1x3), sum(x1x4)],
                            [sum(X2), sum(x1x2), sum(x22), sum(x2x3), sum(x2x4)],
                            [sum(X3), sum(x1x3), sum(x2x3), sum(x32), sum(x3x4)],
                            [sum(X4), sum(x1x4), sum(x2x4), sum(x3x4), sum(x42)]
                            ])
            
                    matrizB = np.array([sum(Y), sum(x1y), sum(x2y), sum(x3y), sum(x4y)])
            
                    matrizA_inversa = np.linalg.inv(matrizA)
                
                    coeficientes = np.dot(matrizA_inversa,matrizB)
            
                    a0 = float(coeficientes[0])
                    a1 = float(coeficientes[1])
                    a2 = float(coeficientes[2])
                    a3 = float(coeficientes[3])
                    a4 = float(coeficientes[4])
            
                    y_est = [(a0 + x1*a1 + x2*a2 + x3*a3 + x4*a4) for x1, x2, x3, x4 in zip(X1,X2,X3,X4)]
                    y_med = sum(Y) / len(Y)
            
                    # print(y_est)
            
                    VE = [(y-y_med)**2 for y in y_est]
                    VT = [(y-y_med)**2 for y in Y]
            
                    r2 = sum(VE)/sum(VT)
            
                    print(f'{c:>3}: {variaveis[i]:^7} + {variaveis[j]:^7} + {variaveis[k]:^7} + {variaveis[l]:^7} | R2: {r2:.2f} | T = {a0:.8f} + {a1:.8f} x {variaveis[i]} + {a2:.8f} x {variaveis[j]} + {a3:.8f} x {variaveis[k]} + {a4:.8f} x {variaveis[l]}')
                    c+=1
                    # print(r2)
            
                    if r2 > melhor_r2:
                        melhor_r2 = r2
                        melhores_indices = [variaveis[i], variaveis[j], variaveis[k], variaveis[l]]
    return melhores_indices, melhor_r2

def reg_mult_5f(arquivo):
    variaveis, dados = dados_arquivo(arquivo)
    melhor_r2 = 0
    melhores_indices = ''
    c=1
    
    for i in range(1, len(variaveis)-4):
        for j in range(i+1, len(variaveis)-3):
            for k in range(j+1, len(variaveis)-2):
                for l in range(k+1, len(variaveis)-1):
                    for m in range(l+1, len(variaveis)):
                        Y = dados[0]
                        X1 = dados[i]
                        X2 = dados[j]
                        X3 = dados[k]
                        X4 = dados[l]
                        X5 = dados[m]
                        n = len(X1)
                        
                        x12 = [x**2 for x in X1]
                        x22 = [x**2 for x in X2]
                        x32 = [x**2 for x in X3]
                        x42 = [x**2 for x in X4]
                        x52 = [x**2 for x in X5]
                        x1x2 = [x1*x2 for x1, x2 in zip(X1,X2)]
                        x1x3 = [x1*x3 for x1, x3 in zip(X1,X3)]
                        x1x4 = [x1*x4 for x1, x4 in zip(X1,X4)]
                        x1x5 = [x1*x5 for x1, x5 in zip(X1,X5)]
                        x2x3 = [x2*x3 for x2, x3 in zip(X2,X3)]
                        x2x4 = [x2*x4 for x2, x4 in zip(X2,X4)]
                        x2x5 = [x2*x5 for x2, x5 in zip(X2,X5)]
                        x3x4 = [x3*x4 for x3, x4 in zip(X3,X4)]
                        x3x5 = [x3*x5 for x3, x5 in zip(X3,X5)]
                        x4x5 = [x4*x5 for x4, x5 in zip(X4,X5)]
                        x1y = [x1*y for x1, y in zip(X1, Y)]
                        x2y = [x2*y for x2, y in zip(X2, Y)]
                        x3y = [x3*y for x3, y in zip(X3, Y)]
                        x4y = [x4*y for x4, y in zip(X4, Y)]
                        x5y = [x5*y for x5, y in zip(X5, Y)]
                        
                        matrizA = np.array([
                                [n, sum(X1), sum(X2), sum(X3), sum(X4), sum(X5)], 
                                [sum(X1), sum(x12), sum(x1x2), sum(x1x3), sum(x1x4), sum(x1x5)],
                                [sum(X2), sum(x1x2), sum(x22), sum(x2x3), sum(x2x4), sum(x2x5)],
                                [sum(X3), sum(x1x3), sum(x2x3), sum(x32), sum(x3x4), sum(x3x5)],
                                [sum(X4), sum(x1x4), sum(x2x4), sum(x3x4), sum(x42), sum(x4x5)],
                                [sum(X5), sum(x1x5), sum(x2x5), sum(x3x5), sum(x4x5), sum(x52)]
                                ])
                
                        matrizB = np.array([sum(Y), sum(x1y), sum(x2y), sum(x3y), sum(x4y), sum(x5y)])
                
                        matrizA_inversa = np.linalg.inv(matrizA)
                    
                        coeficientes = np.dot(matrizA_inversa,matrizB)
                
                        a0 = float(coeficientes[0])
                        a1 = float(coeficientes[1])
                        a2 = float(coeficientes[2])
                        a3 = float(coeficientes[3])
                        a4 = float(coeficientes[4])
                        a5 = float(coeficientes[5])
                
                        y_est = [(a0 + x1*a1 + x2*a2 + x3*a3 + x4*a4 + x5*a5) for x1, x2, x3, x4, x5 in zip(X1,X2,X3,X4,X5)]
                        y_med = sum(Y) / len(Y)
                
                        # print(y_est)
                
                        VE = [(y-y_med)**2 for y in y_est]
                        VT = [(y-y_med)**2 for y in Y]
                
                        r2 = sum(VE)/sum(VT)
                
                        print(f'{c:>3}: {variaveis[i]:^7} + {variaveis[j]:^7} + {variaveis[k]:^7} + {variaveis[l]:^7} + {variaveis[m]:^7} | R2: {r2:.2f} | T = {a0:.8f} + {a1:.8f} x {variaveis[i]} + {a2:.8f} x {variaveis[j]} + {a3:.8f} x {variaveis[k]} + {a4:.8f} x {variaveis[l]} + {a5:.8f} x {variaveis[m]}')
                        c+=1
                        # print(r2)
                
                        if r2 > melhor_r2:
                            melhor_r2 = r2
                            melhores_indices = [variaveis[i], variaveis[j], variaveis[k], variaveis[l], variaveis[m]]
    return melhores_indices, melhor_r2

def reg_mult_6f(arquivo):
    variaveis, dados = dados_arquivo(arquivo)
    melhor_r2 = 0
    melhores_indices = ''
    c = 1
    
    for i in range(1, len(variaveis)-5):
        for j in range(i+1, len(variaveis)-4):
            for k in range(j+1, len(variaveis)-3):
                for l in range(k+1, len(variaveis)-2):
                    for m in range(l+1, len(variaveis)-1):
                        for p in range(m+1, len(variaveis)):
                            Y = dados[0]
                            X1 = dados[i]
                            X2 = dados[j]
                            X3 = dados[k]
                            X4 = dados[l]
                            X5 = dados[m]
                            X6 = dados[p]
                            n = len(X1)
                            
                            x12 = [x**2 for x in X1]
                            x22 = [x**2 for x in X2]
                            x32 = [x**2 for x in X3]
                            x42 = [x**2 for x in X4]
                            x52 = [x**2 for x in X5]
                            x62 = [x**2 for x in X6]
                            x1x2 = [x1*x2 for x1, x2 in zip(X1,X2)]
                            x1x3 = [x1*x3 for x1, x3 in zip(X1,X3)]
                            x1x4 = [x1*x4 for x1, x4 in zip(X1,X4)]
                            x1x5 = [x1*x5 for x1, x5 in zip(X1,X5)]
                            x1x6 = [x1*x6 for x1, x6 in zip(X1,X6)]
                            x2x3 = [x2*x3 for x2, x3 in zip(X2,X3)]
                            x2x4 = [x2*x4 for x2, x4 in zip(X2,X4)]
                            x2x5 = [x2*x5 for x2, x5 in zip(X2,X5)]
                            x2x6 = [x2*x6 for x2, x6 in zip(X2,X6)]
                            x3x4 = [x3*x4 for x3, x4 in zip(X3,X4)]
                            x3x5 = [x3*x5 for x3, x5 in zip(X3,X5)]
                            x3x6 = [x3*x6 for x3, x6 in zip(X3,X6)]
                            x4x5 = [x4*x5 for x4, x5 in zip(X4,X5)]
                            x4x6 = [x4*x6 for x4, x6 in zip(X4,X6)]
                            x5x6 = [x5*x6 for x5, x6 in zip(X5,X6)]
                            x1y = [x1*y for x1, y in zip(X1, Y)]
                            x2y = [x2*y for x2, y in zip(X2, Y)]
                            x3y = [x3*y for x3, y in zip(X3, Y)]
                            x4y = [x4*y for x4, y in zip(X4, Y)]
                            x5y = [x5*y for x5, y in zip(X5, Y)]
                            x6y = [x6*y for x6, y in zip(X6, Y)]
                            
                            matrizA = np.array([
                                    [n, sum(X1), sum(X2), sum(X3), sum(X4), sum(X5), sum(X6)], 
                                    [sum(X1), sum(x12), sum(x1x2), sum(x1x3), sum(x1x4), sum(x1x5), sum(x1x6)],
                                    [sum(X2), sum(x1x2), sum(x22), sum(x2x3), sum(x2x4), sum(x2x5), sum(x2x6)],
                                    [sum(X3), sum(x1x3), sum(x2x3), sum(x32), sum(x3x4), sum(x3x5), sum(x3x6)],
                                    [sum(X4), sum(x1x4), sum(x2x4), sum(x3x4), sum(x42), sum(x4x5), sum(x4x6)],
                                    [sum(X5), sum(x1x5), sum(x2x5), sum(x3x5), sum(x4x5), sum(x52), sum(x5x6)],
                                    [sum(X6), sum(x1x6), sum(x2x6), sum(x3x6), sum(x4x6), sum(x5x6), sum(x62)]
                                    ])
                    
                            matrizB = np.array([sum(Y), sum(x1y), sum(x2y), sum(x3y), sum(x4y), sum(x5y), sum(x6y)])
                    
                            matrizA_inversa = np.linalg.inv(matrizA)
                        
                            coeficientes = np.dot(matrizA_inversa,matrizB)
                    
                            a0 = float(coeficientes[0])
                            a1 = float(coeficientes[1])
                            a2 = float(coeficientes[2])
                            a3 = float(coeficientes[3])
                            a4 = float(coeficientes[4])
                            a5 = float(coeficientes[5])
                            a6 = float(coeficientes[6])
                    
                            y_est = [(a0 + x1*a1 + x2*a2 + x3*a3 + x4*a4 + x5*a5 + x6*a6) for x1, x2, x3, x4, x5, x6 in zip(X1,X2,X3,X4,X5,X6)]
                            y_med = sum(Y) / len(Y)
                    
                            # print(y_est)
                    
                            VE = [(y-y_med)**2 for y in y_est]
                            VT = [(y-y_med)**2 for y in Y]
                    
                            r2 = sum(VE)/sum(VT)
                    
                            print(f'{c:>3}: {variaveis[i]:^7} + {variaveis[j]:^7} + {variaveis[k]:^7} + {variaveis[l]:^7} + {variaveis[m]:^7} + {variaveis[p]:^7} | R2: {r2:.2f} | T = {a0:.8f} + {a1:.8f} x {variaveis[i]} + {a2:.8f} x {variaveis[j]} + {a3:.8f} x {variaveis[k]} + {a4:.8f} x {variaveis[l]} + {a5:.8f} x {variaveis[m]} + {a6:.8f} x {variaveis[p]}')
                            c+=1
                            # print(r2)
                    
                            if r2 > melhor_r2:
                                melhor_r2 = r2
                                melhores_indices = [variaveis[i], variaveis[j], variaveis[k], variaveis[l], variaveis[m], variaveis[p]]
    return melhores_indices, melhor_r2

def reg_mult_7f(arquivo):
    variaveis, dados = dados_arquivo(arquivo)
    melhor_r2 = 0
    melhores_indices = ''
    c = 1
    
    for i in range(1, len(variaveis)-6):
        for j in range(i+1, len(variaveis)-5):
            for k in range(j+1, len(variaveis)-4):
                for l in range(k+1, len(variaveis)-3):
                    for m in range(l+1, len(variaveis)-2):
                        for p in range(m+1, len(variaveis)-1):
                            for q in range(p+1, len(variaveis)):
                                Y = dados[0]
                                X1 = dados[i]
                                X2 = dados[j]
                                X3 = dados[k]
                                X4 = dados[l]
                                X5 = dados[m]
                                X6 = dados[p]
                                X7 = dados[q]
                                n = len(X1)
                                
                                x12 = [x**2 for x in X1]
                                x22 = [x**2 for x in X2]
                                x32 = [x**2 for x in X3]
                                x42 = [x**2 for x in X4]
                                x52 = [x**2 for x in X5]
                                x62 = [x**2 for x in X6]
                                x72 = [x**2 for x in X7]
                                x1x2 = [x1*x2 for x1, x2 in zip(X1,X2)]
                                x1x3 = [x1*x3 for x1, x3 in zip(X1,X3)]
                                x1x4 = [x1*x4 for x1, x4 in zip(X1,X4)]
                                x1x5 = [x1*x5 for x1, x5 in zip(X1,X5)]
                                x1x6 = [x1*x6 for x1, x6 in zip(X1,X6)]
                                x1x7 = [x1*x7 for x1, x7 in zip(X1,X7)]
                                x2x3 = [x2*x3 for x2, x3 in zip(X2,X3)]
                                x2x4 = [x2*x4 for x2, x4 in zip(X2,X4)]
                                x2x5 = [x2*x5 for x2, x5 in zip(X2,X5)]
                                x2x6 = [x2*x6 for x2, x6 in zip(X2,X6)]
                                x2x7 = [x2*x7 for x2, x7 in zip(X2,X7)]
                                x3x4 = [x3*x4 for x3, x4 in zip(X3,X4)]
                                x3x5 = [x3*x5 for x3, x5 in zip(X3,X5)]
                                x3x6 = [x3*x6 for x3, x6 in zip(X3,X6)]
                                x3x7 = [x3*x7 for x3, x7 in zip(X3,X7)]
                                x4x5 = [x4*x5 for x4, x5 in zip(X4,X5)]
                                x4x6 = [x4*x6 for x4, x6 in zip(X4,X6)]
                                x4x7 = [x4*x7 for x4, x7 in zip(X4,X7)]
                                x5x6 = [x5*x6 for x5, x6 in zip(X5,X6)]
                                x5x7 = [x5*x7 for x5, x7 in zip(X5,X7)]
                                x6x7 = [x6*x7 for x6, x7 in zip(X6,X7)]
                                x1y = [x1*y for x1, y in zip(X1, Y)]
                                x2y = [x2*y for x2, y in zip(X2, Y)]
                                x3y = [x3*y for x3, y in zip(X3, Y)]
                                x4y = [x4*y for x4, y in zip(X4, Y)]
                                x5y = [x5*y for x5, y in zip(X5, Y)]
                                x6y = [x6*y for x6, y in zip(X6, Y)]
                                x7y = [x7*y for x7, y in zip(X7, Y)]
                                
                                matrizA = np.array([
                                        [n, sum(X1), sum(X2), sum(X3), sum(X4), sum(X5), sum(X6), sum(X7)], 
                                        [sum(X1), sum(x12), sum(x1x2), sum(x1x3), sum(x1x4), sum(x1x5), sum(x1x6), sum(x1x7)],
                                        [sum(X2), sum(x1x2), sum(x22), sum(x2x3), sum(x2x4), sum(x2x5), sum(x2x6), sum(x2x7)],
                                        [sum(X3), sum(x1x3), sum(x2x3), sum(x32), sum(x3x4), sum(x3x5), sum(x3x6), sum(x3x7)],
                                        [sum(X4), sum(x1x4), sum(x2x4), sum(x3x4), sum(x42), sum(x4x5), sum(x4x6), sum(x4x7)],
                                        [sum(X5), sum(x1x5), sum(x2x5), sum(x3x5), sum(x4x5), sum(x52), sum(x5x6), sum(x5x7)],
                                        [sum(X6), sum(x1x6), sum(x2x6), sum(x3x6), sum(x4x6), sum(x5x6), sum(x62), sum(x6x7)],
                                        [sum(X7), sum(x1x7), sum(x2x7), sum(x3x7), sum(x4x7), sum(x5x7), sum(x6x7), sum(x72)]
                                        ])
                        
                                matrizB = np.array([sum(Y), sum(x1y), sum(x2y), sum(x3y), sum(x4y), sum(x5y), sum(x6y), sum(x7y)])
                        
                                matrizA_inversa = np.linalg.inv(matrizA)
                            
                                coeficientes = np.dot(matrizA_inversa,matrizB)
                        
                                a0 = float(coeficientes[0])
                                a1 = float(coeficientes[1])
                                a2 = float(coeficientes[2])
                                a3 = float(coeficientes[3])
                                a4 = float(coeficientes[4])
                                a5 = float(coeficientes[5])
                                a6 = float(coeficientes[6])
                                a7 = float(coeficientes[7])
                        
                                y_est = [(a0 + x1*a1 + x2*a2 + x3*a3 + x4*a4 + x5*a5 + x6*a6 + x7*a7) for x1, x2, x3, x4, x5, x6, x7 in zip(X1,X2,X3,X4,X5,X6,X7)]
                                y_med = sum(Y) / len(Y)
                        
                                # print(y_est)
                        
                                VE = [(y-y_med)**2 for y in y_est]
                                VT = [(y-y_med)**2 for y in Y]
                        
                                r2 = sum(VE)/sum(VT)
                        
                                print(f'{c:>3}: {variaveis[i]:^7} + {variaveis[j]:^7} + {variaveis[k]:^7} + {variaveis[l]:^7} + {variaveis[m]:^7} + {variaveis[p]:^7} + {variaveis[q]:^7} | R2: {r2:.2f} | T = {a0:.8f} + {a1:.8f} x {variaveis[i]} + {a2:.8f} x {variaveis[j]} + {a3:.8f} x {variaveis[k]} + {a4:.8f} x {variaveis[l]} + {a5:.8f} x {variaveis[m]} + {a6:.8f} x {variaveis[p]} + {a7:.8f} x {variaveis[q]}')
                                c+=1
                                # print(r2)
                        
                                if r2 > melhor_r2:
                                    melhor_r2 = r2
                                    melhores_indices = [variaveis[i], variaveis[j], variaveis[k], variaveis[l], variaveis[m], variaveis[p], variaveis[q]]
    return melhores_indices, melhor_r2