"""9. Para tributar un determinado impuesto se debe ser mayor 
      de 16 años y tener unos ingresos iguales o superiores 
      a 1000 € mensuales. Escribir un programa que pregunte 
      al usuario su edad y sus ingresos mensuales y muestre 
      por pantalla si el usuario tiene que tributar o no."""
        
edad_usuario = int(input("Ingrese edad: "))  
ingresos_usuario = float(input("Ingrese ingresos mensuales: "))

if edad_usuario > 16 and ingresos_usuario >= 1000 :
    print("Tiene que tributar")
else:
    print("No tiene que tributar")