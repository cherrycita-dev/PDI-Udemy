# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 01:48:20 2025

@author: Nancy
"""

# Ciclo For: Se utiliza para recorrer los elementos de un objeto iterable, lista, tupla, diccionario

listaDeValores= 16,20,18,5,9,23,29


# for valor in listaDeValores:
#     print(valor
        
         
# print(listaDeValores[1])
# for valor in range(len(listaDeValores)):
#     print(listaDeValores[valor])





# # Suma valores en lista
# suma=0
# for valor in listaDeValores:
#     suma= suma + valor
# print(suma)


## Imprimir rango de valores
# for elemento in range(1,6):
#     print(elemento)

## Encontrar algun valor

# for elemento in listaDeValores:
#     if elemento == 18 :
#         print("Se ha encontrado el valor ", elemento)
#         break
#     print(elemento)
    
    
    
## Otra forma de hacerlo

# if 18 in listaDeValores:
#     print("se encontro un 18")
# else:
#     print("no se encontro el 18")



# =============================================================================
# Encontrar valor ingresado
# =============================================================================
# valorAEncotrar= int(input ("Ingrese el elemento a encontrar: "))
# for elemento in listaDeValores:
#     if elemento == valorAEncotrar:
#         print("Elemento encontrado", elemento)
#         break
#     else:
#          print("No se encontro el elemento", valorAEncotrar)    
# else:
#     print("Se termino la busqueda sin exito")
    

 
## Ciclo while:repetir fraccion de código con resultado F o T

# Ciclo while controlado por conteo

# cuenta = 0
# while cuenta <10 :
#     cuenta= cuenta+1
#     print(cuenta)
    

# Ciclo while controlado por evento

# numero = int(input("Ingrese 0 para salir: "))
# while numero !=0:
#     print(numero)
    
#     numero = int(input("Ingrese 0 para salir: "))
    

# Sentencia Break

cuenta=0
while cuenta<11:
    cuenta=cuenta+1
    if cuenta == 3:
        continue #saltarse la linea
    if cuenta ==0:
        break
    print(cuenta)
    


# ciclo infinito
cuenta=0
while True:
    cuenta= cuenta+1
    print(cuenta)












