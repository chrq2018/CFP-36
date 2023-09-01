"""6. Escribir un programa que pregunte al usuario 
      su edad y muestre por pantalla si es mayor de edad o no."""
    
EDAD_MAYOR = 18  # es una constante  
edad = int(input("Ingrese edad: "))

if edad <= 0:
        print("error")
elif edad < EDAD_MAYOR:
    print("Es menor de edad")
elif edad > 120:
        print("error")
else:
    print("Es mayor de edad")