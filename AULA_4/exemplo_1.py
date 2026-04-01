import time

contador=10

while(contador>0):
   
    print(f"Contagem regressiva: {contador}")
    contador-=1
    time.sleep(1)

if(contador<=0):
    print("FOGO!!!")

