# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
class Lighting:
    def __init__(self):
        self.Ld = [1., 1., 1., 1.]
        self.Ls = [1., 1., 1., 1.]
        self.La = [0.6, 0.6, 0.6, 1.]
        self.Md = [1, 1, 0.3, 1.]
        self.Ms = [1, 1, 1, 1.]
        self.Ma = [0., 0., 0., 1.]
        self.Lpos = [1500., 1000., 1500.,1.]
        self.shininess = [127]


    def LightSet(self):
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.Ld)
        glLightfv(GL_LIGHT0, GL_SPECULAR, self.Ls)
        glLightfv(GL_LIGHT0, GL_AMBIENT, self.La)

        glMaterialfv(GL_FRONT, GL_DIFFUSE, self.Md)
        glMaterialfv(GL_FRONT, GL_SPECULAR, self.Ms)
        glMaterialfv(GL_FRONT, GL_AMBIENT, self.Ma)
        glMaterialfv(GL_FRONT, GL_SHININESS, self.shininess)
        glMaterialfv(GL_FRONT, GL_EMISSION, [0.1, 0.1, 0.1, 0.0])

    def LightSet2(self):
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT1)
        glEnable(GL_COLOR_MATERIAL)
        glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.2,0.2,0.2])
        glLightfv(GL_LIGHT1, GL_SPECULAR,[0.2,0.2,0.2])
        glLightfv(GL_LIGHT1, GL_AMBIENT, [0.2,0.2,0.2])


        glMaterialfv(GL_FRONT, GL_DIFFUSE,[0.2,0.2,0.2])
        glMaterialfv(GL_FRONT, GL_SPECULAR,[0.2,0.2,0.2])
        glMaterialfv(GL_FRONT, GL_AMBIENT, [0.,0.,0.,1.0])
        glMaterialfv(GL_FRONT, GL_EMISSION, [0.1, 0.1, 0.1, 0.0])
        glMaterialfv(GL_FRONT, GL_SHININESS, [10])

    def LightPosition(self, dt_x, dt_y):
        glLightfv(GL_LIGHT0, GL_POSITION, [dt_x, 0, dt_y, 1.])

    def LightPosition2(self,dt_x,dt_y):

        glLightfv(GL_LIGHT1, GL_POSITION, [dt_x, 0, dt_y,1.])

    def SetLightPos(self, pos):
        self.Lpos = pos

