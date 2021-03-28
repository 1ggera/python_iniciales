#Acá estamos diciendole que imprima valores hasta el 1000 siempre y cuando el resultado de contador dividido por dos sea cero. Si es así, que continue imprimiendo
def run():
  for contador in range(1000):
    if contador % 2 != 0:
      continue
    print(contador)

if __name__ == "__main__":
  run()

#Acá imprimimos los valores hasta el 1000. Pero detenerse si el valor de i llegara a ser 5678.
for i in range (10000):
  print(i)
  if i == 5678:
    break

#Imprime los valores de un texto siempre y cuando no aparezca la letra O
texto = input("Ingresa una texto: ")
for letra in texto:
  if letra == "o":
    break
  print(letra)

