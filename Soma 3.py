"""
Programa soma

Descrição:
Este programa soma dois números dados pelo usuário e imprime
na tela o resultado com uma frase e explicativa.
Autor Neimar Tedesco dos Santos
Versão: 0.0.3
Data: 09/08/2022

Código com erro.
"""
# Entrada de dadaos

# Input é uma função que permite fazer a leitura do teclado do usuário
# durante a execução do programa

numero_1 = input("Entre a primeir parcela.")

#essa instrução diz ao computador quardar o número 3 em um
#endereço de memória e "apelidar" este endereço de número_2
numero_2 = input("Entre a primeir parcela.")

# Processamento de dados

soma = numero_1 + numero_2

# Saídda de dados

# f-string
print(f"O resultado da soma do {numero_1} com o {numero_2} é igual a {soma}.")
