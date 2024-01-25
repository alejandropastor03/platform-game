#Nivel 3

import pygame
from pygame import *
from typing import *

from niveles import Nivel
from plataformas import *

class Nivel_3 (Nivel):
    def __init__(self, jugador) -> None:
        super().__init__(jugador)
        self.imagen_fondo : Surface = pygame.image.load ("Nivel3\BackgroundColorDesert.png")

        #---Plataformas---
        TARTA : Surface = pygame.image.load ("Nivel3\cake.png")
        TARTA_CENTRO_REDONDEADO : Surface = pygame.image.load ("Nivel3\cakeCenter_rounded.png")
        TARTA_CENTRO : Surface = pygame.image.load ("Nivel3\cakeCenter.png")
        TARTA_SALIENTE_IZQUIERDO : Surface = pygame.image.load ("Nivel3\cakeCliffLeft.png")
        TARTA_SALIENTE_DERECHO : Surface = pygame.image.load ("Nivel3\cakeCliffRight.png")
        TARTA_MITAD : Surface = pygame.image.load ("Nivel3\cakeHalfAlt.png")
        TARTA_MITAD_IZQUIERDA : Surface = pygame.image.load ("Nivel3\cakeHalfAltLeft.png")
        TARTA_MITAD_MEDIO : Surface = pygame.image.load ("Nivel3\cakeHalfAltMid.png")
        TARTA_MITAD_DERECHA : Surface = pygame.image.load ("Nivel3\cakeHalfAltRight.png")
        TARTA_IZQUIERDA : Surface = pygame.image.load ("Nivel3\cakeLeft.png")
        TARTA_MEDIO : Surface = pygame.image.load ("Nivel3\cakeMid.png")
        TARTA_DERECHA : Surface = pygame.image.load ("Nivel3\cakeRight.png")
        CHOCO_IZQUIERDA : Surface = pygame.image.load ("Nivel3\chocoHalfAltLeft.png")
        CHOCO_MEDIO : Surface = pygame.image.load ("Nivel3\chocoHalfAltMid.png")
        CHOCO_DERECHA : Surface = pygame.image.load ("Nivel3\chocoHalfAltRight.png")

        #Colocar las plataformas
        plataformas : List = []
        
        for plataforma in plataformas:
            bloque : Plataforma = Plataforma (plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add (bloque)