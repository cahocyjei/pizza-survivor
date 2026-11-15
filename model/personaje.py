import pygame
from model.game_config_display import DisplayGame
from rutas import ruta_img
class Repartidor:
    posicion_x: int
    posicion_y: int
    imagen: pygame.image
    cambio_x: float
    cambio_y: float

    def __init__(self):
        Repartidor.posicion_x = 368
        Repartidor.posicion_y = 440 
        Repartidor.cambio_x = 0
        Repartidor.cambio_y = 0
        Repartidor.imagen = pygame.image.load(ruta_img/"repartidor.png")
        Repartidor.imagen = pygame.transform.scale(Repartidor.imagen, (64, 100))

    def load_Personaje():
        DisplayGame.pantalla.blit(Repartidor.imagen, (Repartidor.posicion_x, Repartidor.posicion_y))

    def mover_Personaje(evento: pygame.event, velocidad: float):
        '''pygame almacena todos los eventos que suceden durante el juego,
        como el mouse, una tecla ect.
        podemos acceder a esa lista por medio de pygame.event.get()
        '''
        if evento.type == pygame.KEYDOWN:
            match evento.key:
                case pygame.K_LEFT:
                    Repartidor.cambio_x = -velocidad
                case pygame.K_RIGHT:
                    Repartidor.cambio_x = velocidad
                case pygame.K_UP:
                    Repartidor.cambio_y = -velocidad
                case pygame.K_DOWN:
                    Repartidor.cambio_y = velocidad
        elif evento.type == pygame.KEYUP:
            Repartidor.cambio_x = 0
            Repartidor.cambio_y = 0

    def limitar_Posicion():
        if Repartidor.posicion_x < 0:
            Repartidor.cambio_x = 0
        elif Repartidor.posicion_x > 736:
            Repartidor.posicion_x = 736
        if Repartidor.posicion_y < 0:
            Repartidor.cambio_y = 0
        elif Repartidor.posicion_y > 500:
            Repartidor.posicion_y = 500

    def avanza_Repartidor():
        Repartidor.posicion_x += Repartidor.cambio_x
        Repartidor.posicion_y += Repartidor.cambio_y