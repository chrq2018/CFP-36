"""
Preguntar al usuario que gusto quiere
Preguntar al usuario el valor que quiere pagar por cada empanada.
Cuantas quiere de cada una.


"""
gusto = str(input("Que gustos de empanada quiere comprar (jyq / carne)?: ")).lower()
#cantidad= int(input("Ingrese la cantidad de empanadas que quiere llevar?: ")) 
#precio_jyq = int(input("ingrese el precio de la empanada de jyq: "))
#precio_carne = int(input("ingrese el precio de la empanada de carne: "))

importe = 0
if gusto == "jyq":
    cantidad_jyq = int(input("Ingrese la cantidad de empanadas que quiere llevar?: ")) 
    precio_jyq = int(input("ingrese el precio de la empanada de jyq: "))
    otro_gusto = str(input("Desea de carne (si / no)"))
    if otro_gusto == "si":
        cantidad_carne = int(input("Ingrese la cantidad de empanadas de carne que quiere llevar?: ")) 
        precio_carne = int(input("ingrese el precio de la empanada de carne: "))
        importe += precio_carne*cantidad_carne + precio_jyq*cantidad_jyq
    else:
        importe = precio_jyq*cantidad_jyq
    print(f"El importe es: ${importe}")
elif gusto == "carne":
    cantidad_carne = int(input("Ingrese la cantidad de empanadas que quiere llevar?: ")) 
    precio_carne = int(input("ingrese el precio de la empanada de carne: "))
    otro_gusto = str(input("Desea de jyq (si / no): "))
    if otro_gusto == "si":
        cantidad_jyq = int(input("Ingrese la cantidad de empanadas de jyq que quiere llevar?: ")) 
        precio_jyq = int(input("ingrese el precio de la empanada de jyq: "))
        importe = precio_jyq*cantidad_jyq + precio_carne*cantidad_carne
    else:
        importe = precio_carne*cantidad_carne
    print(f"El importe es: ${importe}")
else:
    print(f"Ingresó un gusto incorrecto!!!")
