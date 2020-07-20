# Note: x and y coordinates represent the top left corner of each object
import pygame
import random


class Enemy:
    def __init__(self, screen, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.screen = screen
        self.size = 50
        self.__num = 6
        self.__change = 0
        orange = (255, 144, 38)
        blue = (23, 205, 255)
        yellow = (255, 221, 41)
        cyan = (69, 206, 204)
        purple = (87, 77, 255)
        pink = (242, 64, 235)
        self.colors = [orange, orange, blue, blue, yellow, yellow, cyan, cyan, purple, purple, pink, pink]
        self.score = 0
        self.list = []

    def add_enemy(self):
        # Whenever the list is less than num (6), the list will append up to 6 positions
        # Set a delay (random.random) for adding new position to the list,
        # so they will not display on the screen all at once
        if len(self.list) < self.__num and random.random() < 0.05:
            ex = random.randint(0, self.window_width - self.size)
            ey = 0
            position = [ex, ey]
            self.list.append(position)

        return self.list

    def enemy_level(self, score):
        # Set different levels of speed and number of enemy as the score grows
        if score < 20:
            self.__change = 4
        elif score < 40:
            self.__change = 6
            self.__num = 8
        elif score < 60:
            self.__change = 8
            self.__num = 10
        elif score < 80:
            self.__change = 10
            self.__num = 12
        else:
            self.__change = 16

        return self.__change

    def drop_enemy(self):
        # Enemy keeps falling in the range of screen height
        # If it is beyond the range of window, delete the position in the list and get score
        for index, position in enumerate(self.list):
            if 0 <= position[1] < self.window_height:
                position[1] += self.__change
            else:
                self.list.pop(index)
                self.score += 1

        return self.score

    def draw_enemy(self):
        # Color changes as the list deleting or adding new positions
        for index, position in enumerate(self.list):
            pygame.draw.rect(self.screen, self.colors[index], (position[0], position[1], self.size, self.size))
            
    def is_collision(self, px, py, player_size):
        # Check collision
        # px and py are the the player's top left coordinate
        # enemy x = position[0], enemy y = position [1], the enemy's top left coordinate
        for position in self.list:
            if px - self.size <= position[0] <= px + player_size:
                if py - self.size <= position[1] <= py + player_size:
                    return True
        return False
