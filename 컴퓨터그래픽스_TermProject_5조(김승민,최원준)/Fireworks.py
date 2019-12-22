# -*- coding: utf-8 -*-

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import random
import numpy as np
import math

import Particle
import CGEngine

def myRand(start, end) :
    interval = end - start
    return start + interval * random.random()

class fireworks :
    def __init__(self):
        self.particle = []
        self.obj_num = 10
        self.del_start_num = 0
        self.del_time = 5.
        self.add_time = 2.
        for i in range(10) :
            self.particle.append(Particle.Particle())
        self.initObjects()
        self.sphere = gluNewQuadric()

    def addObjects(self):
        l = np.array([myRand(-1000, 1000), myRand(-1000, 1000), myRand(3500, 4000)])
        for i in range(10):
            self.particle.append(Particle.Particle())
        for i in range(10):
            self.particle[self.obj_num + i].set(l,np.array([myRand(1000.,-1000.),myRand(-1000, 1000), myRand(1000.,-1000.)]))
            self.particle[self.obj_num + i].setRadius(30.)
            self.particle[self.obj_num + i].setGravity(np.array([0., 0, 0.]))
            self.particle[self.obj_num + i].addForce(np.array([0., 0., 0.]))

    def initObjects(self):
        l = np.array([myRand(-1000, 1000), myRand(-1000, 1000), myRand(3500, 4000)])
        for i in range(10):
            self.particle[i].set(l, np.array([myRand(1000.,-1000.),myRand(-1000, 1000), myRand(1000.,-1000.)]))
            self.particle[i].setRadius(40.)
            self.particle[i].setGravity(np.array([0., 0., 0.]))
            self.particle[i].addForce(np.array([0., 0., 0.]))


    def frame(self, dt, et):

        for p in self.particle :
            pnum = 0
            p.simulate(dt)
            p.colHandle()

            p.set(p.loc,np.array([p.vel[0],0.,p.vel[2]]))

            if et > self.add_time :
                self.add_time += 1.
                self.addObjects()

            if -1000>p.loc[0] or p.loc[0]>1000 :
                if 3000 > p.loc[2] or p.loc[2]> 5000 :
                    self.particle.pop(pnum)

        temp_num = 0
        for p in self.particle:
            glPushMatrix()
            if(not temp_num%10):
                glColor([myRand(0.0, 1.0), myRand(0.0, 1.0), myRand(0.0, 1.0), 1.0])
            glTranslatef(p.loc[0], p.loc[1], p.loc[2])
            gluSphere(self.sphere, p.radius, 32, 16)
            glPopMatrix()
            temp_num = temp_num + 1