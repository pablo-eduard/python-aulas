idade=int(input("Qual sua idade?: "))

if(idade<13):
    print("Você é Criança!")

elif(idade>=13 and idade<=17):
    print("Você é adolescente")

elif(idade>=18 and idade<=59):
    print("Você é Adulto!")

else:
    print("Você é idoso!")