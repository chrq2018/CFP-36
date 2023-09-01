"""Una escuela nos contrata para diseñar un programa que tome los nombres de los alumnos (seran 3 alumnos),
   y ellos cursan 3 materias (anuales), son 3 notas (1 cuatri,2cuatri y final(promedio)).
   Los alumnos ingresaran su nombre, las 3 materias que son iguales para los 3, y sus notas.
   El programa debera mostrar por pantalla, el nombre de los 3 alumnos, junto con su promedio, y si aprobo.
   Se aprueba con 7
"""
FISICA = "FISICA"
MATEMATICA = "MATEMATICA"
PROGRAMACION = "PROGRAMACION"
NOTA_APROBADO = 7
CANT_MATERIAS = 3
CANT_NOTAS = 2
promedio = 0

alumno = str(input("Ingrese nombre: ")).upper()
print()
print("******************************************")
print(f"*********** Alumno: {alumno} ************")
print("******************************************")
print(f"Materia: {FISICA}")
print("  NOTAS: ")
nota1 = int(input("   Primer cuatrimestre: "))
nota2 = int(input("   Segundo cuatrimestre: "))
promedio_fisica = (nota1 + nota2) / CANT_NOTAS
print()
print(MATEMATICA)
print("  NOTAS: ")
nota1 = int(input("   Primer cuatrimestre: "))
nota2 = int(input("   Segundo cuatrimestre: "))
promedio_matematica = (nota1 + nota2) / CANT_NOTAS
print()
print(PROGRAMACION)
print("  NOTAS: ")
nota1 = int(input("   Primer cuatrimestre: "))
nota2 = int(input("   Segundo cuatrimestre: "))
promedio_programacion = (nota1 + nota2) / CANT_NOTAS
promedio = (promedio_fisica + promedio_matematica + promedio_programacion)/CANT_MATERIAS 
print()
print("**************************")
print(f"Alumno: {alumno}")
print(f"  Promedio: {round(promedio, 2)}")
if promedio >= NOTA_APROBADO:
    print("  Aprobó")
else:
    print("  No aprobó")
print("**************************")
print()
print("***************** Otro Alumno *****************************")
print()
alumno = str(input("Ingrese nombre: ")).upper()
print()
print("******************************************")
print(f"*********** Alumno: {alumno} ************")
print("******************************************")
print(f"Materia: {FISICA}")
print("  NOTAS: ")
nota1 = int(input("   Primer cuatrimestre: "))
nota2 = int(input("   Segundo cuatrimestre: "))
promedio_fisica = (nota1 + nota2) / CANT_NOTAS
print()
print(MATEMATICA)
print("  NOTAS: ")
nota1 = int(input("   Primer cuatrimestre: "))
nota2 = int(input("   Segundo cuatrimestre: "))
promedio_matematica = (nota1 + nota2) / CANT_NOTAS
print()
print(PROGRAMACION)
print("  NOTAS: ")
nota1 = int(input("   Primer cuatrimestre: "))
nota2 = int(input("   Segundo cuatrimestre: "))
promedio_programacion = (nota1 + nota2) / CANT_NOTAS
promedio = (promedio_fisica + promedio_matematica + promedio_programacion)/CANT_MATERIAS 
print()
print("**************************")
print(f"Alumno: {alumno}")
print(f"  Promedio: {round(promedio, 2)}")
if promedio >= NOTA_APROBADO:
    print("  Aprobó")
else:
    print("  No aprobó")
print("**************************")
print()
print("***************** Otro Alumno *****************************")
print()
alumno = str(input("Ingrese nombre: ")).upper()
print()
print("******************************************")
print(f"*********** Alumno: {alumno} ************")
print("******************************************")
print(f"Materia: {FISICA}")
print("  NOTAS: ")
nota1 = int(input("   Primer cuatrimestre: "))
nota2 = int(input("   Segundo cuatrimestre: "))
promedio_fisica = (nota1 + nota2) / CANT_NOTAS
print()
print(MATEMATICA)
print("  NOTAS: ")
nota1 = int(input("   Primer cuatrimestre: "))
nota2 = int(input("   Segundo cuatrimestre: "))
promedio_matematica = (nota1 + nota2) / CANT_NOTAS
print()
print(PROGRAMACION)
print("  NOTAS: ")
nota1 = int(input("   Primer cuatrimestre: "))
nota2 = int(input("   Segundo cuatrimestre: "))
promedio_programacion = (nota1 + nota2) / CANT_NOTAS
promedio = (promedio_fisica + promedio_matematica + promedio_programacion)/CANT_MATERIAS 
print()
print("**************************")
print(f"Alumno: {alumno}")
print(f"  Promedio: {round(promedio, 2)}")
if promedio >= NOTA_APROBADO:
    print("  Aprobó")
else:
    print("  No aprobó")
print("**************************")
print()
print("******************* FIN ***************************")







