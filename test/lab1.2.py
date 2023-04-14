import glfw
from OpenGL.GL import *
import random

delta = 0.0
pos = [0, 0, 0]

verticies = [
    (0.1, -0.1, -0.1),
    (0.1, 0.1, -0.1),
    (-0.1, 0.1, -0.1),
    (-0.1, -0.1, -0.1),
    (0.1, -0.1, 0.1),
    (0.1, 0.1, 0.1),
    (-0.1, -0.1, 0.1),
    (-0.1, 0.1, 0.1)
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
    (5, 7)
)

surfaces = (
    (4, 0, 3, 6),
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2)
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


def display(window):
    global verticies
    global delta

    glLoadIdentity()
    glTranslatef(pos[0], pos[1], pos[2])
    glClearColor(0.5, 0.5, 0.5, 0.5)
    glPushMatrix()
    glRotatef(delta, 0, 1, 0)

    House(verticies)
    glPopMatrix()

    glfw.swap_buffers(window)
    glfw.poll_events()


def key_callback(window, key, scancode, action, mods):
    global delta
    if action == glfw.PRESS:
        if key == glfw.KEY_DOWN:
            pos[1] -= 0.1
        elif key == glfw.KEY_UP:
            pos[1] += 0.1

        elif key == glfw.KEY_RIGHT_SHIFT:
            delta -= 5
        elif key == glfw.KEY_LEFT_SHIFT:
            delta += 5
        elif key == glfw.KEY_LEFT:
            pos[0] -= 0.1
        if key == glfw.KEY_RIGHT:
            pos[0] += 0.1


def main():
    global surfaces

    if not glfw.init():
        return

    display_ = (1000, 800)
    window = glfw.create_window(display_[0], display_[1], "Lab1", None, None)
    if not window:
        glfw.terminate()
        return

    # gluPerspective(45, (display_[0]/display_[1]), 0.1, 50.0)

    glEnable(GL_DEPTH_TEST)

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        display(window)
    glfw.destroy_window(window)
    glfw.terminate()


main()
