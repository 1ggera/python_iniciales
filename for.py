# print(1)
# print(2)
# print(3)
# print(4)

#Aplicando el ciclo WHILE
# contador = 1
# print(contador)
# while contador < 1000:
#   #contador = contador + 1 
#   contador += 1 #podemos reemplazar la linea superior por esta que opera de la misma forma
#   print(contador)

#Aplicando el ciclo FOR
for contador in range(1, 1001):
  print(contador) #le estamos diciendo que imprima los valores de la variable contador que van del 1 al 1001

#Otro ejemplo sería imprimiendo la tabla del once
for i in range(10): #declaramos la variable i que va de 1 en 1 hasta el 9, sin llegar al limite, la multiplicamos por 11 y se imprime.
  print(11 * i)
