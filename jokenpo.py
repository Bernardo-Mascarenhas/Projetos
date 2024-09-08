import random

escolha_usuario = input("Escolha apenas 1 (pedra, papel, tesoura): ").lower()

escolhas_possiveis = ['pedra','papel','tesoura']
escolha_computador = random.choice(escolhas_possiveis)
print(f"Seu oponente escolheu : {escolha_computador}")

if escolha_usuario in escolhas_possiveis:
    if escolha_usuario == escolha_computador:
        print("Empate !")
    elif escolha_usuario == 'pedra' and escolha_computador == 'tesoura' :
        print ("Você Venceu !")
    elif escolha_usuario == 'papel' and escolha_computador == 'pedra':
        print ("Você Venceu !")
    elif escolha_usuario == 'tesoura' and escolha_computador == 'papel':
        print ("Você Venceu !")
    else:
        print ("Você Perdeu !")
else:
    print("Selecione um valor válido")