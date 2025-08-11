# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 18:41:39 2025

@author: Nancy
"""

# Operadores lógicos
# Para formar expresiones que pueden ser representadas con verdadero o falso

# OR [SUMA]

# z = False or False
# print(z)

# z= False or True
# print(z)

# z = True or False
# print(z)

# z= True or True
# print(z)

# # AND a * b

# z = False and False
# print(z)

# z= False and True
# print(z)

# z = True and False
# print(z)

# z= True and True
# print(z)

# Not

# z= not False
# print(z)

# z= not True
# print(z)



# Operadores relacionales


# # Mayor que 
# z = 2>1
# print(z)

# # Menor que 
# z = 2 < 1
# print(z)

# # Mayor o igual que
# z= 2>=1
# print(z)

# # Menor o igual que
# z= 2<=2
# print(z)

# # Igual que, si se usa un = se puede tomar como variable
# z= 2 == 2
# print(z)


# # Diferente de
# z= 2 != 2
# print(z)


# # if
# z=1
# if z == 1:
#     print ("z es igual a 1")
# else: 
#     print("z es diferente de 1")


# elif, si ya se encontro, no seguir con el ciclo

# if z == 1:
#     print("z es igual a 1")
# elif z ==1:
#     print("z es igual a 1")
# elif z ==1:
#     print("z es igual a 1")
# elif z ==1:
#     print("z es igual a 1")

# edad= int(input("Ingresa tu edad: "))

# if edad >= 20 and edad <= 30 :
#     print("Puedes acceder")
# else:
#     print("No puedes acceder")    

# # If anidado, valor ingresado es un numero

# edad= input("Ingresa tu edad: ")

# if edad.isdigit():
#     if int(edad) >= 20 and int(edad) <=30:
#         print("Puedes acceder")
#     else:
#         print("No puedes acceder")

# else:
#     print("El valor ingresado no es digito")




edad= input("Ingresa tu edad: ")

if edad.isdigit():
    if int(edad) > 20 and int(edad) < 30:
        print("Puedes acceder")
    else:
        print("No puedes acceder")

else:
    print("El valor ingresado no es digito")
