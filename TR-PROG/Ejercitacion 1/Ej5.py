"""5. Escribir un programa que pregunte al usuario 
      una cantidad a invertir, el interés anual y 
      el número de años, y muestre por pantalla el 
      capital obtenido en la inversión. M = C * (1 + i)**n"""
       
cantidad_a_invertir = float(input("Ingrese la cantidad que desea invertir: "))
interes_anual = float(input("Ingrese el interes anual (entre 0 y 1): ")) 
cant_anios = float(input("Ingrese la cantidad de años: "))

capital_obtenido = cantidad_a_invertir*((1 + interes_anual)**cant_anios)

print("El capital obtenido por la inversion es: $", capital_obtenido)
