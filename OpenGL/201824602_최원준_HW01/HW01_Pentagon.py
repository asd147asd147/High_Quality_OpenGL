from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
def MyDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(0, 0, 300, 300)
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.75, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.7, 0.2, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-0.4, -0.5, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.4, -0.5, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.7, 0.2, 0.0)
    glEnd()
    glFlush()
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(300, 300)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"OpenGL Sample Drawing")# not only string, put ’b’ in front of string.
    glClearColor(0.5, 0.5, 0.5, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glutDisplayFunc(MyDisplay)
    glutMainLoop()
if __name__ == '__main__':
    main()