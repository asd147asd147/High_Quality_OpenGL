from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np
from PIL import Image

time = 0

nTex = 4
texArr = None


def loadImage(imageName) :
    img = Image.open(imageName)
    img_data = np.array(list(img.getdata()), np.uint8)
    return img.size[0], img.size[1], img_data

def setTexture(texArr, idx, fileName, option):

    glBindTexture(GL_TEXTURE_2D, texArr[idx])
    imgW, imgH, myImage = loadImage(fileName)
    print(imgW, imgH, myImage)

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



def drawQuad(x,y,z, angle) :
    glPushMatrix()
    glTranslatef(x,y,z)
    glRotatef(angle, 1,1,1)
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

    time += 0.1


    glBindTexture(GL_TEXTURE_2D, texArr[0])
    drawQuad(-1, 1, 0, time)
    glBindTexture(GL_TEXTURE_2D, texArr[1])
    drawQuad( 1, 1, 0, time)
    glBindTexture(GL_TEXTURE_2D, texArr[2])
    drawQuad(-1,-1, 0, time)
    glBindTexture(GL_TEXTURE_2D, texArr[3])
    drawQuad( 1,-1, 0, time)

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

    GLInit()

    glutReshapeFunc(myReshape)
    glutDisplayFunc(myDisplay)
    glutIdleFunc(myDisplay)

    glutMainLoop()


if __name__ == "__main__" :
    main(sys.argv)
