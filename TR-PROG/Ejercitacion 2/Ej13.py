"""13. Lo mismo que el anterior pero esta vez son 
       menos estrictos pero quieren plata, si 
       ganamos mas de $200000 al mes o si tenemos 
       entre 25 y 45. Hombres y mujeres por igual."""
    
sueldo = float(input("Ingrese sueldo: "))
edad = int(input("Ingrese edad: "))

if (sueldo > 200000) or (edad >= 25 and edad <= 45) :
    mensaje = "Puede ingresar" 
else:
    mensaje = "No puede ingresar"    

print(mensaje)