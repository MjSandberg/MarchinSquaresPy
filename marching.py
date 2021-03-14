import pygame as pg
import numpy as np
import random as rn
from opensimplex import OpenSimplex
import math

width = 1980
height = 1080

res = 5
increment = 0.1

tmp = OpenSimplex()


def grid(screen, rows, cols):
    xoff = 0
    rows = int(1 + height / res)
    cols = int(1 + width / res)
    field = np.zeros((cols, rows))
    for i in range(cols):
        xoff += increment
        yoff = 0
        for j in range(rows):
            field[i, j] = tmp.noise3d(xoff, yoff, zoff)
            yoff += increment
            col = abs(field[i, j]) * 255
            pg.draw.circle(screen, (col, col, col),
                           (i*res, j*res), res / 5)
    return field


def Getstate(a, b, c, d):
    # Some binary calculation
    return a * 8 + b * 4 + c * 2 + d * 1


def lines(screen, rows, cols, field):
    rows = int(1 + height / res)
    cols = int(1 + width / res)
    for i in range(cols-1):
        for j in range(rows - 1):
            x = i * res
            y = j * res
            a = (x + res * 0.5, y)
            b = (x + res, y + res * 0.5)
            c = (x + res * 0.5, y + res)
            d = (x, y + res * 0.5)
            state = Getstate(math.ceil(field[i, j]), math.ceil(field[i+1, j]),
                             math.ceil(field[i + 1, j + 1]), math.ceil(field[i, j + 1]))
            if state == 1:
                pg.draw.line(screen, (255, 255, 255), c, d)
            elif state == 2:
                pg.draw.line(screen, (255, 255, 255), b, c)
            elif state == 3:
                pg.draw.line(screen, (255, 255, 255), b, d)
            elif state == 4:
                pg.draw.line(screen, (255, 255, 255), a, b)
            elif state == 5:
                pg.draw.line(screen, (255, 255, 255), a, d)
                pg.draw.line(screen, (255, 255, 255), b, c)
            elif state == 6:
                pg.draw.line(screen, (255, 255, 255), a, c)
            elif state == 7:
                pg.draw.line(screen, (255, 255, 255), a, d)
            elif state == 8:
                pg.draw.line(screen, (255, 255, 255), a, d)
            elif state == 9:
                pg.draw.line(screen, (255, 255, 255), a, c)
            elif state == 10:
                pg.draw.line(screen, (255, 255, 255), a, b)
                pg.draw.line(screen, (255, 255, 255), c, d)
            elif state == 11:
                pg.draw.line(screen, (255, 255, 255), a, b)
            elif state == 12:
                pg.draw.line(screen, (255, 255, 255), b, d)
            elif state == 13:
                pg.draw.line(screen, (255, 255, 255), b, c)
            elif state == 14:
                pg.draw.line(screen, (255, 255, 255), c, d)


def main():
    pg.init()
    screen = pg.display.set_mode((width, height))
    clock = pg.time.Clock()
    screen.fill((127, 127, 127))
    global zoff
    zoff = 0

    while (True):
        zoff += 0.1
        field = grid(screen, width, height)
        lines(screen, width, height, field)
        pg.display.update()
        screen.fill((127, 127, 127))
        clock.tick(0)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()


main()
