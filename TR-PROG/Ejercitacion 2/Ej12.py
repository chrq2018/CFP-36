"""12. Como les gusto nuestro trabajo ahora nos 
       llamaron del bar de al lado y nos piden 
       un programa que, solamente deje pasar 
       mujeres de entre 20 y 50 años, 
       y hombres de entre 30 y 40 años."""


HOMBRE = "H"
MUJER = "M"

sexo = str(input("Ingrese sexo (H. hombre / M.  mujer): ")).upper()

if sexo == "H" or sexo == "M":
    edad = int(input("Ingrese edad: "))
    if (edad >= 20 and edad <= 50) and sexo == MUJER :
        mensaje = "Puede ingresar"
    elif (edad >= 30 and edad <= 40) and sexo == HOMBRE :
        mensaje = "Puede ingresar"
    else:
        mensaje = "No puede ingresar"   
else:
    print("Opcion incorrecta")
print(mensaje)
print("---------------")
print("Fin del programa")