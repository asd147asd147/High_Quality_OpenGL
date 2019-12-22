# -*- coding: utf-8 -*-

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import random
import numpy as np
import math

import Particle
import CGEngine

del_start_num = 0
add_time = 0.2
del_time = 5

def myRand(start, end) :
    interval = end - start
    return start + interval * random.random()

class snowing :
    def __init__(self):
        self.particle = []
        self.obj_num = 10
        self.add_time = 0.5
        for i in range(10) :
            self.particle.append(Particle.Particle())
        self.initObjects()
        self.sphere = gluNewQuadric()

    def addObjects(self):
        for i in range(10):
            self.particle.append(Particle.Particle())
        for i in range(10):
            l = np.array([myRand(-1000, 1000 ),myRand(-1000, 1000 ), 4000.])
            self.particle[self.obj_num + i].set(l,np.array([l[0]*0.1,0,-l[2]]))
            self.particle[self.obj_num + i].setRadius(30.)
            self.particle[self.obj_num + i].setGravity(np.array([0., -2, 0.]))
            self.particle[self.obj_num + i].addForce(np.array([0., 0., 0.]))
        self.obj_num += 10
        return

    def deleteObjects(self):
        global obj_num, del_start_num

        for i in range(10):
            self.particle.pop(del_start_num + i)
        obj_num -= 10
        del_start_num += 10

    def initObjects(self):
        for i in range(10):
            l = np.array([myRand(-1000, 1000 ),myRand(-1000, 1000 ), 4000.])
            self.particle[i].set(l, np.array([l[0]*0.1,0,-l[2]]))
            self.particle[i].setRadius(20.)
            self.particle[i].setGravity(np.array([0., -2.0, 0.]))
            self.particle[i].addForce(np.array([0., 0., 0.]))


    def frame(self, dt, et):
        global del_time
        pnum = 0

        for p in self.particle :
            p.simulate(dt)
            p.colHandle()

            if et > self.add_time :
                self.add_time += 0.2
                self.addObjects()

            if p.loc[2] < 2000 :
                self.particle.pop(pnum)
                self.obj_num = self.obj_num - 1

        for p in self.particle:
            glPushMatrix()
            glColor([1.0, 1.0, 1.0, 1.0])
            glTranslatef(p.loc[0], p.loc[1], p.loc[2])
            gluSphere(self.sphere, p.radius, 32, 16)
            glPopMatrix()