import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
import DrawObject
from ObjLoader import *

# IMPORT OBJECT LOADER

pygame.init()
viewport = (800,600)
hx = viewport[0]/2
hy = viewport[1]/2
srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)

clock = pygame.time.Clock()
width, height = viewport
gluPerspective(90.0, width/float(height), 1, 100000.0)

ani = DrawObject.drawObject(800,600, b"Lab07:found")

rx, ry = (0,0)
tx, ty = (0,0)
zpos = 5
rotate = move = False

while 1:
    clock.tick(30)
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN and e.key == K_x :
            print("click!")
            ani.buttonClick()
        elif e.type == KEYDOWN and e.key == K_y :
            ani.weather = 0
            ani.changeModel_basic()
        elif e.type == KEYDOWN and e.key == K_u:
            ani.weather = 1
            ani.changeModel_basic()
        elif e.type == KEYDOWN and e.key == K_i :
            ani.weather = 2
            ani.rain.add_time = ani.getEt()
            ani.changeModel_rain()
        elif e.type == KEYDOWN and e.key == K_o :
            ani.weather = 3
            ani.snow.add_time = ani.getEt()
            ani.changeModel_snow()
        elif e.type == KEYDOWN and e.key == K_p:
            ani.weather = 4
            ani.firework.add_time = ani.getEt()
            ani.changeModel_basic()

        elif e.type == KEYDOWN and e.key == K_w :
            ani.changeCamera('w')

        elif e.type == KEYDOWN and e.key == K_s:
            ani.changeCamera('s')

        elif e.type == KEYDOWN and e.key == K_a:
            ani.changeCamera('a')

        elif e.type == KEYDOWN and e.key == K_d:
            ani.changeCamera('d')

        elif e.type == KEYDOWN and e.key == K_q:
            ani.changeCamera('q')

        elif e.type == KEYDOWN and e.key == K_z:
            ani.changeCamera('z')
        elif e.type == KEYDOWN and e.key == K_ESCAPE:
            sys.exit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    ani.frame()
    pygame.display.flip()
