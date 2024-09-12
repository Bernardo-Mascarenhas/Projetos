"""
3. CONVERSOR DE MOEDAS (:

Descrição: Crie um conversor de moedas que converta valores entre diferentes moedas, 
(por exemplo, de Reais para Dólares e vice-versa). 
Você pode usar taxas de câmbio fixas ou permitir que o usuário insira as taxas.

Objetivos: de Aprendizado: Entrada e saída de dados, operações matemáticas básicas, e manipulação de strings.
"""

taxa_de_câmbio =  5.64 # Salva a taxa de cãmbio atual no banco de dados

print("Conversor de Moeda") # Título do código
print("Digite '1' para converter BRL para USD") # Explicação 1
print("Digite '2' para converter USD para BRL") # Explicação 2

selecao_de_conversao = input("\nQual conversão você quer fazer? 1/2: ").lower() # Pergunta qual conversão o usuário quer fazer
confirmacao = ['1','2'] # Serve para fazer uma confimação interna do resultado
try:
    valor = input("Selecione o valor: ") # Pede para o usuário selecionar um valor
    valor = float(valor) # Tenta transformar o valor dígitado em um número decimal
except ValueError:
    print("Insíra um valor válido !") # Caso não seja possível transformar o valor dígitado em número decimal, mostre uma mensagem de erro


conversão_dolar = (valor / taxa_de_câmbio) # Faz a conversão para Dólar (com margem de erro)
conversão_real = (valor * taxa_de_câmbio) # Faz a conversão para Real (com margem de erro)


if selecao_de_conversao in confirmacao: # Caso a conversão que o usuário selecionou esteja dentro da confirmação ...
    if selecao_de_conversao == '1': # Caso o usuário tenha pedido para transformar BRL em USD ...
        print(f"\nO resultado da conversão é {round(conversão_dolar,2)} Dólares") # Mostre o resultado da conversão feita
    elif selecao_de_conversao == '2': # Caso o usuário tenha pedido para transformar USD em BRL ...
        print(f"\nO resultao da conversão é {round(conversão_real,2)} Reais") # Mostre o resultado da conversão feita
