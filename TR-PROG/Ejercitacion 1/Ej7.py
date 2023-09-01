"""7. Escribir un programa que almacene la cadena de 
      caracteres contraseña en una variable, pregunte 
      al usuario por la contraseña e imprima por pantalla 
      si la contraseña introducida por el usuario coincide 
      con la guardada en la variable sin tener en cuenta 
      mayúsculas y minúsculas."""
        
clave = "contraseña"
clave_usuario = str(input("Ingrese la contraseña: ")).lower()

if clave == clave_usuario:
    print("La contreseña ingresada es correcta")
else:
    print("La contreseña ingresada no es correcta")