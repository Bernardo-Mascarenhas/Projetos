"""
3. CONVERSOR DE MOEDAS

Descrição: Crie um conversor de moedas que converta valores entre diferentes moedas, 
(por exemplo, de Reais para Dólares e vice-versa). 
Você pode usar taxas de câmbio fixas ou permitir que o usuário insira as taxas.

Objetivos: de Aprendizado: Entrada e saída de dados, operações matemáticas básicas, e manipulação de strings.
"""

taxa_de_câmbio =  5.64

print("Conversor de Moeda")
print("Digite '1' para converter BRL para USD")
print("Digite '2' para converter USD para BRL")

selecao_de_conversao = input("\nQual conversão você quer fazer? 1/2: ").lower()
confirmacao = ['1','2']
try:
    valor = input("Selecione o valor: ")
    valor = float(valor)
except ValueError:
    print("Insíra um valor válido !")


conversão_dolar = (valor / taxa_de_câmbio)
conversão_real = (valor * taxa_de_câmbio) 


if selecao_de_conversao in confirmacao:
    if selecao_de_conversao == '1':
        print(f"\nO resultado da conversão é {round(conversão_dolar,2)} Dólares")
    elif selecao_de_conversao == '2':
        print(f"\nO resultao da conversão é {round(conversão_real,2)} Reais")