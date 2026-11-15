"""Proyecto de Juego: PIZZA SURVIVOR"""

import pygame

from model.game_config_display import DisplayGame
from model.personaje import Repartidor
from model.perro import Perro
from model.pizza import Pizza

#Loop game
def main():
    DisplayGame()
    Repartidor()
    perros = [Perro()]
    pizzas = []
    reloj = pygame.time.Clock()
    tiempo_para_disparo = 0.0
    tiempo_para_nuevo_perro = 0.0
    #Pizza.detectar_colisiones(perros, pizzas)
    while DisplayGame.start:
        delta_segundos = reloj.tick(60) / 1000
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                DisplayGame.start = False
            Repartidor.mover_Personaje(evento, 3)

        tiempo_para_nuevo_perro += delta_segundos
        while tiempo_para_nuevo_perro >= 3:
            tiempo_para_nuevo_perro -= 5
            perros.append(Perro())

        DisplayGame.pantalla.blit(DisplayGame.fondo,(0,0))
        Repartidor.avanza_Repartidor()
        Repartidor.limitar_Posicion()
        Repartidor.load_Personaje()
        for perro in perros:
            perro.avance_Perro(60 * delta_segundos)
            perro.load_Perro()

        tiempo_para_disparo += delta_segundos
        while tiempo_para_disparo >= 1:
            tiempo_para_disparo -= 1
            if perros:
                origen = (Repartidor.posicion_x + 32, Repartidor.posicion_y + 50)
                perro_cercano = min(
                    perros,
                    key=lambda perro: pygame.Vector2(origen).distance_squared_to(perro.centro),
                )
                if perro_cercano.centro != origen:
                    pizzas.append(Pizza(origen, perro_cercano.centro))

        pizzas = [pizza for pizza in pizzas if pizza.actualizar(delta_segundos)]
        for pizza in pizzas:
            pizza.load_Pizza()

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()