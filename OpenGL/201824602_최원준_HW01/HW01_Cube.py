from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

colors = ((1,0,0),
          (0,1,0),
          (0,0,1),
          (0,1,0))

surfaces = ((0,1,2,3),
            (3,2,7,6),
            (4,5,1,0),
            (1,5,7,2),
            (4,0,3,6))

vertices = ((0.5,-0.5,-0.5),(0.5,0.5,-0.5),
            (-0.5,0.5,-0.5),(-0.5,-0.5,-0.5),
            (0.5,-0.5,0.5),(0.5,0.5,0.5),
            (-0.5,-0.5,0.5),(-0.5,0.5,0.5))

edges = ((0,1),(0,3),(0,4),
         (2,1),(2,3),(2,7),
         (6,3),(6,4),(6,7),
         (5,1),(5,4),(5,7))

def MyDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(150, 150, 300, 300)
    glRotatef(30, 0.5, 0, 0)
    glRotatef(30, 0, 0, 0.5)
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
            x += 1
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()
    glFlush()
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(500, 500)
    glutCreateWindow(b"OpenGL Sample Drawing")# not only string, put ’b’ in front of string.
    glClearColor(0.5, 0.5, 0.5, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glutDisplayFunc(MyDisplay)
    glutMainLoop()

if __name__ == '__main__':
    main()