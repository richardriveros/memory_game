#pgzero

 #idea : memory game que cada vez que acertes una pareja de cartas que coincidan, te den una cantidad de puntos dependiendo de la carta
 #y con los puntos puedas comprar comodines para eliminar filas, u aumentar el temporizador, cada vez que aciertas todas las parejas subes de nivel y 
 #se agregan mas cartas para aumentar la dificultad hasta un cierto nivel.

#bounce_start_end

"""
BACKLOG:

TO-DO: AGREGAR PUNTAJE:
        -> CREAR VARIABLE GLOBAL PUNTAJE Y OTRA PARA UN TIMER (2')
        -> LA PUNTUACION EMPIEZA EN 300 PTOS Y CADA SEGUNDO SE PIERDEN DOS PUNTOS
           Y CADA PAREJA ERRONEA RESTA 20 PUNTOS
          
DISEÑAR: PAREJAS???

3 ESTADOS: 0 CARTAS / 1 CARTA / 2 CARTAS

lista: "pareja_actual"

¿cuántos seleccioné? -> len(pareja_actual)

    -> 2 CARTAS:
        -> COINCIDEN: LAS "DESACTIVO" // LAS ELIMINO
            >> TO-DO: AGREGAR mecanica de desactivar cartas
            -> vacio lista pareja
        
        -> NO COINCIDEN:
            -> restar 20 puntos
            -> poner boca abajo las cartas
            -> liberar la pareja

TO-DO: AGREGAR BOTONES:
        -> TIENDA
        -> SALIR
        -> REINICIAR



"""

WIDTH = 800
HEIGHT = 600

FPS = 30
TITLE = "SKZ MEMORY"

"""
bokkari = Actor ("tarjeta1") 
jiniret = Actor ("tarjeta2")
foxi.ny = Actor ("tarjeta3")
dwaekki = Actor ("tarjeta4")
wolfchan = Actor ("tarjeta5")
leebit = Actor ("tarjeta6")
quokka = Actor ("tarjeta7")
puppym = Actor ("tarjeta8")
"""
#variables

puntuacion = 0




lista_cartas = []

DIST_ENTRE_CARTAS = 16
"""
Carta:
Pos.x = WIDTH - (
                (DIST_ENTRE_CARTAS * (columna_actual + 1)) +
                (ref_carta.width * (columna_actual - 1)) +
                (ref_carta.width / 2)
                ) 

pos.y = HEIGHT - (
                 (DIST_ENTRE_CARTAS * (fila_actual + 1)) +
                 (ref_carta.height * (fila_actual - 1)) +
                 (ref_carta.height /2)
                 )
"""

pos_cartas = { 1 : () }


ref_carta = Actor("dorso")



for fila_actual in range(4):
    for columna_actual in range(4):
        temp_x = WIDTH - (
                         (DIST_ENTRE_CARTAS * (columna_actual + 1)) +
                         (ref_carta.width * columna_actual) +
                         (ref_carta.width / 2)
                         )
                             
        temp_y = HEIGHT - (
                          (DIST_ENTRE_CARTAS * (fila_actual + 1)) +
                          (ref_carta.height * fila_actual) +
                          (ref_carta.height /2)
                          )
        nva_carta = Actor("dorso", center=(temp_x, temp_y))
        nva_carta.esta_boca_arriba = False
        nva_carta.esta_activa = True
        nva_carta.seleccionada = False
        lista_cartas.append(nva_carta)

def draw():
    screen.fill((80, 80, 80))
    for carta in lista_cartas:
        carta.draw()
        
def on_mouse_down(button, pos):
    
    for carta in lista_cartas:
        if carta.collidepoint(pos) and carta.esta_activa:
            
            # To-do: agregar mecáncia de seleccionar/des-seleccionar
            # To-do: agregar lógica de agregar a pareja_actual
            
            carta.esta_boca_arriba  = not carta.esta_boca_arriba
            if carta.esta_boca_arriba:
                #carta.image = "temp"
                carta.image = "temp"
            else:
                carta.image = "dorso"
