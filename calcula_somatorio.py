"""CÓDIGO PARA CALCULAR SOMATÓRIO"""
#Inserção de valores e atribuição de variaveis 
n = int(input())
soma = 0
#Estrutura de repetição para calcular o somatório
for i in range(2, n + 1):
    soma += i / (i * (i - 1))
#Saída do resultado
print(f"{soma:.2f}")