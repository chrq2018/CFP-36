"""18. Bueno lo hemos logrado, nos han llamado de la pizeria mas famosa de BS AS.
       La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
       Los ingredientes para cada tipo de pizza aparecen a continuación.
       ○	Ingredientes vegetarianos: Pimiento y tofu.
       ○	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
       Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
       y en función de su respuesta le muestre un menú con los ingredientes disponibles 
       para que elija. Solo se puede eligir un ingrediente además de la mozzarella y 
       el tomate que están en todas la pizzas. 
       Al final se debe mostrar por pantalla si la pizza elegida es 
       vegetariana o no y todos los ingredientes que lleva."""

SI = "S"
NO = "N"
MENSAJE_ERROR = "ERROR!!!, Ingreso una opcion incorrecta"

print("***********************************************************************")       
print("********************** Pizzería Bella Napoli **************************")
print("***********************************************************************") 
print()
opcion_vegetariana = str(input("Quiere una pizza vegetariana (S. si / N. no)?: ")).upper()

if opcion_vegetariana == SI or opcion_vegetariana == NO :
       
       if opcion_vegetariana == SI:
              print("** Ingredientes menu Vegetariano: **")
              print("     Pimiento")
              print("     Tofu")  
              print()
              ingrediente = str(input("Elija un ingrediente: ")).lower()
              print()
              if(ingrediente == "pimiento" or ingrediente == "tofu"): 
                     print(f"La pizza es vegetariana y los ingredientes son: {ingrediente}, Muzzarella y tomate ") 
              else:
                     print(MENSAJE_ERROR)
       else:     
              print("** Ingredientes menu No Vegetariano: **")
              print("     Peperoni")
              print("     Jamon")  
              print("     Salmon")
              print()
              ingrediente = str(input("Elija un ingrediente: ")).lower()
              print()
              if(ingrediente == "peperoni" or ingrediente == "jamon" or ingrediente == "salmon"): 
                     print(f"La pizza es NO vegetariana  y los ingredientes son: {ingrediente}, Muzzarella y tomate ") 
              else:
                     print(MENSAJE_ERROR)      
else:
       print(MENSAJE_ERROR)

          
