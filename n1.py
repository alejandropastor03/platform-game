#Nivel 1

import pygame
from pygame import *
from typing import *

from niveles import Nivel
from plataformas import *

class Nivel_1 (Nivel):
    def __init__(self, jugador) -> None:
        super().__init__(jugador)
        self.imagen_fondo : Surface = pygame.image.load ("Nivel1\BackgroundColorGrass.png")
        self.limite_nivel = -2600

        #---Plataformas---
        HIERBA : Surface = pygame.image.load ("Nivel1\grass.png")
        HIERBA_CENTRO : Surface = pygame.image.load ("Nivel1\grassCenter.png")
        HIERBA_SALIENTE_IZQUIERDO : Surface = pygame.image.load ("Nivel1\grassCliffLeft.png")
        HIERBA_SALIENTE_DERECHO : Surface = pygame.image.load ("Nivel1\grassCliffRight.png")
        HIERBA_MITAD : Surface = pygame.image.load ("Nivel1\grassHalf.png")
        HIERBA_MITAD_IZQUIERDA : Surface = pygame.image.load ("Nivel1\grassHalfLeft.png")
        HIERBA_MITAD_MEDIO : Surface = pygame.image.load ("Nivel1\grassHalfMid.png")
        HIERBA_MITAD_DERECHA : Surface = pygame.image.load ("Nivel1\grassHalfRight.png")
        HIERBA_IZQUIERDA : Surface = pygame.image.load ("Nivel1\grassLeft.png")
        HIERBA_MEDIO : Surface = pygame.image.load ("Nivel1\grassMid.png")
        HIERBA_DERECHA : Surface = pygame.image.load ("Nivel1\grassRight.png")
        NAVE : Surface = pygame.image.load ("Nivel1\dino-spaceship-flying-game-character.png")
        AGUA : Surface = pygame.image.load ("Nivel1\liquidWater.png")
        AGUA_ARRIBA : Surface = pygame.image.load ("Nivel1\liquidWaterTop.png")
        PUENTE : Surface = pygame.image.load ("Nivel1\\bridgeLogs.png")
        PUERTA : Surface = pygame.image.load ("Nivel1\door_openMid.png")
        PUERTA_ARRIBA : Surface = pygame.image.load ("Nivel1\door_openTop.png")

        #Colocar las plataformas
        plataformas : List[Plataforma] = [[NAVE, - 450, - 41.5], [HIERBA_MITAD_IZQUIERDA, 850, 590], 
        [HIERBA_MITAD_DERECHA, 920, 590], [HIERBA_MITAD_IZQUIERDA, 1050, 540], [HIERBA_MITAD_DERECHA, 1120, 540],
        [HIERBA_MITAD_IZQUIERDA, 1250, 490], [HIERBA_MITAD_DERECHA, 1320, 490], [HIERBA_SALIENTE_IZQUIERDO, 1450, 440],
        [HIERBA_MEDIO, 1520, 440], [HIERBA_CENTRO, 1520, 510], [HIERBA_MEDIO, 1590, 440], [HIERBA_CENTRO, 1590, 510],
        [HIERBA_CENTRO, 1520, 580], [HIERBA_CENTRO, 1590, 580], [HIERBA_SALIENTE_DERECHO, 1660, 440],
        [AGUA, 1660, 580], [AGUA_ARRIBA, 1660, 520], [AGUA_ARRIBA, 1730, 520], [AGUA_ARRIBA, 1800, 520],
        [AGUA_ARRIBA, 1870, 520], [AGUA_ARRIBA, 1940, 520], [AGUA_ARRIBA, 2010, 520], [AGUA_ARRIBA, 2080, 520],
        [AGUA_ARRIBA, 2150, 520], [AGUA_ARRIBA, 2220, 520], [AGUA_ARRIBA, 2290, 520], [AGUA_ARRIBA, 2360, 520],
        [AGUA, 1730, 580], [AGUA, 1800, 580], [AGUA, 1870, 580], [AGUA, 1940, 580], [AGUA, 2010, 580], [AGUA, 2080, 580],
        [AGUA, 2150, 580], [AGUA, 2220, 580], [AGUA, 2290, 580], [AGUA, 2360, 580], [HIERBA_IZQUIERDA, 2420, 520],
        [HIERBA_CENTRO, 2420, 580], [HIERBA_MEDIO, 2490, 520], [HIERBA_CENTRO, 2490, 580], [HIERBA_DERECHA, 2560, 520],
        [HIERBA_CENTRO, 2560, 580], [HIERBA, 2810, 440], [HIERBA, 3060, 360], [HIERBA_IZQUIERDA, 3310, 280],
        [HIERBA_DERECHA, 3380, 280], [HIERBA_CENTRO, 3310, 340], [HIERBA_CENTRO, 3380, 340], [HIERBA_CENTRO, 3310, 400],
        [HIERBA_CENTRO, 3380, 400], [HIERBA_CENTRO, 3310, 460], [HIERBA_CENTRO, 3380, 460], [HIERBA_CENTRO, 3310, 520],
        [HIERBA_CENTRO, 3380, 520], [HIERBA_CENTRO, 3310, 590], [HIERBA_CENTRO, 3380, 590], [PUENTE, 3450, 280],
        [PUENTE, 3520, 280], [PUENTE, 3590, 280], [PUENTE, 3660, 280], [PUENTE, 3730, 280], [HIERBA_IZQUIERDA, 3800, 280],
        [HIERBA_MEDIO, 3870, 280], [HIERBA_CENTRO, 3800, 340], [HIERBA_CENTRO, 3870, 340], [HIERBA_CENTRO, 3800, 400],
        [HIERBA_CENTRO, 3870, 400], [HIERBA_CENTRO, 3800, 460], [HIERBA_CENTRO, 3870, 460], [HIERBA_CENTRO, 3800, 520],
        [HIERBA_CENTRO, 3870, 520], [HIERBA_CENTRO, 3800, 590], [HIERBA_CENTRO, 3870, 590], [HIERBA_DERECHA, 3940, 280],
        [HIERBA_CENTRO, 3940, 340], [HIERBA_CENTRO, 3940, 400], [HIERBA_CENTRO, 3940, 460], [HIERBA_CENTRO, 3940, 520],
        [HIERBA_CENTRO, 3940, 590], [PUERTA, 3870, 210], [PUERTA_ARRIBA, 3870, 140]]

        for plataforma in plataformas:
            bloque : Plataforma = Plataforma (plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add (bloque)

        #Plataformas móviles
        plataforma_movil_1 : Plataforma_movil = Plataforma_movil (HIERBA_MITAD_IZQUIERDA)
        plataforma_movil_1.rect.x = 1880
        plataforma_movil_1.rect.y = 320
        plataforma_movil_1.perimetro_arriba = 150
        plataforma_movil_1.perimetro_abajo = 480
        plataforma_movil_1.cambio_y = -1  #Si se aumenta la velocidad, habria que aumentar el salto,
        #o si no el personaje no será capaz de saltar cuando la plataforma baje
        plataforma_movil_1.jugador = jugador
        plataforma_movil_1.nivel = self
        self.lista_plataformas.add (plataforma_movil_1)

        plataforma_movil_2 : Plataforma_movil = Plataforma_movil (HIERBA_MITAD_DERECHA)
        plataforma_movil_2.rect.x = 1950
        plataforma_movil_2.rect.y = 320
        plataforma_movil_2.perimetro_arriba = 150
        plataforma_movil_2.perimetro_abajo = 480
        plataforma_movil_2.cambio_y = -1
        plataforma_movil_2.jugador = jugador
        plataforma_movil_2.nivel = self
        self.lista_plataformas.add (plataforma_movil_2)

        plataforma_movil_3 : Plataforma_movil = Plataforma_movil (HIERBA_MITAD_IZQUIERDA)
        plataforma_movil_3.rect.x = 2200
        plataforma_movil_3.rect.y = 200
        plataforma_movil_3.perimetro_arriba = 150
        plataforma_movil_3.perimetro_abajo = 480
        plataforma_movil_3.cambio_y = 1
        plataforma_movil_3.jugador = jugador
        plataforma_movil_3.nivel = self
        self.lista_plataformas.add (plataforma_movil_3)

        plataforma_movil_4 : Plataforma_movil = Plataforma_movil (HIERBA_MITAD_DERECHA)
        plataforma_movil_4.rect.x = 2270
        plataforma_movil_4.rect.y = 200
        plataforma_movil_4.perimetro_arriba = 150
        plataforma_movil_4.perimetro_abajo = 480
        plataforma_movil_4.cambio_y = 1
        plataforma_movil_4.jugador = jugador
        plataforma_movil_4.nivel = self
        self.lista_plataformas.add (plataforma_movil_4)
