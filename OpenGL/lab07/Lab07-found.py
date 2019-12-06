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

class mySim(CGEngine.Loading) :

    def __init__(self, w, h, title):
        super(mySim,self).__init__(w,h,title)

        self.particle = []
        self.particle2 = []
        for i in range(100) :
            self.particle.append(Particle.Particle())
        for i in range(100) :
            self.particle2.append(Particle.Particle())


        self.initObjects()


    def initObjects(self):
        for i in range(100) :
            self.particle[i].set(np.array([myRand(-0.1,0.1),0.1,myRand(-0.1,0.1)]), np.array([myRand(-3,3),myRand(8,11),myRand(-3,3)]))
            self.particle[i].setRadius(0.05)
            self.particle[i].setGravity(np.array([0., -9.8, 0.]))
        for i in range(100) :
            self.particle2[i].set(np.array([myRand(-0.1,0.1),0.1,myRand(-0.1,0.1)]), np.array([myRand(-3,3),myRand(8,11),myRand(-3,3)]))
            self.particle2[i].setRadius(0.05)
            self.particle2[i].setGravity(np.array([0., -9.8, 0.]))
        return

    def frame(self):
        dt = self.getDt()
        et = self.getEt()

        if int(et % 4) == 0:
            for p in self.particle :
                p.set(np.array([myRand(-0.1,0.1),0.1,myRand(-0.1,0.1)]), np.array([myRand(-3,3),myRand(8,11),myRand(-3,3)]))

        super(mySim,self).frame()

        for p in self.particle :
            p.simulate(dt)

        for p in self.particle :
            if p.loc[1] < 0.1:
                p.vel[1] = -1 * p.vel[1]/3

        for p in self.particle :
            #p.draw()
            p.cdraw([0.0,0.5,1.0,1.0])


        if int(et % 5) == 0:
            for p in self.particle2 :
                p.set(np.array([myRand(-0.1,0.1),0.1,myRand(-0.1,0.1)]), np.array([myRand(-3,3),myRand(8,11),myRand(-3,3)]))

        for p in self.particle2 :
            p.simulate(dt)

        for p in self.particle2 :
            if p.loc[1] < 0.1:
                p.vel[1] = -1 * p.vel[1]/3

        for p in self.particle2 :
            #p.draw()
            p.cdraw([0.0,0.5,1.0,1.0])

        super(mySim,self).afterFrame()

ani = mySim(500,500, b"Lab08-4 : Gravity")
ani.grid(True)


def key(k, x,y) :
    if k == b' ':
        if ani.timer.timerRunning:
            ani.timerStop()
        else:
            ani.timerStart()
    if k == b'r':
        ani.initObjects()


def draw():
    ani.frame()

ani.start(draw, key)
