#juego de adivinar el numero, todos juntos
#adivinar un numeo generado aleatoriamente,
#ir introduciendo por teclado el dato a adivinar.

from random import randint
generado=randint(0,10) #generamos el numero aleatorio
#print(generado) #trampa 
condicion=True
intento=10 
while condicion:
    if intento>0:
        numero=input("dame un numero del o al 10: ") 
        intento=intento-1 
        if generado==int(numero): #comparamos el numero introducido por el aleatorio 
            print("Ganaste") 
            condicion=False 
        else:
            print("el perdedor compra hamburguesa") 
            print("te quedan",intento,"intentos") 
        else:
            condicion=False 
            print("perdiste")