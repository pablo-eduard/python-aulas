import random

secreto=random.randint(1,7)
palpite=0

while palpite!=secreto:
    palpite=int(input('Escolha o número: '))
    
    
    if palpite!=secreto:
        print("Você errou! Tente novamente.")

print("Você acertou!!!")


    


  