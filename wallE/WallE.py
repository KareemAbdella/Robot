from OpenGL.GLUT import *
from ui.Robot import *
from ui.World import *


def draw():
    glClearColor(0.5, 0.2, 0.4, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    BackStars()
    Road()
    The_WallE_Robot()
    glFlush()


def CoOrd():
    # TO TEST MY CO-ORD WHILE CODING
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex(0, 1)
    glVertex(0, -1)
    glVertex(1, 0)
    glVertex(-1, 0)
    glEnd()


# NOT SHOWN IN THE PIC..
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


# NOT SHOWN IN THE PIC..
def Hand2():
    glColor4f(0, 1, 0, 1)

    glTranslate(0.5, 0.3, 0)
    glScale(0.3, 0.3, 1)
    glBegin(GL_POLYGON)
    glVertex(0, 0.1)
    glVertex(0, -0.1)
    glVertex(0.7, -0.1)
    glVertex(0.7, 0.1)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex(0.7, 0.1)
    glVertex(0.7, -0.1)
    glVertex(-0.1, -0.4)
    glVertex(-0.15, -0.3)
    glEnd()
    glTranslate((-0.25 / 2), (-0.7 / 2), 0)
    glRotate(-63.43494882, 0, 0, 1)
    glColor3f(0.5, 0.2, 0)
    glBegin(GL_POLYGON)
    glVertex(0.15, 0)
    glVertex(0.15, -0.5)
    glVertex(-0.15, -0.5)
    glVertex(-0.15, 0)
    glEnd()
    glColor3f(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(-0.15, 0)
    glVertex(-0.2, -0.15)
    glVertex(-0.2, -0.4)
    glVertex(-0.16, -0.6)
    glVertex(-0.1, -0.6)
    glVertex(-0.1, -0.2)
    glVertex(0.1, -0.2)
    glVertex(0.1, -0.6)
    glVertex(0.16, -0.6)
    glVertex(0.2, -0.4)
    glVertex(0.2, 0.15)
    glVertex(0.15, 0)
    glEnd()

    glRotate(63.43494882, 0, 0, 1)
    glTranslate((0.25 / 2), (0.7 / 2), 0)
    glScale((10 / 3), (10 / 3), 1)
    glTranslate(-0.5, -0.3, 0)  # NOD


def The_WallE_Robot():
    # CoOrd()
    leg()
    body()
    Hand()
    # TO DRAW THE LEFT HALF
    glRotate(180, 0, 1, 0)
    leg()
    Hand()
    glRotate(-180, 0, 1, 0)
    Head()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Robot By Kareem Abdella")
glutDisplayFunc(draw)
glutMainLoop()
