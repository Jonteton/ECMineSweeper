import pygame
import random


class Cell:
    def __init__(self, x, y, width, height, bomb_chance):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cell_center = (
            self.x + self.width // 2,
            self.y + self.width // 2,
        )  # useful for drawing
        self.cell = pygame.Rect(x, y, width, height)
        self.cell_thickness = 2
        self.color = (0, 64, 0)  # RGB color
        self.bomb = random.random() < bomb_chance
        self.selected = False
        self.neighbouring_bombs = 0

    def draw(self, screen, font):
        """!!Remember!! Pygame starts drawing in upper left corner as (0,0)"""
        pygame.draw.rect(screen, self.color, self.cell, width=self.cell_thickness)

        if self.selected:
            if not self.bomb:
                text_surface = font.render(
                    str(self.neighbouring_bombs), True, (255, 255, 255)
                )
                text_width = text_surface.get_width()
                text_height = text_surface.get_height()
                centered_x = self.x + self.width // 2 - text_width // 2
                centered_y = self.y + self.height // 2 - text_height // 2

                screen.blit(text_surface, (centered_x, centered_y))
            if self.bomb:
                text_surface = font.render("X", True, (255, 255, 255))
                text_width = text_surface.get_width()
                text_height = text_surface.get_height()
                centered_x = self.x + self.width // 2 - text_width // 2
                centered_y = self.y + self.height // 2 - text_height // 2

                screen.blit(text_surface, (centered_x, centered_y))

    def dummy_draw(self, screen):
        c_r = 5
        c_color = "red"
        pygame.draw.circle(screen, c_color, self.cell_center, c_r)
