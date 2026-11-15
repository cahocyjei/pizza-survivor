import pygame

from model.game_config_display import DisplayGame
from model.perro import Perro
from rutas import ruta_img


class Pizza:
    imagen = None

    def __init__(
        self,
        origen: tuple[float, float],
        objetivo: tuple[float, float],
        velocidad: float = 300,
    ):
        if Pizza.imagen is None:
            Pizza.imagen = pygame.image.load(ruta_img / "pizza.png")
            Pizza.imagen = pygame.transform.scale(Pizza.imagen, (32, 32))

        self.posicion = pygame.Vector2(origen) - pygame.Vector2(16, 16)
        self.rect = Pizza.imagen.get_rect(center=origen)
        direccion = pygame.Vector2(objetivo) - pygame.Vector2(origen)
        if direccion.length_squared() == 0:
            raise ValueError("El origen y el objetivo de la pizza deben ser distintos.")
        self.direccion = direccion.normalize()
        self.velocidad = velocidad

    def actualizar(self, delta_segundos: float) -> bool:
        desplazamiento = self.direccion * self.velocidad * delta_segundos
        self.posicion += desplazamiento
        self.rect.topleft = (round(self.posicion.x), round(self.posicion.y))
        return DisplayGame.pantalla.get_rect().colliderect(self.rect)

    def load_Pizza(self):
        DisplayGame.pantalla.blit(Pizza.imagen, self.rect)

    def detectar_colisiones(perros: list, pizzas: list):
            pass