import random

import pygame

from model.game_config_display import DisplayGame
from model.personaje import Repartidor
from rutas import ruta_img


class Perro:
    def __init__(self):
        self.perro = pygame.image.load(ruta_img / "perro.png")
        self.perro = pygame.transform.scale(self.perro, (54, 64))
        self.posicion_x = random.randint(0, 800 - 54)
        self.posicion_y = 0

    @property
    def centro(self) -> tuple[float, float]:
        return (
            self.posicion_x + self.perro.get_width() / 2,
            self.posicion_y + self.perro.get_height() / 2,
        )

    def load_Perro(self):
        DisplayGame.pantalla.blit(self.perro, (self.posicion_x, self.posicion_y))

    def avance_Perro(self, velocidad: float):
        centro_repartidor = (
            Repartidor.posicion_x + Repartidor.imagen.get_width() / 2,
            Repartidor.posicion_y + Repartidor.imagen.get_height() / 2,
        )
        direccion = pygame.Vector2(centro_repartidor) - pygame.Vector2(self.centro)
        if direccion.length_squared() > 0:
            movimiento = direccion.normalize() * velocidad
            self.posicion_x += movimiento.x
            self.posicion_y += movimiento.y
