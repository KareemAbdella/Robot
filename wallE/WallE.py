import random
from math import *

import numpy as s
from OpenGL.GL import *
from OpenGL.GLUT import *


def draw():
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    The_WallE_Robot()
    glFlush()


def circleB():
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


def Background():
    glColor3f(1, 0, 0)
    for i in range(20):
        circleB()


def CoOrd():
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex(0, 1)
    glVertex(0, -1)
    glVertex(1, 0)
    glVertex(-1, 0)
    glEnd()


def circle(r):
    for theta in s.arange(0, 2 * pi, 0.0001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x, y)


def body():
    glLineWidth(2)
    glColor3f(1, 0.7, 0.1)
    # glScale(2, 2, 2)
    glBegin(GL_POLYGON)
    glVertex(0.5, -0.5)
    glVertex(0.5, 0.5)
    glVertex(-0.5, 0.5)
    glVertex(-0.5, -0.5)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(1, 0.8, 0.3)
    glVertex(-0.1, 0)
    glVertex(-0.4, 0)
    glVertex(-0.4, 0.4)
    glVertex(-0.1, 0.4)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 0.7, 0.1)
    glVertex(-0.55, 0.4)
    glVertex(-0.55, 0.45)
    glVertex(-0.5, 0.5)
    glVertex(0.5, 0.5)
    glVertex(0.55, 0.45)
    glVertex(0.55, 0.4)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    glVertex(-0.5, -0.5)
    glVertex(-0.5, 0.5)
    glVertex(0.5, 0.5)
    glVertex(0.5, -0.5)
    glVertex(0.5, -0.5)
    glVertex(-0.5, -0.5)
    glVertex(0.5, 0.5)
    glVertex(-0.5, 0.5)
    glVertex(0.55, 0.4)
    glVertex(-0.55, 0.4)
    glVertex(0.55, 0.4)
    glVertex(0.55, 0.45)
    glVertex(-0.55, 0.4)
    glVertex(-0.55, 0.45)
    glVertex(0.55, 0.45)
    glVertex(0.5, 0.5)
    glVertex(-0.55, 0.45)
    glVertex(-0.5, 0.5)
    glVertex(0.25, 0.5)
    glVertex(0.25, 0.4)
    glVertex(-0.25, 0.5)
    glVertex(-0.25, 0.4)
    glVertex(0.25, 0.475)
    glVertex(0.5, 0.475)
    glVertex(-0.25, 0.475)
    glVertex(-0.5, 0.475)

    glEnd()
    glTranslate(0.125, 0.45, 0)
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    circle(0.03)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(1, 0, 0)
    circle(0.015)
    glEnd()

    glTranslate(-0.125, -0.45, 0)


def leg():
    glTranslate(0.4, -0.4, 0)
    glScale(0.097, 0.1, 0)
    glColor3f(0, 0.4, 0.2)

    glBegin(GL_POLYGON)
    glVertex(0, 0)
    glVertex(0, -2)
    glVertex(0.3, -2.5)
    glVertex(1, -2.5)
    glVertex(1, -2)
    glVertex(1.5, -1.75)
    glVertex(1.5, 0)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glColor3f(0, 0, 0)
    glVertex(1, -2.15)
    glVertex(1, -2.35)
    glVertex(1.5, -2.35)
    glVertex(1.5, -2.15)
    glEnd()
    glBegin(GL_LINE_LOOP)

    glVertex(0, 0)
    glVertex(0, -2)
    glVertex(0.3, -2.5)
    glVertex(1, -2.5)
    glVertex(1, -2)
    glVertex(1.5, -1.75)
    glVertex(1.5, 0)
    glEnd()
    glBegin(GL_LINES)
    glVertex(0, -2)
    glVertex(1, -2)
    glEnd()
    glColor3f(0.1, 0.1, 0)
    glBegin(GL_POLYGON)
    glVertex(1.5, 0.5)
    glVertex(3, 0.5)
    glVertex(3, -3.5)
    glVertex(1.5, -3.5)
    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex(1.5, 0)
    glVertex(3, 0)
    glVertex(1.5, -0.5)
    glVertex(3, -0.5)
    glVertex(1.5, -1)
    glVertex(3, -1)
    glVertex(1.5, -1.5)
    glVertex(3, -1.5)
    glVertex(1.5, -2)
    glVertex(3, -2)
    glVertex(1.5, -2.5)
    glVertex(3, -2.5)
    glVertex(1.5, -3)
    glVertex(3, -3)
    glEnd()

    glScale(10.3, 10, 0)
    glTranslate(-0.4, 0.4, 0)


def Head2():
    glTranslate(0, 0.5, 0)
    glColor3f(0, 0.4, 0.2)

    glBegin(GL_POLYGON)
    glVertex(0.2, 0)
    glVertex(-0.2, 0)
    glVertex(-0.1, 0.1)
    glVertex(0.1, 0.1)
    glEnd()
    glTranslate(0, -0.5, 0)


def BackStars():
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


def The_WallE_Robot():
    # CoOrd()
    BackStars()
    Road()
    leg()
    # Hand()
    # To Draw The Left Half
    glRotate(180, 0, 1, 0)
    leg()
    # Hand()
    glRotate(-180, 0, 1, 0)
    body()
    Head()


def Head():
    def half_circle(r):
        for theta in s.arange(0, pi, 0.001):
            x = r * cos(theta)
            y = r * sin(theta)
            glVertex(x, y)

    def half_circle_hair(r):
        for theta in s.arange(0, pi, 1):
            x = r * cos(theta)
            y = r * sin(theta)
            glVertex(x, y)

    glTranslate(0, 0.5, 0)
    glBegin(GL_POLYGON)
    # Skinny Color
    glColor3f(0, 0.4, 0.2)
    half_circle_hair(0.25)
    glEnd()
    glBegin(GL_LINE_STRIP)
    # Skinny Color

    glColor3f(0.8, 1, 1)
    half_circle(0.25)
    glEnd()

    # Eye
    def Eye():
        glTranslate(0.125, 0.125, 0)
        glBegin(GL_POLYGON)
        glColor3f(1, 1, 1)
        circle(0.05)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(0, 0, 0)
        circle(0.02)
        glEnd()
        glTranslate(-0.125, -0.125, 0)

    Eye()
    glRotate(180, 0, 1, 0)
    Eye()
    glRotate(-180, 0, 1, 0)

    glTranslate(0, -0.5, 0)


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


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Wall-E By Kareem Abdella")
glutDisplayFunc(draw)
glutMainLoop()
