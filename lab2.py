import glfw
from OpenGL.GL import *
import random
import math

deltaZ = 0.0
deltaX = 0.0
deltaY = 0.0
m = [[0.87, 0.0, 1.0, 0.5], [0, 1, 0, 0], [0.5, 0, -1.73, -0.87], [0, 0, 1, 2]]
mode = GL_FILL

verticies = [
    (0.6, -0.6, -0.6),
    (0.6, 0.6, -0.6),
    (-0.6, 0.6, -0.6),
    (-0.6, -0.6, -0.6),
    (0.6, -0.6, 0.6),
    (0.6, 0.6, 0.6),
    (-0.6, -0.6, 0.6),
    (-0.6, 0.6, 0.6)
    ]

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces = (
    (4,0,3,6),
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2)
    )

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

def random_color():
    levels = list(frange(0,1,0.001))
    return tuple(random.choice(levels) for _ in range(3))

colors = list(random_color() for _ in range(30))

def makeMZ(d):
    return [[math.cos(d), math.sin(d), 0, 0], 
          [-math.sin(d),math.cos(d), 0, 0],
           [0,0,1,0], [0,0,0,1]]

def makeMX(d):
    return [[1, 0,0,0],
            [0, math.cos(d), math.sin(d), 0], 
            [0, -math.sin(d),math.cos(d), 0],
            [0,0,0,1]]

def makeMY(d):
    return [[math.cos(d), 0, -math.sin(d), 0], [0, 1, 0,0], [math.sin(d), 0,math.cos(d),0], [0,0,0,1]]

def Cube(verticies):

    glBegin(GL_QUADS)
    x = 0
    for surface in surfaces:
        for vertex in surface:
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
            x += 1
    glEnd()

    glColor3fv((0,0,0))
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((0, 0, 0))
            glVertex3fv(verticies[vertex])
    glEnd()

def display(window):
    global verticies
    global deltaZ
    global deltaX
    global deltaY
    global mode


    glPolygonMode(GL_FRONT_AND_BACK, mode)
    glClearColor(0.5, 0.5, 0.5, 0.5)

    glViewport(500, 400, 450, 360)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glPushMatrix()
    glMultMatrixd(makeMY(10))
    glMultMatrixd(makeMZ(-5))

    Cube(verticies)

    glPopMatrix()


    glViewport(0, 0, 500, 400)
    glMatrixMode(GL_PROJECTION)
    glLoadMatrixd(m)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glPushMatrix()
    glMultMatrixd(makeMY(10))
    glMultMatrixd(makeMZ(deltaZ))
    glMultMatrixd(makeMX(deltaX))
    glMultMatrixd(makeMY(deltaY))
    Cube(verticies)

    glPopMatrix()



    glfw.swap_buffers(window)
    glfw.poll_events()


def key_callback(window, key, scancode, action, mods):
    global deltaZ
    global deltaY
    global deltaX
    global mode
    if action == glfw.PRESS:
        if key == glfw.KEY_RIGHT_SHIFT:
            deltaZ -= 0.20
        elif key == glfw.KEY_LEFT_SHIFT:
            deltaZ += 0.20

        elif key == glfw.KEY_LEFT:
            deltaY -= 0.20
        elif key == glfw.KEY_RIGHT:
            deltaY += 0.20

        elif key == glfw.KEY_DOWN:  
            deltaX -= 0.20
        elif key == glfw.KEY_UP:
            deltaX += 0.20
        elif key == glfw.KEY_0:
            if mode == GL_LINE:
                mode = GL_FILL
            else: 
                mode = GL_LINE
        

def main():
    global surfaces

    if not glfw.init():
        return

    display_ = (1000,800)
    window = glfw.create_window(display_[0], display_[1], "Lab2", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    # glEnable(GL_DEPTH_TEST) 

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        display(window)
    glfw.destroy_window(window)
    glfw.terminate()
        
main() 