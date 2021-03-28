# contador = 0
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador)) #convertimos el valor a str para poder imprimirlo
# contador = 1
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador)) #convertimos el valor a str para poder imprimirlo
# contador = 2
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador)) #convertimos el valor a str para poder imprimirlo
# contador = 3
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador)) #convertimos el valor a str para poder imprimirlo


#A continuación escribiremos las potencias de 2 hasta llegar a 1000
def run(): #Paso 1: definimos una funcioón principal
  LIMITE = 1000 #Paso 3: si la variable no varía a lo largo del programa la llamamos CONSTANTE va en MAYUSCULAS

  contador = 0
  potencia_2 = 2**contador
  while potencia_2 < LIMITE: #esta es una expresión que compara dos valores o más y devuelve verdadero o falso. Mientras se de esta condisión se ejecutará el siguiente código
    print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))
    contador = contador + 1
    potencia_2 = 2**contador

if __name__ == "__main__": #Paso 2: agregamos nuestro enter point
  run()
