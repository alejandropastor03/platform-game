#Este modulo contiene todo lo referido a las plataformas sobre las que el jugador puede saltar

import pygame
from pygame import *
from typing import *

class Plataforma (pygame.sprite.Sprite):
    def __init__ (self, imagen : Surface) -> None:
        super().__init__()
        self.image : Surface = imagen
        self.rect : Rect = self.image.get_rect ()
    
class Plataforma_movil (Plataforma):
    def __init__ (self, imagen : Surface) -> None:
        super().__init__(imagen)
        self.cambio_x : float = 0
        self.cambio_y : float = 0
        self.perimetro_arriba : float = 0
        self.perimetro_abajo : float = 0
        self.perimetro_izquierda : float = 0
        self.perimetro_derecha : float = 0
        self.nivel = None
        self.jugador = None

    def update (self) -> None:
        #Mover derecha/izquierda
        self.rect.x += self.cambio_x

        #Choque con el jugador
        choque : bool = pygame.sprite.collide_rect (self, self.jugador)
        if choque:
            if self.cambio_x < 0:
                self.jugador.rect.right = self.rect.left
            else:
                self.jugador.rect.left = self.rect.right

        #Mover arriba/abajo
        self.rect.y += self.cambio_y
        choque : bool = pygame.sprite.collide_rect (self, self.jugador)
        if choque:
            if self.cambio_y < 0:
                self.jugador.rect.bottom = self.rect.top
            else:
                self.jugador.rect.top = self.rect.bottom

        #Cambio de direccion
        if self.rect.bottom > self.perimetro_abajo or self.rect.top < self.perimetro_arriba:
            self.cambio_y *= -1
        posicion_x : float = self.rect.x - self.nivel.desplazamiento_mundo
        if posicion_x < self.perimetro_izquierda or posicion_x > self.perimetro_derecha:
            self.cambio_x *= -1