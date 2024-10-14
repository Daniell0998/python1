#1
print ("Cual es tu nombre?")
nombre=input()
print ("Hola", nombre, "me alegro de conocerle",nombre)

#2
print ("Dime tu nombre")
nombre=input()
print ( nombre.upper," tu nombre tiene", nombre.len, "caracteres")

#3
print ("Dime el numero en el que quieres para de contar numeros pares.")
numero=input()
i=2
while i<numero:
    print (i)
    i+=2
#4
print ("Dime tu peso")
peso=input()
print ("Dime tu altura")
altura= input
resul =peso/altura
rounded_number = round(resul, 2)
print ("Tu indice de masa corporal es" ,rounded_number )

#5
import random
numeroA= random.randint(2,10) 
numeroB=random.randint(2,10)
resul =numeroA*numeroB
print ("Dime el rultado de la siguiente multiplicacion", numeroA, "X", numeroB) 
numeroRespondido=input()
if resul==numeroRespondido:
    print ("Has acertado")
else:
    print ("Has fallado")
