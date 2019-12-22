# -*- coding: utf-8 -*-

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import random
import numpy as np
import math

import DrawObject
import Particle
import CGEngine
from math import *
obj_num = 10
del_start_num = 0
add_time = 0.5
del_time = 5


def myRand(start, end):
    interval = end - start
    return start + interval * random.random()


class moon():
    def __init__(self):
        self.particle = []
        self.particle.append(Particle.Particle())

        l = np.array([0., 0., 4000.])
        self.particle[0].set(l)
        self.particle[0].setRadius(100.0)
        self.particle[0].setGravity(np.array([0., 0., 0.]))
        self.particle[0].addForce(np.array([0., 0., 0.]))

        self.sphere = gluNewQuadric()

    def deleteObjects(self):
        global obj_num, del_start_num

        for i in range(10):
            self.particle.pop(del_start_num + i)
        obj_num -= 10
        del_start_num += 10

    def moveObjects(self):

        for i in range(10):
            l = np.array([0., 0., 0.])
            self.particle[i].set(l, l)
            self.particle[i].setRadius(10000.)
            self.particle[i].setGravity(np.array([0., 0., 0.]))
            self.particle[i].addForce(np.array([0., 0., 0.]))

    def frame(self, dt, et):

        glPushMatrix()
        glColor([1.0, 1.0, 0.0, 1.0])
        glTranslatef(cos(et)*2000, self.particle[0].loc[1], sin(et)*2000+2000)
        gluSphere(self.sphere, self.particle[0].radius, 32, 16)
        glPopMatrix()



