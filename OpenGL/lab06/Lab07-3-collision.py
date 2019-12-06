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
        for i in range(100) :
            self.particle.append(Particle.Particle())


        self.initObjects()


    def initObjects(self):
        root2 = math.sqrt(2.0)
        for i in range(100) :
            l = np.array([myRand(-6, 6), 0.0, myRand(-6, 6)])
            self.particle[i].set(l,-l*0.1)

            self.particle[i].setRadius(0.2)
            self.particle[i].setGravity(np.array([0., 0.0, 0.]))

        return



    def frame(self):
        dt = self.getDt()


        super(mySim,self).frame()

        for p in self.particle :
            p.simulate(dt)
            p.colHandle()

        for i in range(100) :
            for j in range(i+1, 100) :
                self.particle[i].colHandlePair(self.particle[j])

        for p in self.particle :
            p.cdraw([0.0,0.0,1.0,1.0])


        super(mySim,self).afterFrame()

ani = mySim(500,500, b"Lab07-3:Collision")
ani.grid(True)


def key(k, x, y) :
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
