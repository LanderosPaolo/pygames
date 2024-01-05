import pygame
from pygame.locals import *
import random
import math
from pygame import mixer

# Inicializar a pygame
pygame.init()


# --> Configuracion de pantalla <--
# Configuración tamaño de pantalla
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
# Especificación de título
pygame.display.set_caption('Space Invaders')
# Icono para la pantalla
icono = pygame.image.load("10.Programa el juego invasión espacial/proyecto/imgs/ovni.png")
pygame.display.set_icon(icono)
# ruta a la imagen que se usara de fondo
ruta_img = "10.Programa el juego invasión espacial/proyecto/imgs/backgroundSpace.jpg"
bg_img = pygame.image.load(ruta_img)
bg_img = pygame.transform.scale(bg_img,(width,height))
# --> Fin configuracion de pantalla <--

# ---> Musica <--
mixer.music.load("10.Programa el juego invasión espacial/proyecto/audio/MusicaFondo.mp3")
mixer.music.play(-1)
# ---> Fin musica <--

# --> Nave Jugador <--
# Cargar imagen que hara de nave del jugador
ruta_nave_jugador = "10.Programa el juego invasión espacial/proyecto/imgs/jugador.png"
nave_jugador = pygame.image.load(ruta_nave_jugador)
# Posicion de la nave del jugador
nave_jugador_x = 608
nave_jugador_y = 640
# velocidad de la nave
movimiento_nave_jugador = 0
# --> Fin nave jugador <--

# --> Crear mas enemigos <--
nave_enemigo = []
nave_enemigo_x = []
nave_enemigo_y = []
movimiento_enemigo_x = []
movimiento_enemigo_y = []
cantidad = 10
# --> Fin naves enemigas <--

for e in range(cantidad):
    # --> Nave enemiga <--
    # Cargar imagen de nave enemiga
    ruta_nave_enemigo = "10.Programa el juego invasión espacial/proyecto/imgs/enemigo.png"
    nave_enemigo.append(pygame.image.load(ruta_nave_enemigo))
    # Posicion de las naves enemigas
    nave_enemigo_x.append(random.randint(0, 1216))
    nave_enemigo_y.append(random.randint(50, 400))
    movimiento_enemigo_x.append(3)
    movimiento_enemigo_y.append(50)
    # --> Fin nave enemiga <--


# --> Disparo <--
# Cargar imagen de disparo
balas = []
ruta_disparo = "10.Programa el juego invasión espacial/proyecto/imgs/disparo.png"
disparo = pygame.image.load(ruta_disparo)
bala_x = 0
bala_y = 640
movimiento_y = 1
visible = False
# --> Fin disparo <--


#  --> Puntaje <--
puntaje = 0
texto_x = 10
texto_y = 10
fuente = pygame.font.SysFont('arial', 32)

def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    window.blit(texto, (x, y))
# --> Fin puntaje <--

# Texto fin del juego
fuente_final = pygame.font.SysFont('arial', 40)

def texto_final():
    mi_fuente_final = fuente_final.render("Game Over", True, pygame.Color('red'))
    window.blit(mi_fuente_final, (520, 300))


# Funcion jugador
def jugador(x, y):
    window.blit(nave_jugador, (x, y))

# Funcion enemigo
def enemigo(x, y, ene):
    window.blit(nave_enemigo[ene], (x, y))

# Funcion bala
def disparar(x, y):
    global visible
    visible = True
    window.blit(disparo, (x + 16, y + 10))

# Funcion para detectar colisiones
def colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False

# Bucle while para mantener la pantalla abierta hasta que se presione el boton cerrar
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movimiento de la nave en el juego
        if event.type == pygame.KEYDOWN:
            if event.key == K_d:
                movimiento_nave_jugador = 5
            if event.key == K_a:
                movimiento_nave_jugador = -5
            if event.key == K_SPACE:
                # sonido de disparo
                sonido_disparo = mixer.Sound('10.Programa el juego invasión espacial/proyecto/audio/Disparo.mp3')
                sonido_disparo.play()
                nueva_bala = {
                    "x": nave_jugador_x,
                    "y": nave_jugador_y,
                    "velocidad": -5
                }
                balas.append(nueva_bala)

        if event.type == pygame.KEYUP:           
            if event.key == pygame.K_d or event.key == pygame.K_a:
                movimiento_nave_jugador = 0

    window.blit(bg_img, (0, 0))
    # Ubicacion del jugador
    nave_jugador_x += movimiento_nave_jugador


    # --> Limitar bordes jugador <--
    if nave_jugador_x <= 0:
        nave_jugador_x = 0
    elif nave_jugador_x >= 1216:
        nave_jugador_x = 1216
    # --> Fin limitar bordes jugador <--


    # Ubicacion del enemigo
    for e in range(cantidad):
        
        # Fin del juego
        if nave_enemigo_y[e] > 550:
            for k in range(cantidad):
                nave_enemigo_y[k] = 1000
            texto_final()
            break

        nave_enemigo_x[e] += movimiento_enemigo_x[e]

        # --> Limitar bordes enemigo <--
        if nave_enemigo_x[e] <= 0:
            movimiento_enemigo_x[e] = 3
            nave_enemigo_y[e] += movimiento_enemigo_y[e]
        elif nave_enemigo_x[e] >= 1216:
            movimiento_enemigo_x[e] = -5
            nave_enemigo_y[e] += movimiento_enemigo_y[e]
        # --> Fin limitar bordes jugador <--

            # Colision
        for bala in balas:
            colisionado = colision(nave_enemigo_x[e], nave_enemigo_y[e], bala["x"], bala["y"])
            if colisionado:
                sonido_colision = mixer.Sound('10.Programa el juego invasión espacial/proyecto/audio/Golpe.mp3')
                balas.remove(bala)
                # bala_y = 640
                # visible = False
                puntaje += 10
                nave_enemigo_x[e] = random.randint(0, 1216)
                nave_enemigo_y[e] = random.randint(50, 400)
                break

        enemigo(nave_enemigo_x[e], nave_enemigo_y[e], e)


    # --> Movimiento bala <--
    for bala in balas:
        bala["y"] += bala["velocidad"]
        window.blit(disparo, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)
    for bala in balas:
        bala["y"] += bala["velocidad"]
        window.blit(disparo, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)


    jugador(nave_jugador_x, nave_jugador_y)

    mostrar_puntaje(texto_x, texto_y)

    pygame.display.flip()
    pygame.display.update()

    # Controlar la cantidad de fotogramas
    clock.tick(60)