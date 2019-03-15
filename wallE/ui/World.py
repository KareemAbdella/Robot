import random
from math import *
import numpy as s
from OpenGL.GL import *



def Road():
    glColor3f(0.3, 0.5, 0.6)
    glBegin(GL_POLYGON)
    glVertex(1, -1)
    glVertex(-1, -1)
    glVertex(-0.2, 0.1)
    glVertex(0.2, 0.1)
    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex(0.07, -0.9)
    glVertex(0.022, -0.6)
    glVertex(-0.022, -0.6)
    glVertex(-0.07, -0.9)
    glEnd()



def BackStars():
    # THE WORLD WILL RANDOMLY DRAWIN AT QUAR1 , HERE TO ROTATE TO QUAR2,QUAR3,QUAR4
    Background()
    glRotate(180, 0, 1, 0)
    Background()
    glRotate(180, 1, 0, 0)
    Background()

    glRotate(-180, 1, 0, 0)
    glRotate(-180, 0, 1, 0)

    glRotate(180, 1, 0, 0)
    Background()
    glRotate(-180, 1, 0, 0)
    glRotate(180, 1, 1, 0)
    Background()
    glRotate(-180, 1, 1, 0)


def Background():
    # TO DRAW THE STARS OF THE WORLD
    glColor4f(1, 0, 0, 0.1)
    for i in range(20):
        circleB()



def circleB():
    # TO DRAW THE WORLD STARS WITH RANDOM PLACES, RANDOM RADIOUS
    TX = random.random()
    TY = random.random()
    glTranslate(TX, TY, 0)
    r = random.random() / 30
    glBegin(GL_POLYGON)
    for theta in s.arange(0, 2 * pi, 0.001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x, y)
    glEnd()
    glTranslate(-TX, -TY, 0)
