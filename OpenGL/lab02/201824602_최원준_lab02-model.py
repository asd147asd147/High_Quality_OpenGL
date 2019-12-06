#-*- coding:utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import *

IsMove = True
IsZoom = True
ZoomSize = 1.0
    

##############################################################################
# vertices
##############################################################################

vertices=[#정점의 좌표
        -0.25,-0.25,0.25,
        -0.25,0.25,0.25,
        0.25,0.25,0.25,
        0.25,-0.25,0.25,
        -0.25,-0.25,-0.25,
        -0.25,0.25,-0.25,
        0.25,0.25,-0.25,
        0.25,-0.25,-0.25,
        ]
colors=[#각 정점의 색깔을 정의함 
        0.2,0.2,0.2,
        1.0,0.0,0.0,
        1.0,1.0,0.0,
        0.0,1.0,0.0,
        0.0,0.0,1.0,
        1.0,0.0,1.0,
        1.0,1.0,1.0,
        0.0,1.0,1.0,
        ]
indices=[ #정점 리스트 : 6면을 4개의 정점으로 한 면을 정의함
        0,3,2,1,
        2,3,7,6,
        0,4,7,3,
        1,2,6,5,
        4,5,6,7,
        0,1,5,4,
        ]

Angle=0.0

##############################################################################
def init():
    glClearColor (1.0, 1.0, 1.0, 1.0)

def drawAxis():
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex3f(0.0, -1.0, 0.0)
    glVertex3f(0.0, 1, 0.0)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0,1,0)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(1, 0.0, 0.0)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0,0,1)
    glVertex3f(0.0, 0.0, -1)
    glVertex3f(0.0, 0.0, 1)
    glEnd()
    
    
def MyTimer(Value):
    global Angle
    if IsMove:
        Angle += 0.2
    elif IsMove:
        Angle += 0
    glutPostRedisplay()
    glutTimerFunc(40,MyTimer,1)

def reshape_func(w, h):
    glViewport(0,0,w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1.0,0.01,20.0)

def disp_func():
    # clear
    glClear(GL_COLOR_BUFFER_BIT)
    glFrontFace(GL_CCW);							
    glEnable(GL_CULL_FACE);	
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices) #정점변수 설정
    glColorPointer(3, GL_FLOAT, 0, colors)#정점색 저장변수 지정

    # view
    global ZoomSize
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    if IsZoom and ZoomSize > 1.0:
        ZoomSize -= 0.5
    elif not IsZoom and ZoomSize < 10.0:
        ZoomSize += 0.5
    gluLookAt(ZoomSize * cos(Angle), 1, ZoomSize * sin(Angle),  # 카메라위치->perspective때는허용됨
              0.0, 0.0, 0.0,  # 초점
              0.0, 1.0, 0.0)  # 카메라방향
    drawAxis()
    glPushMatrix()
    glRotatef(30.0, 1.0, 1.0, 1.0)
    
    #for i in range(6):
    #    glDrawElements(GL_POLYGON,4,GL_UNSIGNED_BYTE, indices[4*i])
    glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE,indices)

    glPopMatrix()
    
    glDisableClientState(GL_COLOR_ARRAY)
    glDisableClientState(GL_VERTEX_ARRAY)
    glFlush()

def MySubMenu(entryID):
    global IsMove
    global IsZoom
    if entryID == 1:
        IsMove = True
    elif entryID == 2:
        IsMove = False
    elif entryID == 3:
        IsZoom = True
    elif entryID == 4:
        IsZoom = False
    glutPostRedisplay()
    return 0

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Vertex Handling")
    init()    

    glutDisplayFunc(disp_func)
    glutTimerFunc(40,MyTimer,1)
    glutReshapeFunc(reshape_func)
    MySubMenuAnimation = glutCreateMenu(MySubMenu)
    glutAddMenuEntry('Move', 1)
    glutAddMenuEntry('Stop', 2)
    MySubMenuCamera = glutCreateMenu(MySubMenu)
    glutAddMenuEntry('Zoom In', 3)
    glutAddMenuEntry('Zoom Out', 4)
    glutCreateMenu(MySubMenu)
    glutAddSubMenu('Animation', MySubMenuAnimation)
    glutAddSubMenu('Camera', MySubMenuCamera)
    glutAttachMenu(GLUT_RIGHT_BUTTON)

    glutMainLoop()

if __name__=="__main__":
    main()

