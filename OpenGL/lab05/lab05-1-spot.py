from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

Ld = [0,1,1,1]
Ls = [0,1,1,1]

Ld1 = [1,1,0,1]
Ls1 = [1,1,0,1]

Ld2 = [1,0,1,1]
Ls2 = [1,0,1,1]

Ld3 = [1,1,1,1]
Ls3 = [1,1,1,1]

Lp = [1,1,5,1]
Lp1 = [1,1,5,1]
Lp2 = [1,1,5,1]
Lp3 = [0,0,5,1]

Md = [1,1,1,1]
Ms = [1,1,1,1]
shininess = [127.0]

flag = 0

t = 0

def LightSet():
    glLightfv(GL_LIGHT0, GL_DIFFUSE, Ld)
    glLightfv(GL_LIGHT0, GL_SPECULAR, Ls)
    #spot light setting
    glLightf (GL_LIGHT0, GL_SPOT_CUTOFF, 20.0)
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0,0,-1])
    glLightf (GL_LIGHT0, GL_SPOT_EXPONENT, 3.0)

    glLightfv(GL_LIGHT1, GL_DIFFUSE, Ld1)
    glLightfv(GL_LIGHT1, GL_SPECULAR, Ls1)
    # spot light setting
    glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 20.0)
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, [0, 0, -1])
    glLightf(GL_LIGHT1, GL_SPOT_EXPONENT, 3.0)

    glLightfv(GL_LIGHT2, GL_DIFFUSE, Ld2)
    glLightfv(GL_LIGHT2, GL_SPECULAR, Ls2)
    # spot light setting
    glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 20.0)
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, [0, 0, -1])
    glLightf(GL_LIGHT2, GL_SPOT_EXPONENT, 3.0)

    glLightfv(GL_LIGHT3, GL_DIFFUSE, Ld3)
    glLightfv(GL_LIGHT3, GL_SPECULAR, Ls3)
    # spot light setting
    glLightf(GL_LIGHT3, GL_SPOT_CUTOFF, 20.0)
    glLightfv(GL_LIGHT3, GL_SPOT_DIRECTION, [0, 0, -1])
    glLightf(GL_LIGHT3, GL_SPOT_EXPONENT, 3.0)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, Md)
    glMaterialfv(GL_FRONT, GL_SPECULAR, Ms)
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess)

def LightPosition(t):

    Lp[0] = 3.0*math.sin(t)
    Lp[1] = 3.0*math.cos(t)

    Lp1[0] = 3.0 * math.cos(t)
    Lp1[1] = 3.0 * math.sin(t)

    Lp2[0] = 3.0 * math.sin(t)
    Lp2[1] = 3.0 * math.sin(t)

    glLightfv(GL_LIGHT0, GL_POSITION, Lp)
    glLightfv(GL_LIGHT1, GL_POSITION, Lp1)
    glLightfv(GL_LIGHT2, GL_POSITION, Lp2)
    glLightfv(GL_LIGHT3, GL_POSITION, Lp3)

def glInit() :
    glClearColor(0,0,0.5,1)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHT2)
    glEnable(GL_LIGHT3)
    glEnable(GL_DEPTH_TEST)


def disp() :
    global t, flag
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # CAMERA setting
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #gluPerspective(60, 1.0, 0.1, 1000)
    glOrtho(-6,6,-6,6, -100,100)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,10, 0,0,0, 0,1,0)
    #gluLookAt(0,10,0, 0,0,0, 0,0,1)
    if flag <= 50:
        Ld3[0], Ld3[1], Ld3[2] = 1, 1, 1
        Ls3[0], Ls3[1], Ls3[2] = 1, 1, 1
        flag+=1
    else:
        Ld3[0],Ld3[1],Ld3[2] = 0,0,0
        Ls3[0], Ls3[1], Ls3[2] = 0,0,0
        flag += 1
    if flag == 100:
        flag = 0
    LightSet()
    t+= 0.01
    LightPosition(t)
    # OBJECTS 
    for x in range(-10, 11) :
        for y in range(-10, 11) :
            glPushMatrix()
            glTranslatef(x/2.0, y/2.0, 0)
            #glutSolidSphere(0.5, 20,20)
            glutSolidSphere(0.2, 20,20)
            glPopMatrix()

    glFlush()

def main():
    # windowing
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH | GLUT_RGB)
    glutInitWindowSize(512,512)
    glutInitWindowPosition(50,50)
    glutCreateWindow(b'Spot Lights')

    # initialization
    glInit()

    # register callbacks
    glutDisplayFunc(disp)
    glutIdleFunc(disp)

    # enter main loop
    glutMainLoop()

if __name__ == '__main__' :
    main()
    
