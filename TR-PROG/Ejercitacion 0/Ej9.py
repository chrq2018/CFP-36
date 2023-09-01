"""9. Preguntar al usuario su edad y guardarlo en una variable 
      llamada <Edad>, luego si el número ingresado el usuario es par, 
      mostrar por pantalla un mensaje que diga <”Su edad es un número par”>, 
      y si es impar mostrar por pantalla un mensaje que diga <”Su edad es impar”>.."""
      
edad = int(input("Ingrese su edad: "))

if edad %2 == 0 :
    print("Su edad es par")
else:
    print("Su edad es impar")