def conversor(tipo_pesos, valor_dolar):
  pesos = input("¿Cuántos pesos" + tipo_pesos + "tenés?: ")
  pesos = float (pesos) #transforma el valor ingresado en un numero con decimales
  dolares = pesos / valor_dolar #establecemos que nuestros pesos seran pasados a dolares
  dolares = round(dolares, 2) #para establecer la cantidad de números decimales con la palabra reservada ROUND
  dolares = str(dolares)
  print("Tienes $" + dolares + " dólares")  


menu = """
Bienvenido al conversor de monedas 💰

1. Pesos argentinos
2. Pesos mexicanos
3. Reales brasileños

"""

opcion = int(input(menu)) #con INT convierto a entero para que me tome el número que ingreso xq sino py siempre toma el valor ingresado como texto

if opcion == 1:
  conversor(" argentinos ", 142)
elif opcion == 2:
  conversor(" mexicanos ", 20.59)
elif opcion == 3:
  conversor(" reales brasileños ", 5.75)
else:
  print("Ingresa una opción correcta por favor.")

