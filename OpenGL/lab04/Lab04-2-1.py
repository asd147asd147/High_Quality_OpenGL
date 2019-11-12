#-*- coding:utf-8 -*-
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np
from PIL import Image
from math import *

time = 0

nTex = 6
texArr = None

angle_x = 0.0
angle_y = 0.0
r_x = 0.0
r_y = 1.0

def processSpecialKeys(key,x,y):
    global angle_x, angle_y, r_x, r_y
    if(key == GLUT_KEY_LEFT):
        angle_x += 0.1
        r_y = 1.0
        r_x = 0.0
    elif(key == GLUT_KEY_RIGHT):
        angle_x -= 0.1
        r_y = 1.0
        r_x = 0.0
    elif (key == GLUT_KEY_UP):
        angle_y += 10
        r_x = 1.0
        r_y = 0.0
    elif (key == GLUT_KEY_DOWN):
        angle_y -= 10
        r_x = 1.0
        r_y = 0.0

def loadImage(imageName) :
    img = Image.open(imageName)
    img_data = np.array(list(img.getdata()), np.uint8)
    return img.size[0], img.size[1], img_data

def setTexture(texArr, idx, fileName, option):

    glBindTexture(GL_TEXTURE_2D, texArr[idx])
    imgW, imgH, myImage = loadImage(fileName)
    #print(imgW, imgH, myImage)

    # texture image 생성
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
                 imgW, imgH, 0, option,
                 GL_UNSIGNED_BYTE, myImage)

    # texture 매핑 옵션 설정
    glTexParameterf(GL_TEXTURE_2D,
                    GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D,
                    GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D,
                    GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D,
                    GL_TEXTURE_MIN_FILTER, GL_NEAREST)



def drawQuad(x,y,z, angle, a_x, a_y, a_z) :
    glPushMatrix()
    glTranslatef(x,y,z)
    glRotatef(angle, a_x, a_y, a_z)
    glBegin(GL_QUADS)
    glTexCoord2f(0,0)
    glVertex3fv([-1, 1, 0])
    glTexCoord2f(0,1)
    glVertex3fv([-1,-1, 0])
    glTexCoord2f(1,1)
    glVertex3fv([ 1,-1, 0])
    glTexCoord2f(1,0)
    glVertex3fv([ 1, 1, 0])
    glEnd()
    glPopMatrix()

def myReshape(w, h) :
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    aspRatio = w / h
    gluPerspective(60, aspRatio, 0.1, 10)
    glViewport(0, 0, w, h)



def myDisplay():
    global time, texArr

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,5, 0,0,0, 0,1,0)
    if(r_y == 1.0):
        gluLookAt(3.0 * cos(angle_x), 0, 3.0 * sin(angle_x),  # 카메라위치->perspective때는허용됨
                  0.0, 0.0, -1.0,  # 초점
                  0.0, 1.0, 0.0)  # 카메라방향
    elif(r_x == 1.0):
        glRotatef(angle_y, 1, 0, 0)  # 카메라방향
    time += 0.1


    glBindTexture(GL_TEXTURE_2D, texArr[0])
    drawQuad(-1, 0, -1, -90, 0, 1, 0) #left
    glBindTexture(GL_TEXTURE_2D, texArr[1])
    drawQuad( 1, 0, -1, 90, 0, 1, 0) #right
    glBindTexture(GL_TEXTURE_2D, texArr[2])
    drawQuad( 0, 0, 0, 0, 0, 0, 0) #front
    glBindTexture(GL_TEXTURE_2D, texArr[3])
    drawQuad( 0, 1, -1, -90, 1, 0, 0) #up
    glBindTexture(GL_TEXTURE_2D, texArr[4])
    drawQuad(0, -1, -1, 90, 1, 0, 0) #down
    glBindTexture(GL_TEXTURE_2D, texArr[5])
    drawQuad(0, 0, -2, 180, 1, 0, 0) #behind

    gluLookAt(cos(time),1,sin(time), #카메라위치->perspective때는허용됨
              0.0, 0.0, 0.0,#초점
              0.0,1.0, 0.0) #카메라방향

    glFlush()

    return

def GLInit() :
    global nTex, texArr

    texArr = glGenTextures(nTex)
    # clear color setting
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)
    setTexture(texArr, 0, "pnu01.jpg", GL_RGB)
    setTexture(texArr, 1, "pnu02.jpg", GL_RGB)
    setTexture(texArr, 2, "pnu03.jpg", GL_RGB)
    setTexture(texArr, 3, "pnu04.jpg", GL_RGB)
    setTexture(texArr, 4, "pnu05.jpg", GL_RGB)
    setTexture(texArr, 5, "pnu06.jpg", GL_RGB)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_TEXTURE_2D)


def main(arg) :
    # opengl glut initialization
    glutInit(arg)

    # window setting
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Texture")

    glutSpecialFunc(processSpecialKeys)
    GLInit()

    glutReshapeFunc(myReshape)
    glutDisplayFunc(myDisplay)
    glutIdleFunc(myDisplay)

    glutMainLoop()


if __name__ == "__main__" :
    main(sys.argv)
