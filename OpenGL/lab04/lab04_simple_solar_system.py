from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import numpy as np

import SimCamera


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_POSITION_X = 0
WINDOW_POSITION_Y = 0

angle = 0.0
myCam = SimCamera.Camera()

def drawPlanet(distance, angle, planetRadius, spin = 0.0, slope = 0.0):
    glRotatef(slope, 1, 0, 0)
    glBegin(GL_LINE_STRIP)
    for i in range(0, 361):
        theta = 2.0 * 3.141592 * i / 360.0
        x = distance * math.cos(theta)
        y = distance * math.sin(theta)
        glVertex3f(x, 0, y)
    glEnd()

    glRotatef(angle, 0, 1, 0)
    glTranslatef(distance, 0, 0)
    glPushMatrix()
    glRotatef(spin, 0, 1, 0)
    glutWireSphere(planetRadius, 10, 10)
    glPopMatrix()



def drawScene():
    global angle

    # drawing
    # sun
    glColor3f(1, 0, 0)
    glutSolidSphere(1.0, 20, 20)
    angle += 0.1
    # earth
    glPushMatrix()
    glColor3f(0, 0.5, 1.0)
    drawPlanet(10.0, angle, 0.5, angle*33.33, -5)
    # moon
    glColor(1.0, 1.0, 0.0)
    drawPlanet(2.0, 14.231*angle, 0.2, 0.0, slope = 23.5)
    glPopMatrix()


def disp():
    # reset buffer
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #gluPerspective(30, 1.0, 0.1, 100)
    myCam.applyLens()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glViewport(WINDOW_POSITION_X, WINDOW_POSITION_Y, int(WINDOW_WIDTH / 2), WINDOW_HEIGHT)
    #gluLookAt(10, 20, 60, 0, 0, -1, 0, 1, 0)

    myCam.setCameraLoc(np.array([-5,10,40]))
    #gluLookAt(0, 50, 0, 0, 0, 0, 0, 0, 1)
    myCam.applyCamera()
    drawScene()

    glFlush()


def main():
    # windowing
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(WINDOW_POSITION_X, WINDOW_POSITION_Y)
    glutCreateWindow(b"Simple Solar")

    glClearColor(0, 0.0, 0.0, 0)

    # register callbacks
    glutDisplayFunc(disp)
    glutIdleFunc(disp)

    # enter main infinite-loop
    glutMainLoop()


if __name__ == "__main__":
    main()



