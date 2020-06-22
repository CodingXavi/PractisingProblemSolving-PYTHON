#Ask to input how much notes need to do average, then introduce notes and finally do the average.

def media():
  num = int(input("¿ Cuantas notas has de medir ? "))
  notas = 0
  
  for x in range(1, num+1):
    numbers = float(input(f"Introduce la nota {x}: "))
    notas += numbers
    print(f"nota {x}: ", numbers)
    
  avg = notas / num
  print("La media de tus notas es: ", avg)

media()

