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
