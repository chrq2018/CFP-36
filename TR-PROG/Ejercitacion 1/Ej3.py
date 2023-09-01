"""3. Escribir un programa que pregunte al usuario 
      por el número de horas trabajadas y el coste 
      por hora. Después debe mostrar por pantalla 
      la paga que le corresponde."""
        
horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))
coste_por_hora = float(input("Ingrese el coste por hora: "))

sueldo = horas_trabajadas * coste_por_hora

print("La paga que le corresponde es: $", sueldo)
        