from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

def setTexture() :

    myImage = [
        [255, 0, 0, 255, 255, 0, 0, 255, 0, 0, 0, 255],
        [255, 0, 0, 255, 255, 0, 0, 255, 0, 0, 0, 255],
        [255, 0, 0, 255, 255, 0, 0, 255, 0, 0, 0, 255],
        [255, 0, 0, 255, 255, 0, 0, 255, 0, 0, 0, 255]
    ]
    imgW = 4
    imgH = 4

    # texture image 생성
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
                 imgW, imgH, 0, GL_RGB,
                 GL_UNSIGNED_BYTE, myImage)

    # texture 매핑 옵션 설정
    glTexParameterf(GL_TEXTURE_2D,
                    GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D,
                    GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D,
                    GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D,
                    GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    # 2d texture 매핑을 활성화
    glEnable(GL_TEXTURE_2D)


def drawQuad() :
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

def myReshape(w, h) :
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    aspRatio = w / h
    gluPerspective(60, aspRatio, 0.1, 10)
    glViewport(0, 0, w, h)



def myDisplay():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,3, 0,0,0, 0,1,0)

    drawQuad()

    glFlush()

    return

def GLInit() :
    # clear color setting
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)
    setTexture()


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
