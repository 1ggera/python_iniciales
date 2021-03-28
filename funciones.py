def imprimir_mensaje():
  print("Mensaje especial: ¡Estoy aprendiendo funciones!")
  print("Mensaje especial: ¡Estoy aprendiendo funciones!")
  print("Mensaje especial: ¡Estoy aprendiendo funciones!")

imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()

#Parámetros
def conversacion(mensaje):
  print("Hola")
  print("¿Cómo estás?")
  print(mensaje)
  print("Adiós")

opcion = int(input("Elige una opción (1, 2, 3): "))
if opcion == 1:
  conversacion("Elegiste la opción 1")
elif opcion == 2:
  conversacion("Elegiste la opción 2")
elif opcion == 3:
  conversacion("Elegiste la opcion 3")
else:
  print("Escribe una opción correcta por favor.")

