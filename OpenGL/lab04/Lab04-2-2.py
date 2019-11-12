from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from PIL import Image
import numpy


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutCreateWindow(b"sphere OpenGL")
    glutDisplayFunc(draw_sphere)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40, 1, 1, 40)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, 0, 10,
              0, 0, 0,
              0, 1, 0)
    glPushMatrix()
    glutMainLoop()
    return



def draw_sphere():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    texture_id = read_texture(b"pnu07.jpg")
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)

    glutSolidSphere(2, 50, 50)
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()
    glutSwapBuffers()
    return


def read_texture(filename):

    img = Image.open(filename)

    img_data = numpy.array(list(img.getdata()), numpy.int8)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    format = GL_RGB if img.mode == "RGB" else GL_RGBA
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0,
                 format, GL_UNSIGNED_BYTE, img_data)
    return texture_id


if __name__ == '__main__':
    main()