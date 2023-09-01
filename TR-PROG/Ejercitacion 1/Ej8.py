"""8. Escribir un programa que pida al usuario 
      un número entero y muestre por pantalla 
      si es par o impar."""
        
numero_ingresado = int(input("Ingrese un numero entero: "))
if numero_ingresado == 0:
        print("No aplica")
elif numero_ingresado %2 == 0 :
    print("El numero ingresado es par")
else: 
    print("El numero ingresado es impar")