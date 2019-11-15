from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import numpy as np

def loadMesh(filename):
    with open(filename, "rt") as mesh :
        nV = int(next(mesh))
        verts = [[0,0,0] for idx in range(nV)]
        for i in range(0, nV) :
            verts[i][0], verts[i][1], verts[i][2] = [float(x) for x in next(mesh).split()]
        nF = int(next(mesh))
        faces = [[0,0,0] for idx in range(nF)]
        for i in range(0, nF) :
            faces[i][0], faces[i][1], faces[i][2] = [int(x) for x in next(mesh).split()]
    return verts, faces

V, F = loadMesh("testCube.txt")



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
    glLightf (GL_LIGHT0, GL_SPOT_CUTOFF, 10.0)
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0,0,-1])
    glLightf (GL_LIGHT0, GL_SPOT_EXPONENT, 3.0)

    glLightfv(GL_LIGHT1, GL_DIFFUSE, Ld1)
    glLightfv(GL_LIGHT1, GL_SPECULAR, Ls1)
    # spot light setting
    glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 10.0)
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, [0, 0, -1])
    glLightf(GL_LIGHT1, GL_SPOT_EXPONENT, 3.0)

    glLightfv(GL_LIGHT2, GL_DIFFUSE, Ld2)
    glLightfv(GL_LIGHT2, GL_SPECULAR, Ls2)
    # spot light setting
    glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 10.0)
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, [0, 0, -1])
    glLightf(GL_LIGHT2, GL_SPOT_EXPONENT, 3.0)

    glLightfv(GL_LIGHT3, GL_DIFFUSE, Ld3)
    glLightfv(GL_LIGHT3, GL_SPECULAR, Ls3)
    # spot light setting
    glLightf(GL_LIGHT3, GL_SPOT_CUTOFF, 10.0)
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

# initialization
def GLinit() :
    #색상,z-buffer, 조명 설정
    glClearColor(0,0,0.5,1)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHT2)
    glEnable(GL_LIGHT3)
    glEnable(GL_DEPTH_TEST)

def computeNormal(p1, p2, p3) :
    u = np.array([p2[i] - p1[i] for i in range(0, 3)])
    v = np.array([p3[i] - p1[i] for i in range(0, 3)])
    N = np.cross(u,v)
    N = N / np.linalg.norm(N)
    return N

def drawVerts(v, f):
    glBegin(GL_TRIANGLES)
    for i in range(len(f)) :
        p1, p2, p3 = f[i][0], f[i][1], f[i][2]
        N = computeNormal(v[p1], v[p2], v[p3])
        glNormal3fv(N)
        glVertex3fv(v[p1])
        glVertex3fv(v[p2])
        glVertex3fv(v[p3])
    glEnd()

# display callback
def display() :
    global t, V, F, flag

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # CAMERA SETTING
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, 1.0, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,8, 0,0,0, 0,1,0)
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
    t += 0.01
    LightPosition(t)

    for x in range(-10, 11) :
        for y in range(-10, 11) :
            glPushMatrix()
            glTranslatef(x/3.0, y/3.0, 0)
            drawVerts(V, F)
            glPopMatrix()
    glFlush()

def main():
    # windowing
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH |GLUT_RGBA)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(10,10)
    glutCreateWindow(b"Light on Mesh in file ")

    GLinit()

    # register callbacks
    glutDisplayFunc(display)
    glutIdleFunc(display)

    # enter main-loop
    glutMainLoop()


if __name__ == '__main__' :
    main()

