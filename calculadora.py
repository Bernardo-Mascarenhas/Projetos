# CALCULADORA BÁSICA
print("Operações dísponiveis: adição, subtração, divisão, multiplicação.")
operador = input("Qual operação você deseja fazer? : ").lower()
num1 = input("Escolha o primeiro número da operação: ")
num2 = input("Escolha o segundo número da operação: ")

num1 = float(num1)
num2 = float(num2)

try :
    adição = num1 + num2
    subtração = num1 - num2
    divisão = num1 / num2
    multiplicação = num1 * num2

    ADICAO_DIGITACAO = "adição", "adicao", "adiçao", "adicão"
    SUBTRACAO_DIGITACAO = "subtração", "subtracao", "subtraçao", "subtracão"
    DIVISAO_DIGITACAO = "divisão", "divisao"
    MULTIPLICACAO_DIGITACAO = "multiplicação", "multiplicacao", "multiplicaçao", "multiplicacão"


    if operador in ADICAO_DIGITACAO:
        print (f"O resultado foi {adição}")

    elif operador in SUBTRACAO_DIGITACAO:
        print (f"O resultado foi {subtração}")

    elif operador in DIVISAO_DIGITACAO :
        if num1 or num2 == 0 :
            print ("0 Não é divisivel")
        else :
            print (f"O resultado foi {divisão}")
            

    elif operador in MULTIPLICACAO_DIGITACAO :
        print (f"O resultado foi {multiplicação}")

    else :
        print ("Operação inválida")

except ValueError:
    print("Preencha todos os campos")
except ZeroDivisionError:
    print("O número 0 não é divisivel")