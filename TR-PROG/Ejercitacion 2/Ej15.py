""" 15. Felicitaciones somos tan buenos que ahora nos 
        llaman hasta de la casa de empanadas, quieren 
        que hagamos un programa que el usuario ingrese 
        que cantidad de empanadas quiere y le arroje 
        por pantalla cuanto tiene que abonar, teniendo 
        en cuenta que el lugar solo vende empanadas 
        de jyq y de carne, y cada empanada vale diferente.
        El local le pone el precio a las empanadas."""

OPCION_JYQ = 1
OPCION_CARNE = 2 

print("***** MENU DE EMPANADAS: *****")
print("  1. jamon y queso")
print("  2. carne")

print("***Ingrese el precio de las empanadas***")       
precio_empanada_jyq = float(input("Ingrese el precio de la empanada de jyq: "))
precio_empanada_carne = float(input("Ingrese el precio de la empanada de carne: "))
print()
print("***Ingrese el pedido de empanadas***")   

tipo_empanada = int(input("Ingrese el tipo de empanada : "))

if tipo_empanada == OPCION_JYQ :
    cant_empanadas = int(input("ingrese la cantidad de empanadas: "))
    print(f"Debe abonar: ${cant_empanadas * precio_empanada_jyq}")
elif tipo_empanada == OPCION_CARNE:
    cant_empanadas = int(input("ingrese la cantidad de empanadas: "))
    print(f"Debe abonar: ${cant_empanadas * precio_empanada_carne}")
else:
    print("ERROR!!!, Ingreso una opcion incorrecta")