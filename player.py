# Note: x and y coordinates represent the top left corner of each object
import pygame


class Player:
    def __init__(self, screen, player_size, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.screen = screen
        self.px = 400
        self.py = 600
        self.image = pygame.image.load("spaceship.png")
        self.size = player_size

    def draw_player(self):
        self.screen.blit(self.image, (self.px, self.py))

    def player_movement(self, change):
        # Set the speed of player movement
        self.px += change

        # Set a boundary
        # The player cannot be moved out of the range of window width and height
        if self.px <= 0:
            self.px = 0
        elif self.px >= self.window_width - self.size:
            self.px = self.window_width - self.size

        return self.px

    def __repr__(self):
        return "Player({self.px}{self.py}{self.size}".format(self=self)

