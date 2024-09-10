print(
    """CONVERSOR DE UNIDADES. Digite 'C' para transformar Celsius em Fahrenheits,
Ou digite 'F' para transformar Fahrenheits em Celsius"""
    )

try:

    unidade = input("\nQual unidade você deseja converter?: ").upper()

    temperatura = input(f"\nEscolha o valor que você que será convertido em '{unidade}': ")
    temperatura = float(temperatura)

    celsius_para_fahrenheit = (temperatura * 1.8) + 32
    fahrenheit_para_celsius = (temperatura - 32) / 1.8

    celsius_para_fahrenheit = round(celsius_para_fahrenheit, 2)
    fahrenheit_para_celcius = round(fahrenheit_para_celsius, 2)

    if unidade == 'C':
        print(f"\nO resultado é {celsius_para_fahrenheit}")

    if unidade == 'F':
        print(f"\nO resultado é {fahrenheit_para_celcius}")

except ValueError:
    print("\ninsíra um valor válido !")