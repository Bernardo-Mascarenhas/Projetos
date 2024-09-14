import random

escolha_usuario = input("Escolha apenas 1 (pedra, papel, tesoura): ").lower() # Pergunta ao usuário qual dos 3 ele escolhe (Pedra, Papel ou Tesoura)

escolhas_possiveis = ['pedra','papel','tesoura'] # Salva as escolhas possíveis na mémoria interna
escolha_computador = random.choice(escolhas_possiveis) # Pede para o computador escolher aleatoriamente uma das 3 escolhas possíveis
print(f"Seu oponente escolheu : {escolha_computador}") # Mostra a escolha do computador

if escolha_usuario in escolhas_possiveis: # Verifica se sua escolha está dentro das escolhas possíveis de se fazer
    if escolha_usuario == escolha_computador: # Caso você tenha escolhido a mesma coisa que o computador ...    
        print("Empate !") # Diga que houve um empate
    elif escolha_usuario == 'pedra' and escolha_computador == 'tesoura': # Caso você tenha escolhido pedra e o computador tesoura ...
        print ("Você Venceu !") # Diga que o usuário venceu
    elif escolha_usuario == 'papel' and escolha_computador == 'pedra': # Caso você tenha escolhido papel e o computador pedra ...
        print ("Você Venceu !") # Diga que o usuário venceu
    elif escolha_usuario == 'tesoura' and escolha_computador == 'papel': # Caso você tenha escolhido tesoura e o computador papel ...
        print ("Você Venceu !") # Diga que o usuário venceu
    else: # Caso o contrário ...
        print ("Você Perdeu !") # Diga que o usuário perdeu
else: # Caso a escolha do usuário não estea dentro das escolhas possíveis...
    print("Selecione um valor válido") # Diga ao usuário que ele digitou algo invalído
