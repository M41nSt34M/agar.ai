import pygame

import vector
from controllers.abstract_controller import AbstractController


# controls a blob family according to a mouse movemnt
class mouse_controller(AbstractController):

    def __init__(self, view_size, player_radius, model):
        self.view_center = vector.divide(view_size, 2)
        self.player_radius = player_radius
        self.model = model

    def update(self):
        if not self.manipulator.is_alive(): return

        mouse_position = pygame.mouse.get_pos()
        direction = vector.substract(mouse_position, self.view_center)
        direction = vector.divide(direction, self.player_radius)
        self.manipulator.set_velocity(direction)

        for event in self.model.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: self.manipulator.divide()
                elif event.button == 3: self.manipulator.shoot()
