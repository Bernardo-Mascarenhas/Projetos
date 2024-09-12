print(
    """CONVERSOR DE UNIDADES. Digite 'C' para transformar Celsius em Fahrenheits, 
Ou digite 'F' para transformar Fahrenheits em Celsius"""
    ) # Explca o que o usuário deve fazer

try: # Tente fazer:

    unidade = input("\nQual unidade você deseja converter?: ").upper() # Pergunta ao usuário qual unidade ele quer converter

    temperatura = input(f"\nEscolha o valor que você que será convertido em '{unidade}': ") # Pede para o usuário selecionar o valor que ele quer converter
    temperatura = float(temperatura) # Tenta transformar o valor selecionado em um número decimal
    
    celsius_para_fahrenheit = (temperatura * 1.8) + 32 # Salva formúla para converter celcius em fahrenheit
    fahrenheit_para_celsius = (temperatura - 32) / 1.8 # Salva formúla para converter fahrenheit em celcius
    
    celsius_para_fahrenheit = round(celsius_para_fahrenheit, 2) # Arredonda o resultado da formúla para apenas 2 número decimais
    fahrenheit_para_celcius = round(fahrenheit_para_celsius, 2) # Arredonda o resultado da formúla para apenas 2 número decimais
    
    if unidade == 'C': # Caso o usuário tenha pedido para transformar Celcius em Fahrenheit ...
        print(f"\nO resultado é {celsius_para_fahrenheit}") # Mostre o resultado da formula
    
    if unidade == 'F': # Caso o usuário tenha pedido para transformar Fahrenheit em Celcius ...
        print(f"\nO resultado é {fahrenheit_para_celcius}") # Mostre o resultado da formula

except ValueError: # Caso não consiga transformar em um número decimal, mostre uma mensagem de erro
    print("\ninsíra um valor válido !")
