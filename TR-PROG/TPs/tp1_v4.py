""" TP1. Un sastre vende tela, tiene color blanco, azul y rojo, preguntar al cliente de que color
    va a querer y cuantos metros de cada uno en caso de que quiera mas de un color.
    el color blanco cuesta 15 pesos x metro, el rojo cuesta 20 y el azul 25.
    Imprimir por consola cuantos metros esta llevando en total y cuanto es el total del dinero."""
  
# Constantes  
PRECIO_TELA_BLANCA = 15   
PRECIO_TELA_AZUL = 25 
PRECIO_TELA_ROJA = 20  
COLOR_TELA_BLANCA = "B"
COLOR_TELA_AZUL = "A"
COLOR_TELA_ROJA = "R"
MENSAJE_METROS = "¿Cuantos metros quiere?: "
MENSAJE_COLOR = "¿Que color de tela quiere comprar (B. blanco / A. azul / R. rojo)?: "
MENSAJE_OTRO_COLOR = "¿Quiere comprar otro color? (S. si / N. no)?: "
SI = "S"
NO = "N"

MENSAJE_ERROR = "ERROR!!!, ingreso un valor incorrecto"
importe = 0
total_metros = 0
    
color_tela = str(input(MENSAJE_COLOR)).upper()
if ((color_tela == COLOR_TELA_BLANCA)  or (color_tela == COLOR_TELA_AZUL) or (color_tela == COLOR_TELA_ROJA)):
    metros_tela1 = int(input(MENSAJE_METROS))
    if color_tela == COLOR_TELA_BLANCA:
       precio1 = PRECIO_TELA_BLANCA
    elif color_tela == COLOR_TELA_AZUL:
       precio1 = PRECIO_TELA_AZUL
    elif color_tela == COLOR_TELA_ROJA:
       precio1 = PRECIO_TELA_ROJA
    else: 
        print(MENSAJE_ERROR) 
    otro_color = str(input(MENSAJE_OTRO_COLOR)).upper()
    if otro_color == SI:
        color_tela = str(input(MENSAJE_COLOR)).upper()
        if ((color_tela == COLOR_TELA_BLANCA)  or (color_tela == COLOR_TELA_AZUL) or (color_tela == COLOR_TELA_ROJA)):
            metros_tela2 = int(input(MENSAJE_METROS))
            if color_tela == COLOR_TELA_BLANCA:
                precio2 = PRECIO_TELA_BLANCA
            elif color_tela == COLOR_TELA_AZUL:
                precio2 = PRECIO_TELA_AZUL
            elif color_tela == COLOR_TELA_ROJA:
                precio2 = PRECIO_TELA_ROJA
            else: 
                print(MENSAJE_ERROR)
            otro_color = str(input(MENSAJE_OTRO_COLOR)).upper()
            if otro_color == SI:
                color_tela = str(input(MENSAJE_COLOR)).upper()
                if ((color_tela == COLOR_TELA_BLANCA)  or (color_tela == COLOR_TELA_AZUL) or (color_tela == COLOR_TELA_ROJA)):
                    metros_tela3 = int(input(MENSAJE_METROS))
                    if color_tela == COLOR_TELA_BLANCA:
                        precio3 = PRECIO_TELA_BLANCA
                    elif color_tela == COLOR_TELA_AZUL:
                        precio3 = PRECIO_TELA_AZUL
                    elif color_tela == COLOR_TELA_ROJA:
                        precio3 = PRECIO_TELA_ROJA
                    else:
                        print(MENSAJE_ERROR)  
                    print(f"Debe pagar: $ {precio1*metros_tela1 + precio2*metros_tela2 + precio3*metros_tela3}")
                    print(f"Lleva {metros_tela1 + metros_tela2 + metros_tela3} metros de tela") 
                else:
                    print(MENSAJE_ERROR)  
            elif otro_color == NO:    
                print(f"Debe pagar: $ {precio1*metros_tela1 + precio2*metros_tela2} ") 
                print(f"Lleva {metros_tela1 + metros_tela2} metros de tela")
            else:
                print(MENSAJE_ERROR)   
        else:
                print(MENSAJE_ERROR)      
    elif otro_color == NO:
        print(f"Debe pagar: $ {precio1*metros_tela1}")
        print(f"Lleva {metros_tela1} metros de tela")
    else:
        print(MENSAJE_ERROR)      
else:
    print(MENSAJE_ERROR) 