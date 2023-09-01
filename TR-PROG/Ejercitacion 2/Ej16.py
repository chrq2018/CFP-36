"""16. A la casa de empanadas le funciono tan bien 
       nuestro programa que se fue para arriba, ahora 
       agrego una modalidad mas de pago, antes era 
       solo efectivo ahora tambien se puede abonar 
       con tarjeta de credito, pero ojo tiene 
       intereses y la casa de empanadas no quiere perder.
       Entonces quiere que adaptemos el programa para 
       que el usuario pueda abonar con efectivo, 
       en este caso va a tener un descuento del 10%, 
       y si abona con tarjeta de credito es el precio normal."""
       
# Cosntantes 
MENSAJE_ERROR = "ERROR!!!, Ingreso una opcion incorrecta"
PAGO_TARJETA_CREDITO = "T"
PAGO_EFECTIVO = "E"
DESCUENTO_PAGO_EFECTIVO = 0.10
OPCION_JYQ = 1
OPCION_CARNE = 2 
total = 0

print("******************************")
print("***** MENU DE EMPANADAS: *****")
print("******************************")
print("  1. jamon y queso")
print("  2. carne")
print()
print("***Ingrese el precio de las empanadas***")       
precio_empanada_jyq = float(input("   Ingrese el precio de la empanada de jyq: "))
precio_empanada_carne = float(input("   Ingrese el precio de la empanada de carne: "))
print()
print("***TIPO DE PAGO***")
print("   E. Efectivo")
print("   T. Tarjeta de credito")
tipo_pago = str(input("Ingrese el tipo de pago: ")).upper()
if tipo_pago == PAGO_EFECTIVO or tipo_pago == PAGO_TARJETA_CREDITO:
        print("***Ingrese el pedido de empanadas***")   
        tipo_empanada = int(input("Ingrese el tipo de empanada : "))
        if tipo_empanada == OPCION_JYQ or tipo_empanada == OPCION_CARNE: 
                cant_empanadas = int(input("ingrese la cantidad de empanadas: "))
                if tipo_empanada == OPCION_JYQ:
                        total = cant_empanadas * precio_empanada_jyq
                else:
                        total = cant_empanadas * precio_empanada_carne
        
                if tipo_pago == PAGO_EFECTIVO:
                        descuento = total*DESCUENTO_PAGO_EFECTIVO
                else:
                        descuento = 0
                total = total - descuento
                print(f"Descuento por pago en efectivo: ${descuento}")
                print(f"Monto total a pagar: ${total}")  
        else:
                print(MENSAJE_ERROR)         
else:
        print(MENSAJE_ERROR)