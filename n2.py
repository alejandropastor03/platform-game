#Nivel 2

import pygame
from pygame import *
from typing import *

from niveles import Nivel
from plataformas import *

class Nivel_2 (Nivel):
    def __init__(self, jugador) -> None:
        super().__init__(jugador)
        self.imagen_fondo : Surface = pygame.image.load ("Nivel2\BackgroundCastles.png")
        self.limite_nivel : int = - 600

        #---Plataformas---
        NIEVE : Surface = pygame.image.load ("Nivel2\snow.png")
        NIEVE_CENTRO_REDONDEADO : Surface = pygame.image.load ("Nivel2\snowCenter_rounded.png")
        NIEVE_CENTRO : Surface = pygame.image.load ("Nivel2\snowCenter.png")
        NIEVE_SALIENTE_IZQUIERDO : Surface = pygame.image.load ("Nivel2\snowCliffLeft.png")
        NIEVE_SALIENTE_DERECHO : Surface = pygame.image.load ("Nivel2\snowCliffRight.png")
        NIEVE_MITAD : Surface = pygame.image.load ("Nivel2\snowHalf.png")
        NIEVE_MITAD_IZQUIERDA : Surface = pygame.image.load ("Nivel2\snowHalfLeft.png")
        NIEVE_MITAD_MEDIO : Surface = pygame.image.load ("Nivel2\snowHalfMid.png")
        NIEVE_MITAD_DERECHA : Surface = pygame.image.load ("Nivel2\snowHalfRight.png")
        NIEVE_IZQUIERDA : Surface = pygame.image.load ("Nivel2\snowLeft.png")
        NIEVE_MEDIO : Surface = pygame.image.load ("Nivel2\snowMid.png")
        NIEVE_DERECHA : Surface = pygame.image.load ("Nivel2\snowRight.png")
        PUERTA : Surface = pygame.image.load ("Nivel1\door_openMid.png")
        PUERTA_ARRIBA : Surface = pygame.image.load ("Nivel1\door_openTop.png")

        #Colocar las plataformas
        plataformas : List = [[PUERTA, -5, 580], [PUERTA_ARRIBA, -5, 510], [NIEVE, 500, 510], [NIEVE, 650, 420]]
        
        for plataforma in plataformas:
            bloque : Plataforma = Plataforma (plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add (bloque)