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
        for i in range(10) :
            self.particle.append(Particle.Particle())


        self.initObjects()


    def initObjects(self):
        for i in range(10) :
            self.particle[i].set(np.array([myRand(-10,10),5.0,myRand(-10,10)]))
            self.particle[i].setRadius(0.2)
            self.particle[i].setGravity(np.array([0., -9.8, 0.]))

        return



    def frame(self):
        dt = self.getDt()

        super(mySim,self).frame()

        for p in self.particle :
            p.simulate(dt)

        for p in self.particle :
            if p.loc[1] < 0.2:
                p.vel[1] = -1 * p.vel[1]

        for p in self.particle :
            #p.draw()
            p.cdraw([1.0,0.0,0.0,1.0])


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
