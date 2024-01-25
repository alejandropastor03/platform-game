#Este módulo contiene los niveles del juego

import pygame
from pygame import *
from typing import *

import constantes

class Nivel ():
    #Clase padre de la que heredarn atributos las clases propias de cada nivel
    def __init__ (self, jugador) -> None:
        self.lista_plataformas : List = None
        self.imagen_fondo : List = None
        self.desplazamiento_mundo : float = 0
        self.limite_nivel : float = -1000
        self.lista_plataformas = pygame.sprite.Group ()
        self.jugador = jugador

    def update (self) -> None:
        self.lista_plataformas.update ()

    def draw (self, pantalla : Surface) -> None:
        #Fondo repetido
        pantalla.fill (constantes.AZUL)
        for i in range (-1, 10):
            pantalla.blit (self.imagen_fondo, ((self.desplazamiento_mundo // 3) + 1024 * i, 0))

        #Listas de sprites
        self.lista_plataformas.draw (pantalla)

    def desplazar_mundo (self, desplazamiento_x : float) -> None:
        self.desplazamiento_mundo += desplazamiento_x
        for plataforma in self.lista_plataformas:
            plataforma.rect.x += desplazamiento_x