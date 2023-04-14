import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

verticies = [
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),

    (0, 2, 0),

    (1.01, 0.5, -0.5),
    (1.01, 0.5, 0.5),
    (1.01, -0.5, 0.5),
    (1.01, -0.5, -0.5),

    (1.01, 0, -0.5),
    (1.01, 0, 0.5),

    (1.01, -0.5, 0),
    (1.01, 0.5, 0),


    (-1.01, 0.5, -0.5),
    (-1.01, 0.5, 0.5),
    (-1.01, -0.5, 0.5),
    (-1.01, -0.5, -0.5),

    (-1.01, 0, -0.5),
    (-1.01, 0, 0.5),

    (-1.01, -0.5, 0),
    (-1.01, 0.5, 0),

    # (0.5, 1, -0.5),
    # (0.5, 1, 0.5),
    # (-0.5, 1, 0.5),
    # (-0.5, 1, -0.5),
]

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),

    (1, 8),
    (2, 8),
    (5, 8),
    (7, 8),

    (9, 10),
    (10, 11),
    (11, 12),
    (12, 9),
    (13, 14),
    (15, 16),

    (17, 18),
    (18, 19),
    (19, 20),
    (20, 17),
    (21, 22),
    (23, 24)
)

surfaces = (
    (4, 0, 3, 6),
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    # (1,5,7,2), -

    (7, 2, 8),
    (1, 5, 8),
    (2, 1, 8),
    (5, 7, 8),
)


def frange(x, y, jump):
    while x < y:
        yield x
        x += jump


def random_color():
    levels = list(frange(0, 1, 0.001))
    return tuple(random.choice(levels) for _ in range(3))


colors = list(random_color() for _ in range(100))


def House(verticies):

    glBegin(GL_QUADS)
    x = 0
    for surface in surfaces:
        for vertex in surface:
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
            x += 1
    glEnd()

    glColor3fv((0, 0, 0))
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((0, 0, 0))
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    global surfaces

    pygame.init()
    display = (1000, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0, 0, -10)

    glEnable(GL_DEPTH_TEST)

    # verticies1 = list()
    # for i in verticies:
    #     v = list(i)
    #     v[0] += 3
    #     v[1] += 3
    #     verticies1.append(tuple(v))
    while True:
        # House(verticies1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_0):
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, 0, 2)
                elif event.key == pygame.K_UP:
                    glTranslatef(0, 0, -2)
                elif event.key == pygame.K_RSHIFT:
                    glRotatef(-5, 0, 1, 0)
                elif event.key == pygame.K_LSHIFT:
                    glRotatef(5, 0, 1, 0)
                elif event.key == pygame.K_LEFT:
                    glTranslatef(-2, 0, 0)
                elif event.key == pygame.K_RIGHT:
                    glTranslatef(2, 0, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        House(verticies)

        pygame.display.flip()


main()
