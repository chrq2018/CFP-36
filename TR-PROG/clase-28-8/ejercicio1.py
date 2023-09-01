"""
Preguntar al usuario que gusto quiere
Preguntar al usuario el valor que quiere pagar por cada empanada.
Cuantas quiere de cada una.


"""
gusto = str(input("Que gustos de empanada quiere comprar (jyq / carne)?: ")).lower()
#cantidad= int(input("Ingrese la cantidad de empanadas que quiere llevar?: ")) 
#precio_jyq = int(input("ingrese el precio de la empanada de jyq: "))
#precio_carne = int(input("ingrese el precio de la empanada de carne: "))


if gusto == "jyq":
    cantidad= int(input("Ingrese la cantidad de empanadas que quiere llevar?: ")) 
    precio_jyq = int(input("ingrese el precio de la empanada de jyq: "))
    otro_gusto = str(input("Desa de carne (si / no)"))
    print(f"El importe es: ${precio_jyq*cantidad}")
elif gusto == "carne":
     cantidad= int(input("Ingrese la cantidad de empanadas que quiere llevar?: ")) 
     precio_carne = int(input("ingrese el precio de la empanada de carne: "))
     print(f"El importe es: ${precio_jyq*cantidad}")
else:
    print(f"Ingresó un gusto incorrecto!!!")
