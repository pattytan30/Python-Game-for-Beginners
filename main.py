"""
CS521 Final Project: Spaceship Game
Author: Peiqi Tan (ptan@bu.edu)
April 2020
Environment: Pycharm
Python 3.8; pip 20.0.2; pygame 2.0.0dev6

Introduction:
Press left and right arrow keys to control the spaceship's movement.
Get points when you escape from getting crash by cubes.
The highest points will be stored in txt file, and updated on the screen.

"""

import pygame
import sys
from player import Player
from enemy import Enemy
from score import Score
pygame.init()


def display_game_over(screen, window_width, window_height):
    font = pygame.font.SysFont("Arial", 70, bold=True)
    text_color = (255, 255, 255)
    game_over_label = font.render("Game Over!", 1, text_color)
    screen.blit(game_over_label, (window_width/3, window_height/2))


def main():
    # screen elements
    window_width = 800
    window_height = 770
    screen = pygame.display.set_mode((window_width, window_height))
    bg_color = (0, 0, 0)

    # player elements
    player_size = 32
    change = 0
    speed = 5
    p = Player(screen, player_size, window_width, window_height)

    # enemy elements
    e = Enemy(screen, window_width, window_height)

    # while loop to run until game over
    # for loop for handling events
    run = True

    while run:
        screen.fill(bg_color)

        for event in pygame.event.get():
            # handle exit the game
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            # handle direction by arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change = -speed
                if event.key == pygame.K_RIGHT:
                    change = speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    change = 0

        # player
        x = p.player_movement(change)
        y = p.py
        p.draw_player()

        # enemy
        e.add_enemy()
        e.draw_enemy()

        # score
        score = e.drop_enemy()
        s = Score(screen, score)
        s.display_score()
        s.store_highest_score()
        e.enemy_level(score)

        # check collision
        if e.is_collision(x, y, player_size) is True:
            display_game_over(screen, window_width, window_height)
            pygame.time.delay(120)
            run = False

        pygame.time.Clock().tick(60)
        pygame.display.update()


if __name__ == "__main__":
    main()
