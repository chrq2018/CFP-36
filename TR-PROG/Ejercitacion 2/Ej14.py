"""14. Felicitaciones somos tan buenos que ahora nos 
       llaman hasta de la casa de empanadas, quieren 
       que hagamos un programa que el usuario ingrese 
       que cantidad de empanadas quiere y le arroje 
       por pantalla cuanto tiene que abonar, teniendo 
       en cuenta que el lugar solo vende empanadas 
       de jyq y de carne, y cada empanada vale diferente.
       Las de carne valen $500 y las de jyq valen $700."""
MENSAJE_ERROR = "Ingreso una opcion incorrecta"
OPCION_JYQ = 1
OPCION_CARNE = 2 
PRECIO_JYQ = 700
PRECIO_CARNE = 500 

print("***** MENU DE EMPANADAS: *****")
print("  1. jamon y queso")
print("  2. carne")

tipo_empanada = int(input("Ingrese el tipo de empanada : "))

if tipo_empanada == OPCION_JYQ or tipo_empanada == OPCION_CARNE:
    cant_empanadas = int(input("ingrese la cantidad de empanadas: "))
    if tipo_empanada == OPCION_CARNE:
        total = cant_empanadas*PRECIO_CARNE
    else:
        total = cant_empanadas*PRECIO_JYQ
    print(f"Debe abonar: ${cant_empanadas * PRECIO_CARNE}")
else:
    print(MENSAJE_ERROR)


       
