#Este módulo contiene todo lo referente al personaje controlado por el jugador

import pygame
from pygame import *
from typing import *
import os

from constantes import *
from niveles import Nivel
import plataformas

class Jugador (pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        #Atributos de velocidad
        self.cambio_x : float = 0
        self.cambio_y : float = 0

        #Cambiar imagenes cuando el personaje se mueve
        self.frames_andados_d : List[Surface] = []
        self.frames_andados_i : List[Surface] = []

        #Dirección hacia la que anda (Derecha por defecto)
        self.direccion : str = "D"

        #Lista de sprites contra los que se puede chochar
        self.nivel : Nivel = None

        #Animación de andar
        #Derecha
        directorio_original : str = os.getcwd()
        os.chdir ("Movimientos")
        for i in os.listdir ():
            if i != "p2_front.png":
                imagen : Surface = pygame.image.load (i)
                self.frames_andados_d += [imagen]
        os.chdir (directorio_original)
        #Izquierda
        for i in self.frames_andados_d:
            i = pygame.transform.flip (i, True, False)
            self.frames_andados_i += [i]

        #Imagen inicial
        self.image : Surface = pygame.image.load ("Movimientos\p2_front.png")

        #Referencia para el rectangulo de la imagen
        self.rect : Rect = self.image.get_rect ()

    def calcular_gravedad (self) -> None:
        if self.cambio_y == 0:
            self.cambio_y = 1
        else:
            self.cambio_y += 0.35

        #Comprobar si el jugador está en el suelo
        if self.rect.y >= ALTO - self.rect.height and self.cambio_y >= 0:
            self.cambio_y = 0
            self.rect.y = ALTO - self.rect.height

    def update (self) -> None:
        self.calcular_gravedad ()

        #Mover izquierda/derecha
        self.rect.x += self.cambio_x
        posicion : float = self.rect.x + self.nivel.desplazamiento_mundo
        if self.direccion == "D":
            frame : int = (posicion // 30) % len (self.frames_andados_d)
            self.image = self.frames_andados_d[frame]
        else:
            frame : int = (posicion // 30) % len (self.frames_andados_i)
            self.image = self.frames_andados_i[frame]

        #Comprobar si choca con alguna plataforma (horizontal)
        lista_bloques = pygame.sprite.spritecollide (self, self.nivel.lista_plataformas, False)
        for bloque in lista_bloques:
            if self.cambio_x > 0:
                self.rect.right = bloque.rect.left
            elif self.cambio_x < 0:
                self.rect.left = bloque.rect.right
        #Mover arriba/abajo
        self.rect.y += self.cambio_y

        #Comprobar si choca con alguna plataforma (vertical)
        lista_bloques = pygame.sprite.spritecollide (self, self.nivel.lista_plataformas, False)
        for bloque in lista_bloques:
            if self.cambio_y > 0:
                self.rect.bottom = bloque.rect.top
            elif self.cambio_y < 0:
                self.rect.top = bloque.rect.bottom
            self.cambio_y = 0
            if isinstance (bloque, plataformas.Plataforma_movil):
                self.rect.x += bloque.cambio_x


    def salto (self) -> None:
        self.rect.y += 2
        lista_bloques = pygame.sprite.spritecollide (self, self.nivel.lista_plataformas, False)
        self.rect.y -= 2

        if len (lista_bloques) > 0 or self.rect.bottom >= ALTO:
            self.cambio_y = -10

    def mover_izquierda (self) -> None:
        self.cambio_x = -6.5
        self.direccion = "I"

    def mover_derecha (self) -> None:
        self.cambio_x = 6.5
        self.direccion = "D"

    def parar (self) -> None:
        self.cambio_x = 0