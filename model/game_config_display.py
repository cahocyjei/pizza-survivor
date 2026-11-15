import pygame
from rutas import ruta_img
class DisplayGame:
    start = True
    pantalla: pygame.display
    icono: pygame.image
    fondo: pygame.image
    def __init__(self):
        pygame.init()
        DisplayGame.pantalla = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("*** PIZZA SURVIVOR ***")
        DisplayGame.icono = pygame.image.load(ruta_img/"pizza.png")
        pygame.display.set_icon(DisplayGame.icono)
        DisplayGame.fondo = pygame.image.load(ruta_img/"fondo.png")
        DisplayGame.fondo = pygame.transform.scale(DisplayGame.fondo, (800, 600))
