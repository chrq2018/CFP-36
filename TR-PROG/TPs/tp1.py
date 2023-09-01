""" TP1. Un sastre vende tela, tiene color blanco, azul y rojo, preguntar al cliente de que color
    va a querer y cuantos metros de cada uno en caso de que quiera mas de un color.
    el color blanco cuesta 15 pesos x metro, el rojo cuesta 20 y el azul 25.
    Imprimir por consola cuantos metros esta llevando en total y cuanto es el total del dinero."""
  
# Constantes  
PRECIO_TELA_BLANCA = 15   
PRECIO_TELA_AZUL = 25 
PRECIO_TELA_ROJA = 20  
COLOR_TELA_BLANCA = "blanco"
COLOR_TELA_AZUL = "azul"
COLOR_TELA_ROJA = "rojo"
MENSAJE_METROS = "¿Cuantos metros quiere?: "
MENSAJE_OTRO_COLOR = "¿Quiere comprar otro color? (si / no)?: "
MENSAJE_ERROR = "ERROR!!!, ingreso un valor incorrecto"
importe = 0
total_metros = 0
    
color_tela = str(input("¿Que color de tela quiere comprar (blanco, azul o rojo)?: ")).lower()
if color_tela == COLOR_TELA_BLANCA:
    metros_tela_blanca = int(input(MENSAJE_METROS))
    otro_color = str(input(MENSAJE_OTRO_COLOR)).lower()
    if otro_color == "si":
        color_tela = str(input("¿Que color de tela quiere comprar (azul o rojo)?: ")).lower()
        if color_tela == COLOR_TELA_AZUL:
            metros_tela_azul = int(input(MENSAJE_METROS))
            otro_color = str(input(MENSAJE_OTRO_COLOR)).lower()
            if otro_color == "si":
                color_tela = str(input("¿Que color de tela quiere comprar (rojo)?: ")).lower()
                metros_tela_rojo = int(input(MENSAJE_METROS))
                print(f"Total a Pagar: ${metros_tela_blanca*PRECIO_TELA_BLANCA + metros_tela_azul*PRECIO_TELA_AZUL + metros_tela_rojo*PRECIO_TELA_ROJA}")
                print(f"La cantidad de metros comprados es: {metros_tela_azul + metros_tela_blanca + metros_tela_rojo}")
            elif otro_color == "no":
                print(f"Total a Pagar: ${metros_tela_blanca*PRECIO_TELA_BLANCA + metros_tela_azul*PRECIO_TELA_AZUL}")
                print(f"La cantidad de metros comprados es: {metros_tela_azul + metros_tela_blanca}")
            else:
                print(MENSAJE_ERROR)
    elif otro_color == "no":
        print(f"Total a Pagar: ${metros_tela_blanca*PRECIO_TELA_BLANCA}")
    else:
        print(MENSAJE_ERROR )
       
elif color_tela == COLOR_TELA_AZUL:
    metros_tela_azul = int(input(MENSAJE_METROS))
    otro_color = str(input(MENSAJE_OTRO_COLOR)).lower()
    if otro_color == "si":
        color_tela = str(input("¿Que color de tela quiere comprar (blanco o rojo)?: ")).lower()
        if color_tela == COLOR_TELA_BLANCA:
            metros_tela_blanca = int(input(MENSAJE_METROS))
            otro_color = str(input(MENSAJE_OTRO_COLOR)).lower()
            if otro_color == "si":
                color_tela = str(input("¿Que color de tela quiere comprar (rojo)?: ")).lower()
                metros_tela_rojo = int(input(MENSAJE_METROS))
                print(f"Total a Pagar: ${metros_tela_blanca*PRECIO_TELA_BLANCA + metros_tela_azul*PRECIO_TELA_AZUL + metros_tela_rojo*PRECIO_TELA_ROJA}")
                print(f"La cantidad de metros comprados es: {metros_tela_azul + metros_tela_blanca + metros_tela_rojo}")
            elif otro_color == "no":
                print(f"Total a Pagar: ${metros_tela_blanca*PRECIO_TELA_BLANCA + metros_tela_azul*PRECIO_TELA_AZUL}")
                print(f"La cantidad de metros comprados es: {metros_tela_azul + metros_tela_blanca}")
            else:
                print(MENSAJE_ERROR)

    elif otro_color == "no":
        print(f"Total a Pagar: {metros_tela_azul*PRECIO_TELA_AZUL}")
    else:
        print(MENSAJE_ERROR)

elif color_tela == COLOR_TELA_ROJA:
    metros_tela_rojo = int(input(MENSAJE_METROS))
    otro_color = str(input(MENSAJE_OTRO_COLOR)).lower()
    if otro_color == "si":
        color_tela = str(input("¿Que color de tela quiere comprar (blanco o azul)?: ")).lower()
        if color_tela == COLOR_TELA_AZUL:
            metros_tela_azul = int(input(MENSAJE_METROS))
            otro_color = str(input(MENSAJE_OTRO_COLOR)).lower()
            if otro_color == "si":
                color_tela = str(input("¿Que color de tela quiere comprar (blanco)?: ")).lower()
                metros_tela_blanca = int(input(MENSAJE_METROS))
                print(f"Total a Pagar: ${metros_tela_rojo*PRECIO_TELA_BLANCA + metros_tela_azul*PRECIO_TELA_AZUL + metros_tela_rojo*PRECIO_TELA_ROJA}")
                print(f"La cantidad de metros comprados es: {metros_tela_azul + metros_tela_blanca + metros_tela_rojo}")
            elif otro_color == "no":
                print(f"Total a Pagar: ${metros_tela_rojo*PRECIO_TELA_ROJA + metros_tela_azul*PRECIO_TELA_AZUL}")
                print(f"La cantidad de metros comprados es: {metros_tela_azul + metros_tela_rojo}")
            else:
                print(MENSAJE_ERROR)
    elif otro_color == "no":
        print(f"Total a Pagar: {metros_tela_rojo*PRECIO_TELA_ROJA}")
    else:
        print(MENSAJE_ERROR)

else:
    print(MENSAJE_ERROR) 