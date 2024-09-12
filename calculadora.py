# CALCULADORA BÁSICA (:
print("Operações dísponiveis: adição, subtração, divisão, multiplicação.") # Mostra as operações possíveiei de se fazer 
operador = input("Qual operação você deseja fazer? : ").lower() # Pergunta qual operação o usuário quer fazer
num1 = input("Escolha o primeiro número da operação: ") # Pergunta qual será o primeiro operador
num2 = input("Escolha o segundo número da operação: ") # Pergunta qual será o segundo operador

num1 = float(num1) # Faz o resultado da pergunta se trasformar em um número decimal
num2 = float(num2) # Faz o resultado da pergunta se trasformar em um número decimal

try :
    adição = num1 + num2  # Faz a soma número 1 + número 2
    subtração = num1 - num2  # Faz a subtração número 1 - número 2
    divisão = num1 / num2  # Faz a divisão número 1 / número 2
    multiplicação = num1  * num2  # Faz a multiplicação número 1 * número 2

    ADICAO_DIGITACAO = "adição", "adicao", "adiçao", "adicão" # Faz o cógigo funcionar mesmo se o usuário tenha errado a digitação
    SUBTRACAO_DIGITACAO = "subtração", "subtracao", "subtraçao", "subtracão" # Faz o cógigo funcionar mesmo se o usuário tenha errado a digitação
    DIVISAO_DIGITACAO = "divisão", "divisao" # Faz o cógigo funcionar mesmo se o usuário tenha errado a digitação
    MULTIPLICACAO_DIGITACAO = "multiplicação", "multiplicacao", "multiplicaçao", "multiplicacão" # Faz o cógigo funcionar mesmo se o usuário tenha errado a digitação


    if operador in ADICAO_DIGITACAO: # Caso o usuário tenha digitado Adição, mostra o resultado da adição
        print (f"O resultado foi {adição}")

    elif operador in SUBTRACAO_DIGITACAO: # Caso o usuário tenha digitado Subtração, mostra o resultado da subtração
        print (f"O resultado foi {subtração}")

    elif operador in DIVISAO_DIGITACAO: # Caso o usuário tenha digitado Divisão, mostra o resultado da divisão
        if num1 or num2 == 0: # Dá erro caso o usuário tenha digitado 0 em algum dos campos tendo selecionado divisão 
            print ("0 Não é divisivel")
        else :
            print (f"O resultado foi {divisão}")
            
    elif operador in MULTIPLICACAO_DIGITACAO:  # Caso o usuário tenha digitado Multiplicação, mostra o resultado da multiplicação
        print (f"O resultado foi {multiplicação}")

    else :  # Caso o usuário tenha digitado um valor inválido, mostre uma mensagem de erro
        print ("Operação inválida")

except ValueError:
    print("Preencha todos os campos")
except ZeroDivisionError:
    print("O número 0 não é divisivel")
