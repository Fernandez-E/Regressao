# Algoritmo para determinação de equações de regressão
## Métodos de regressão disponíveis:
1. Regressão simples
2. Regressão quadrática
3. Regressão múltipla com 2 fatores
4. Regressão múltipla com 3 fatores
5. Regressão múltipla com 4 fatores
6. Regressão múltipla com 5 fatores
7. Regressão múltipla com 6 fatores
8. Regressão múltipla com 7 fatores

## Como utilizar:
- O algoritmo realiza a leitura de arquivo em formato .txt separado por tabulação horizontal entre elementos na linha ("\t") e quebra de linhas entre linhas ("\n")
  - Esse formato é obtido copiando dados de uma planilha excel e colando em um bloco de notas, por exemplo</br>
- A primeira linha deverá conter o rótulo das variáveis</br>
- A primeira coluna deve ser a variável dependente</br>
- As demais colunas serão para variáveis independentes</br>

### Exemplo de formatação:
```
Y  x1  x2
1.0  1.2  1.5
1.5  1.5  1.8
2.1  1.9  2.4
```
É solocitado do usuário quais as metodologias de regressão devem ser executadas</br>
Ao final da execução, é gerado o log com os resultado na mesma pasta em que está o arquivo do algoritmo com o nome "output.log".

### Exemplo de saída:

```
######################################################################################################################################################
REGRESSAO SIMPLES
######################################################################################################################################################
  1:  NDVI   | R2: 0.00 | T = 0.7875 x NDVI + 35.7103
  2:  GNDVI  | R2: 0.03 | T = 4.8760 x GNDVI + 33.4899
  3:  NDRE   | R2: 0.15 | T = 15.2410 x NDRE + 33.9075
  4:   EVI   | R2: 0.10 | T = 0.5704 x EVI + 34.4116
  5:  OSAVI  | R2: 0.00 | T = 0.7873 x OSAVI + 35.7105
  6: NDVI705 | R2: 0.02 | T = -3.7837 x NDVI705 + 38.3136
  7:   GCI   | R2: 0.02 | T = 0.3512 x GCI + 35.2789
  8:    R    | R2: 0.00 | T = -0.0000 x R + 36.3064
  9:   NIR   | R2: 0.00 | T = -0.0000 x NIR + 36.3346
 10:   RE    | R2: 0.03 | T = -0.0001 x RE + 38.1205
 11:    G    | R2: 0.01 | T = -0.0002 x G + 37.1364
 12:    B    | R2: 0.01 | T = 0.0002 x B + 35.3124
######################################################################################################################################################
Para a regressao simples, o melhor indice foi o  NDRE   [R2=0.146838]
######################################################################################################################################################
```
