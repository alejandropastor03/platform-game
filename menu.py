#Este módulo contiene todo lo relaccionado con el menú que aparece al inciar el juego

import pygame
from pygame import *
from typing import *
from pygame.font import Font

from constantes import *

def formato_texto (mensaje : str, fuente : str, tamaño : float, color : Tuple) -> Font:
    letra : Font = pygame.font.Font (fuente, tamaño)
    return letra.render (mensaje, 0, color)

def extraer_partidas (archivo : str) -> List[List[str]]:
    entrada = open (archivo, "r", encoding = "UTF-8")
    lista : List[str] = []
    lista_completa : List[List[str]] = []
    for linea in entrada:
        if linea != "\n":
            lista += [linea[:-1]]
        else:
            lista_completa += [lista]
            lista = []
    lista_completa += [lista]
    entrada.close ()
    return lista_completa

class Menu ():
    def __init__(self) -> None:
        self.menu : bool = True
        self.lista_opciones : list = ["INICIAR JUEGO", "CONTROLES", "PARTIDAS ANTERIORES", "CREDITOS", "SALIR"]
        self.seleccionado : str = self.lista_opciones[0]
        self.seleccionado_numero = 0
        self.clock = pygame.time.Clock ()
        self.pantalla : Surface = pygame.display.set_mode ((625, 350))
        self.fondo : Surface = pygame.image.load ("Menu\\fondo_menu.jpg")
        self.fondo = pygame.transform.scale (self.fondo, (625, 350))
        self.lista_partidas_anteriores : List[List[str]] = extraer_partidas ("Partidas_anteriores.txt")

    def existe_partida (self, numero : int, lista : List[List[str]]) -> bool:
        existe : bool = False
        i : int = 0
        while i < len (lista) and not existe:
            if int(lista[i][0]) == numero:
                existe = True
            else:
                i += 1
        return existe

    def controles (self) -> None:
        pygame.display.set_caption ("Controles")
        control : bool = True
        while control:
            for event in pygame.event.get ():
                if event.type == pygame.QUIT:
                    exit ()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        control = False
            #Cambiar el fondo
            fondo_controles : Surface = pygame.image.load ("Menu\\fondo_controles.jpg")
            fondo_controles = pygame.transform.scale (fondo_controles, (625, 350))
            self.pantalla.blit (fondo_controles, (0, 0))

            lista_textos : List[str] = ["Pulsa ", " para ", "moverte hacia la ", "izquierda", "derecha", "saltar", "volver al menu"]
            for i in range (0, 7):
                lista_textos[i] = formato_texto (lista_textos[i], "Menu\Bubblegum.ttf", 25, NEGRO)

            #Imagenes de la teclas
            tecla_derecha : Surface = pygame.image.load ("Menu\g14209.png")
            tecla_derecha = pygame.transform.scale (tecla_derecha, (25, 25))
            tecla_izquierda : Surface = pygame.image.load ("Menu\g14134.png")
            tecla_izquierda = pygame.transform.scale (tecla_izquierda, (25, 25))
            tecla_arriba : Surface = pygame.image.load ("Menu\g14228.png")
            tecla_arriba = pygame.transform.scale (tecla_arriba, (25, 25))
            tecla_espacio : Surface = pygame.image.load ("Menu\g14253.png")
            tecla_espacio = pygame.transform.scale (tecla_espacio, (120, 25))

            #Colocar elementos en la pantalla
            lista_elementos_pantalla : List[Surface] = [[lista_textos[0], (50, 15)], [tecla_derecha, (130, 15)],
            [lista_textos[1], (160, 15)], [lista_textos[2], (240, 15)], [lista_textos[4], (470, 15)],
            [lista_textos[0], (50, 45)], [tecla_izquierda, (130, 45)], [lista_textos[1], (160, 45)],
            [lista_textos[2], (240, 45)], [lista_textos[3], (470, 45)], [lista_textos[0], (180, 75)], 
            [tecla_arriba, (260, 75)], [lista_textos[1], (290, 75)], [lista_textos[5], (370, 75)],
            [lista_textos[6], (140, 270)], [tecla_espacio, (350, 270)]]
            for elemento in lista_elementos_pantalla:
                self.pantalla.blit (elemento[0], elemento[1])

            pygame.display.flip()

    def creditos (self) -> None:
        pygame.display.set_caption ("Creditos")
        creditos : bool = True
        while creditos:
            for event in pygame.event.get ():
                if event.type == pygame.QUIT:
                    exit ()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        creditos = False
            #Cambiar el fondo
            fondo_creditos : Surface = pygame.image.load ("Menu\\fondo_creditos.jpg")
            fondo_creditos = pygame.transform.scale (fondo_creditos, (625, 350))
            self.pantalla.blit (fondo_creditos, (0, 0))

            #Colocar elementos en la pantalla
            tecla_espacio : Surface = pygame.image.load ("Menu\g14253.png")
            tecla_espacio = pygame.transform.scale (tecla_espacio, (120, 25))
            texto_salir : Font = formato_texto ("volver al menu", "Menu\Bubblegum.ttf", 20, BLANCO)
            texto_creditos_1 : Font = formato_texto ("CREADO POR ", "Menu\Bubblegum.ttf", 25, BLANCO)
            texto_creditos_2 : Font = formato_texto ("ALEJANDRO PASTOR MEMBRADO", "Menu\Bubblegum.ttf", 35, BLANCO)
            self.pantalla.blit (texto_salir, (140,270))
            self.pantalla.blit (tecla_espacio, (310, 270))
            self.pantalla.blit (texto_creditos_1, (230, 30))
            self.pantalla.blit (texto_creditos_2, (80, 70))

            self.clock.tick(60)
            pygame.display.flip()

    def partidas_anteriores (self) -> None:
        pygame.display.set_caption ("Partidas anteriores")
        p_anteriores : bool = True
        nº_partida : int = 0
        while p_anteriores:
            for event in pygame.event.get ():
                if event.type == pygame.QUIT:
                    exit ()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        p_anteriores = False
                    if event.key == pygame.K_LEFT:
                        if nº_partida > 0:
                            nº_partida -= 1
                    if event.key == pygame.K_RIGHT:
                        if nº_partida < len (self.lista_partidas_anteriores) - 1:
                            nº_partida += 1
                    if event.key == pygame.K_a:
                      numero : int = int (input ("Introduzca un número de partida: "))
                      if self.existe_partida (numero, self.lista_partidas_anteriores):
                        nº_partida = numero
            
            #Cambiar el fondo
            fondo_anteriores : Surface = pygame.image.load ("Menu\\fondo_anteriores.jpg")
            fondo_anteriores = pygame.transform.scale (fondo_anteriores, (625, 350))
            cuadro : Surface = pygame.image.load ("Menu\cuadro.jpg")
            cuadro = pygame.transform.scale (cuadro, (400, 250))
            self.pantalla.blit (fondo_anteriores, (0, 0))
            self.pantalla.blit (cuadro, (112.5, 50))

            #Colocar elementos en la pantalla
            texto_salir : Font = formato_texto ("volver al menu", "Menu\Bubblegum.ttf", 20, BLANCO)
            tecla_espacio : Surface = pygame.image.load ("Menu\g14253.png")
            tecla_espacio = pygame.transform.scale (tecla_espacio, (120, 25))
            tecla_derecha : Surface = pygame.image.load ("Menu\g14209.png")
            tecla_derecha = pygame.transform.scale (tecla_derecha, (50, 50))
            tecla_izquierda : Surface = pygame.image.load ("Menu\g14134.png")
            tecla_izquierda = pygame.transform.scale (tecla_izquierda, (50, 50))
            self.pantalla.blit (texto_salir, (140,310))
            self.pantalla.blit (tecla_espacio, (310, 310))
            self.pantalla.blit (tecla_derecha, (550, 150))
            self.pantalla.blit (tecla_izquierda, (25, 150))

            #Input
            texto_input : Font = formato_texto ("presione A para buscar una partida determinada por consola",\
            "Menu\Bubblegum.ttf", 17, BLANCO)
            self.pantalla.blit (texto_input, (40, 20))

            #Informacion de las partidas
            lista_textos : List[str] = self.lista_partidas_anteriores[nº_partida]
            texto_numero : Font = formato_texto ("partida " + str (lista_textos[0]), "Menu\Bubblegum.ttf", 30, NEGRO)
            texto_fecha : Font = formato_texto ("fecha -> " + str (lista_textos[1]), "Menu\Bubblegum.ttf", 25, NEGRO)
            texto_tiempo : Font = formato_texto ("duracion -> " + str (lista_textos[2]), "Menu\Bubblegum.ttf", 20, NEGRO)
            self.pantalla.blit (texto_numero, (230, 100))
            self.pantalla.blit (texto_fecha, (170, 150))
            self.pantalla.blit (texto_tiempo, (170, 200))

            self.clock.tick(60)
            pygame.display.flip()

    def update (self) -> None:
        if self.seleccionado_numero == 0:
            self.texto_iniciar : Font = formato_texto (self.lista_opciones[0], "Menu\stocky.ttf", 30, AZUL)
        else:
            self.texto_iniciar : Font = formato_texto (self.lista_opciones[0], "Menu\stocky.ttf", 25, BLANCO)
        if self.seleccionado_numero == 1:
            self.texto_control : Font = formato_texto (self.lista_opciones[1], "Menu\stocky.ttf", 30, AZUL)
        else:
            self.texto_control : Font = formato_texto (self.lista_opciones[1], "Menu\stocky.ttf", 25, BLANCO)
        if self.seleccionado_numero == 2:
            self.texto_anteriores : Font = formato_texto (self.lista_opciones[2], "Menu\stocky.ttf", 30, AZUL)
        else:
            self.texto_anteriores : Font = formato_texto (self.lista_opciones[2], "Menu\stocky.ttf", 25, BLANCO)
        if self.seleccionado_numero == 3:
            self.texto_creditos : Font = formato_texto (self.lista_opciones[3], "Menu\stocky.ttf", 30, AZUL)
        else:
            self.texto_creditos : Font = formato_texto (self.lista_opciones[3], "Menu\stocky.ttf", 25, BLANCO)
        if self.seleccionado_numero == 4:
            self.texto_salir : Font = formato_texto (self.lista_opciones[4], "Menu\stocky.ttf", 30, AZUL)
        else:
            self.texto_salir : Font = formato_texto (self.lista_opciones[4], "Menu\stocky.ttf", 25, BLANCO)

    def ejecutar_menu (self) -> None:
        pygame.init ()
        pygame.font.init ()
        pygame.display.set_caption ("Menu principal")
        while self.menu:
            for event in pygame.event.get ():
                if event.type == pygame.QUIT:
                    exit ()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.seleccionado_numero > 0:
                            self.seleccionado_numero -= 1
                            self.seleccionado = self.lista_opciones[self.seleccionado_numero]
                    if event.key == pygame.K_DOWN:
                        if self.seleccionado_numero < 4:
                            self.seleccionado_numero += 1
                            self.seleccionado = self.lista_opciones[self.seleccionado_numero]
                    if event.key == pygame.K_RETURN:
                        if self.seleccionado == "INICIAR JUEGO":
                            self.menu = False
                        elif self.seleccionado == "CONTROLES":
                            self.controles ()
                        elif self.seleccionado == "PARTIDAS ANTERIORES":
                            self.partidas_anteriores ()
                        elif self.seleccionado == "CREDITOS":
                            self.creditos ()
                        else:
                            exit ()

            #Dar formato al texto
            self.pantalla.blit (self.fondo, (0, 0))
            self.update ()
            #Colocar los textos en la pantalla
            self.pantalla.blit (self.texto_iniciar, (50, 25))
            self.pantalla.blit (self.texto_control, (50, 85))
            self.pantalla.blit (self.texto_anteriores, (50, 145))
            self.pantalla.blit (self.texto_creditos, (50, 205))
            self.pantalla.blit (self.texto_salir, (50, 265))

            pygame.display.set_caption ("Menu principal")

            self.clock.tick(60)
            pygame.display.flip()
        pygame.quit ()