import pygame
from pygame import *
from typing import *
import datetime
import time

import constantes
import n1
import n2
from jugador import Jugador
from menu import Menu
from niveles import Nivel

def guardar_datos (segundos : float) -> None:
    ahora : datetime.date = datetime.datetime.now ()
    entrada = open ("Partidas_anteriores.txt", "r+", encoding = "UTF-8")
    n_lineas : int = 0
    for i in entrada:
        n_lineas += 1
    if n_lineas == 0:
        partida : int = 0
    else:
        partida : int = n_lineas // 4
    minutos : int = segundos // 60
    segundos : int = segundos % 60
    print (str (partida), file = entrada)
    print (str (ahora.day) + "/" + str (ahora.month) + "/" + str (ahora.year), file = entrada)
    print (str (round (minutos, 2)) + " : " + str (round (segundos, 2)), file = entrada)
    print(file = entrada)
    entrada.close ()

def main () -> None:

    menu : Menu = Menu ()
    menu.ejecutar_menu ()

    pygame.init ()
    #Creación de la pantalla, titulo e icono del juego
    pantalla : Surface = pygame.display.set_mode ((constantes.ANCHO, constantes.ALTO))
    pygame.display.set_caption ("Juego de plataformas")

    #Creación del jugador
    jugador : Jugador = Jugador ()
    
    #Creación de los niveles
    lista_niveles : List = [n1.Nivel_1 (jugador), n2.Nivel_2 (jugador)]
    nivel_actual_nº : int = 0
    nivel_actual : Nivel = lista_niveles[nivel_actual_nº]

    lista_sprites_activos = pygame.sprite.Group ()
    jugador.nivel = nivel_actual

    jugador.rect.x = 350
    jugador.rect.y = constantes.ALTO - jugador.rect.height
    lista_sprites_activos.add (jugador)

    #Desarrollo del juego
    comienzo = time.time () #Para medir la duracion de la partida

    done : bool = False
    clock = pygame.time.Clock ()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jugador.mover_derecha ()
                elif event.key == pygame.K_LEFT:
                    jugador.mover_izquierda ()
                if event.key == pygame.K_UP:
                    jugador.salto ()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and jugador.cambio_x < 0:
                    jugador.parar ()
                elif event.key == pygame.K_RIGHT and jugador.cambio_x > 0:
                    jugador.parar ()

        lista_sprites_activos.update ()
        nivel_actual.update ()

        #Mover la camara con el movimiento del jugador
        if jugador.rect.x >= 600:
            diferencia : float = jugador.rect.x - 600
            jugador.rect.x = 600
            nivel_actual.desplazar_mundo (-diferencia)
        
        if jugador.rect.x <= 300:
            diferencia : float = 300 - jugador.rect.left
            jugador.rect.x = 300
            nivel_actual.desplazar_mundo (diferencia)

        #Cambiar de nivel
        posicion_actual : int = jugador.rect.x + nivel_actual.desplazamiento_mundo
        if posicion_actual < nivel_actual.limite_nivel:
            jugador.rect.x = 120
            if nivel_actual_nº < len (lista_niveles) - 1:
                nivel_actual_nº += 1
                nivel_actual = lista_niveles[nivel_actual_nº]
                jugador.nivel = nivel_actual
            else:
                #El juego termina con un cierre de la pantalla, falta pantalla de fin
                final = time.time ()
                guardar_datos (final - comienzo)
                exit ()

        #Dibujar en pantalla
        nivel_actual.draw (pantalla)
        lista_sprites_activos.draw (pantalla)

        clock.tick(60)
        pygame.display.flip()
    pygame.quit ()

if __name__ == "__main__": 
    main ()