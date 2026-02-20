from funcoes.regressao_simples import reg_simples
from funcoes.regressao_quadratica import reg_quadratica
from funcoes.regressao_multipla import reg_mult_2f, reg_mult_3f, reg_mult_4f, reg_mult_5f, reg_mult_6f, reg_mult_7f
import sys
import os
import tkinter as tk
from tkinter import filedialog

regressoes = []

print('#' * 150)
print(f'{"Algoritmo para determinacao de equacoes de regressao":^150}')
print('#' * 150)
print('O algoritmo foi desenvolvido para determinação de equações de regressão simples, quadrática e múltipla com até 7 fatores')
print('Voce devera selecionar quais metodologias de regressao serao aplicadas aos seus dados a seguir')
print('Digite 1 para "SIM" e 0 para "NAO"')
print('#' * 150)
regressoes.append(int(input('Regressao simples: ')))
regressoes.append(int(input('Regressao quadratica: ')))
regressoes.append(int(input('Regressao multipla com 2 fatores: ')))
regressoes.append(int(input('Regressao multipla com 3 fatores: ')))
regressoes.append(int(input('Regressao multipla com 4 fatores: ')))
regressoes.append(int(input('Regressao multipla com 5 fatores: ')))
regressoes.append(int(input('Regressao multipla com 6 fatores: ')))
regressoes.append(int(input('Regressao multipla com 7 fatores: ')))


print('#' * 150)
print('Agora selecione o arquivo a ser executado.')
input('Tecle ENTER para selecionar o arquivo...')
root = tk.Tk()
root.withdraw()
root.update()
root.attributes('-topmost', True)
dados = filedialog.askopenfilename(
    title="Selecione um arquivo TXT",
    filetypes=(("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*"))
)
root.destroy()

log = open('output.log', 'w', encoding='utf-8')
sys.stdout = log

print('#' * 150)
print(f'{"Algoritmo para determinação de equaçoes de regressao":^150}')
print('#' * 150)
print(f'Arquivo executado: {os.path.basename(dados)}')
print(f'Modelos de regressao executados:')
if regressoes[0] == 1:
    print(f'\tSimples')
if regressoes[1] == 1:
    print(f'\tQuadratica')
if regressoes[2] == 1:
    print(f'\tMultipla com 2 fatores')
if regressoes[3] == 1:
    print(f'\tMultipla com 3 fatores')
if regressoes[4] == 1:
    print(f'\tMultipla com 4 fatores')
if regressoes[5] == 1:
    print(f'\tMultipla com 5 fatores')
if regressoes[6] == 1:
    print(f'\tMultipla com 6 fatores')
if regressoes[7] == 1:
    print(f'\tMultipla com 7 fatores')  

if regressoes[0] == 1:
    print('\n')
    print('#' * 150)
    print('REGRESSAO SIMPLES')
    print('#' * 150)
    indice, r2 = reg_simples(dados)
    print('#' * 150)
    print(f'Para a regressao simples, o melhor indice foi o {indice:^7} [R2={r2:.6f}]')
    print('#' * 150)
    print('\n')

if regressoes[1] == 1:
    print('#' * 150)
    print('REGRESSAO QUADRATICA')
    print('#' * 150)
    indice, r2 = reg_quadratica(dados)
    print('#' * 150)
    print(f'Para a regressao quadratica, o melhor indice foi o {indice:^7} [R2={r2:.6f}]')
    print('#' * 150)
    print('\n')

if regressoes[2] == 1:
    print('#' * 150)
    print('REGRESSÃO MULTIPLA 2 FATORES')
    print('#' * 150)
    indice, r2 = reg_mult_2f(dados)
    print('#' * 150)
    print(f'Para a regressao multipla com 2 fatores, os melhores indices foram {indice[0]:^7} + {indice[1]:^7} [R2={r2:.6f}]')
    print('#' * 150)
    print('\n')

if regressoes[3] == 1:
    print('#' * 150)
    print('REGRESSÃO MULTIPLA 3 FATORES')
    print('#' * 150)
    indice, r2 = reg_mult_3f(dados)
    print('#' * 150)
    print(f'Para a regressao multipla com 3 fatores, os melhores indices foram {indice[0]:^7} + {indice[1]:^7} + {indice[2]:^7} [R2={r2:.6f}]')
    print('#' * 150)
    print('\n')

if regressoes[4] == 1:
    print('#' * 150)
    print('REGRESSÃO MULTIPLA 4 FATORES')
    print('#' * 150)
    indice, r2 = reg_mult_4f(dados)
    print('#' * 150)
    print(f'Para a regressao multipla com 4 fatores, os melhores indices foram {indice[0]:^7} + {indice[1]:^7} + {indice[2]:^7} + {indice[3]:^7} [R2={r2:.6f}]')
    print('#' * 150)
    print('\n')

if regressoes[5] == 1:
    print('#' * 150)
    print('REGRESSÃO MULTIPLA 5 FATORES')
    print('#' * 150)
    indice, r2 = reg_mult_5f(dados)
    print('#' * 150)
    print(f'Para a regressao multipla com 5 fatores, os melhores indices foram {indice[0]:^7} + {indice[1]:^7} + {indice[2]:^7} + {indice[3]:^7} + {indice[4]:^7} [R2={r2:.6f}]')
    print('#' * 150)
    print('\n')

if regressoes[6] == 1:
    print('#' * 150)
    print('REGRESSÃO MULTIPLA 6 FATORES')
    print('#' * 150)
    indice, r2 = reg_mult_6f(dados)
    print('#' * 150)
    print(f'Para a regressao multipla com 6 fatores, os melhores indices foram {indice[0]:^7} + {indice[1]:^7} + {indice[2]:^7} + {indice[3]:^7} + {indice[4]:^7} + {indice[5]:^7} [R2={r2:.6f}]')
    print('#' * 150)
    print('\n')

if regressoes[7] == 1:
    print('#' * 150)
    print('REGRESSÃO MULTIPLA 7 FATORES')
    print('#' * 150)
    indice, r2 = reg_mult_7f(dados)
    print('#' * 150)
    print(f'Para a regressao multipla com 7 fatores, os melhores indices foram {indice[0]:^7} + {indice[1]:^7} + {indice[2]:^7} + {indice[3]:^7} + {indice[4]:^7} + {indice[5]:^7} + {indice[6]:^7} [R2={r2:.6f}]')
    print('#' * 150)
    print('\n')

sys.stdout = sys.__stdout__
log.close()

print('Algoritmo executado. Abrindo arquivo.')
os.startfile('output.log')
