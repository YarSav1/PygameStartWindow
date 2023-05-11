import pygame


def correction(WINDOW, x,y,w,h, color):
    pygame.draw.rect(WINDOW, color, (x, y, w, h))