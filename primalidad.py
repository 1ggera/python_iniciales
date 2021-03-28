def es_primo(numero): #decimos que si el contador al dividirlo por uno y por si mismo no dió un resto igual a cero, por lo tanto el contador nunca aumento, entonces es TRUE, sino FALSE.
  contador = 0

  for i in range(1, numero + 1): #ponemos numero + 1 para llegar a imprimir los valores hasta el numero  que ingreso el usuario
    if i == 1 or i == numero: #si i es igual a 1 o a numero nos saltamos la linea.
      continue 
    if numero % i == 0: #si al dividir el numero por i nos da cero, le sumamos un valor al contador
      contador += 1
  if contador == 0:
    return True
  else:
    return False

def run():
  numero = int(input("Escribe un número: "))
  if es_primo(numero): #No hace falta poner la comparación de si número es igual a True
    print("Es primo")
  else:
    print("No es primo")

if __name__ == "__main__":
  run()
