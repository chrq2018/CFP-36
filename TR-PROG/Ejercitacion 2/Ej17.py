"""17. Felicitaciones somos tan buenos que ahora nos llaman hasta de la casa de empanadas, quieren 
       que hagamos un programa que el usuario ingrese que cantidad de empanadas quiere y le arroje 
       por pantalla cuanto tiene que abonar, teniendo en cuenta que el lugar solo vende empanadas 
       de jyq y de carne, y cada empanada vale diferente.El local le pone el precio a las empanadas. 
       A la casa de empanadas le funciono tan bien nuestro programa que se fue para arriba, ahora 
       agrego una modalidad mas de pago, antes era solo efectivo ahora tambien se puede abonar 
       con tarjeta de credito, pero ojo tiene intereses y la casa de empanadas no quiere perder.
       Entonces quiere que adaptemos el programa para que el usuario pueda abonar con efectivo, 
       en este caso va a tener un descuento del 10%, y si abona con tarjeta de credito es el precio normal.
       Ahora agrego gaseosas, tiene linea pepsi y linea coca, ellos tambien le quiere poner el precio, 
       tambien con la modalidad de pago, pero guarda agrego una promocion! Llevan 3 empanadas 
       (cualquiera sea su gusto, puede ser mixto), 
       y una gaseosa linea pepsi, el valor de la promo es de $1000 super barato no ? vamos a ver si podemos. """

# Cosntantes 
MENSAJE_ERROR = "ERROR!!!, Ingreso una opcion incorrecta"
SI = "S"
NO = "N"
PAGO_TARJETA_CREDITO = "T"
PAGO_EFECTIVO = "E"
DESCUENTO_PAGO_EFECTIVO = 0.10
OPCION_JYQ = 1
OPCION_CARNE = 2 
OPCION_COCA = 3
OPCION_PEPSI = 4
PROMO_1 = 5
PRECIO_PROMO1 = 1000
total = 0

print("******************************************")
print("****************** MENU ******************")
print("******************************************")
print("  1. Empanas - Gaseosas")
print("  2. Promo1 (3 empanadas y una Pepsi)")
print()
opcion_menu = int(input("Elija una opcion: "))
if opcion_menu == 1 or opcion_menu == 2:
    if opcion_menu == 1:
        print("********************************")
        print("***** Empanadas - Gaseosas *****")
        print("********************************")
        print("  1. jamon y queso")
        print("  2. carne")
        print("  3. Coca")
        print("  4. Pepsi")
        print()
        print("***Ingrese el precio de las empanadas***")       
        precio_empanada_jyq = float(input("   Ingrese el precio de la empanada de jyq: "))
        precio_empanada_carne = float(input("   Ingrese el precio de la empanada de carne: "))
        print()
        print("***Ingrese el precio de las gaseosas***")       
        precio_coca = float(input("   Ingrese el precio de la Coca: "))
        precio_pepsi = float(input("   Ingrese el precio de la Pepsi: "))
        print()
        print("***TIPO DE PAGO***") 
        print("   E. Efectivo")
        print("   T. Tarjeta de credito")
        tipo_pago = str(input("Ingrese tipo de pago: ")).upper()
        if tipo_pago == PAGO_EFECTIVO or tipo_pago == PAGO_TARJETA_CREDITO:
            print("***Ingrese el pedido de empanadas***")   
            print()
            tipo_empanada = int(input("Ingrese el tipo de empanada : "))
            if tipo_empanada == OPCION_JYQ or tipo_empanada == OPCION_CARNE :
                cant_empanadas = int(input(f"ingrese la cantidad de empanadas de {tipo_empanada}: "))
                if tipo_empanada == OPCION_JYQ:
                    total = cant_empanadas * precio_empanada_jyq
                else:
                    total = cant_empanadas * precio_empanada_carne

                opcion_gaseosa= str(input("Quiere comprar gaseosa (S. Si / N. No)?: ")).upper()
                if opcion_gaseosa == "S" or opcion_gaseosa == "N":
                    if opcion_gaseosa == "S": 
                        opcion_gaseosa = int(input("Ingrese la marca de la gaseosa (3. Coca / 4. Pepsi)"))
                        if opcion_gaseosa == OPCION_COCA or opcion_gaseosa == OPCION_PEPSI:
                            cantidad_gaseosa = int(input("Ingrese la cantidad de gaseosas: "))
                            if opcion_gaseosa == OPCION_COCA:
                                total += cantidad_gaseosa*precio_coca
                            else:
                                total += cantidad_gaseosa*precio_pepsi 
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
                else:
                    print(MENSAJE_ERROR)  
            else:
                print(MENSAJE_ERROR)
        else:
            print(MENSAJE_ERROR) 
    else:
        total = PRECIO_PROMO1
        print(f"Monto total a pagar: ${total}")     
else:
    print("3 " + MENSAJE_ERROR)