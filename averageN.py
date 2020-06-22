#Ask to input how much notes need to do average, then introduce notes and finally do the average.

def media():
  num_notas = int(input("¿ Cuantas notas vas has de medir ? "))
  total_notas = 0
  
  for x in range(1, num_notas+1):
    numbers = float(input(f"Introduce la nota {x}: "))
    total_notas += numbers
    print(f"nota {x}: ", numbers)
    
  avg = total_notas / num_notas
  print("La media de tus notas es: ", avg)

media()

