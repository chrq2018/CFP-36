"""11. Nos contratan de un boliche para hacer un programa 
       que facilite la entrada de la gente, nos piden que 
       pregunte la edad al ingresante y si este tiene hasta 
       15 años no puede entrar, si tiene entre 16 y 18 puede entrar 
       a matine, y si tiene mas de 18 puede pasar, pero si 
       tiene mas de 80 no podra acceder."""
    
edad = int(input("Ingrese la edad: "))

if (edad >= 0 and edad <= 15) :
    mensaje = "No puede ingresar"
elif edad >= 16 and edad <= 18 :
    mensaje = "Puede ingresar a Matine"
elif edad >= 19 and edad <= 80 :
    mensaje = "Puede pasar"
else :
    mensaje = "No puede acceder"

print(mensaje)
