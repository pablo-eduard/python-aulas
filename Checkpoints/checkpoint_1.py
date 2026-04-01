import random

palpite=0
numero_secreto=random.randint(1,100)
tentativas=0

while palpite!=numero_secreto:
    
    palpite=int(input(f"Digite um número. {numero_secreto}:  "))
    
    if(palpite==numero_secreto):
        print(f"Parabéns, Você acertou!!! Total de Tentativas: {tentativas}")
    
    elif(tentativas==7):
        print("Gamer Over, excesso de tentativas !!!")
        break
    
    elif(palpite!=numero_secreto):
        if(numero_secreto>palpite):
            print("Errou, tente novamente!!!, Dica: É maior que isso.")
            tentativas=tentativas+1
        
        elif(numero_secreto<palpite):
            print("Errou, tente novamente!!!, Dica: É menor que isso.")
            tentativas=tentativas+1
