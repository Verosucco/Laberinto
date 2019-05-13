#creamos un archivo nuevo 
#guardamos en la carpeta del repositorio con la extension .py
#uso de numeros aleatorios 

from random import randint  #importamos la libreria randint 
aleatorio=randint(0,20)     #creamos una variable y generamos un numero aleatorio entre 0 y 20
print(aleatorio)            #imprimimos el numero generado  
#ejercicio
#escribir una funcion sorteo() que reciba una lista de participantes, y elegir uno de los participantes
#aleatoriamente y retornar esa persona elegida.
#desafio:no volver a retornar una persona ya sorteada  


from random import randint       #importamos la funcion randint de la libreria randint                 
def sorteo(nombres):             #creamos una funcion con el nombre sorteo
    cantidad=len(nombres)-1      #definimos la cantidad de elementos que posee la lista(le restamos 1 por que se cuenta desde 0) y guardamos en una variable
    posicion=randint(0,cantidad) #elige un elemento aleatorio dependiendo de la posicion y la guardamos en una variable
    gan=nombres[posicion]        #seleccionamos un elemento de la lista y guardamos en la variable gan
    print(cantidad)              # imprimimos la cantidad de elementos que posee la lista
    return gan                   #retorna la variable con el nombre del ganador

nombres=["Andres","Roberto","Maria","Jeremias","Vero"] #creamos la lista fuera de la funcion
ganador=sorteo(nombres)          #llamamos a la funcion y la guardamos en una variable
print(ganador)                   #imprimimos la variable que contiene el nombre ganador 