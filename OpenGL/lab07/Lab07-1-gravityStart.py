from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import random
import numpy as np

import CGEngine

# without any particle system
class mySim(CGEngine.Loading):
    def __init__(self, w, h, title):
        super(mySim,self).__init__(w, h, title)

        self.loc = []
        self.vel = []
        self.mass = []
        self.force = []
        self.loc.append(np.array([-15.,  5., 0.])) #loc of ball1
        self.loc.append(np.array([ 15., -5., 0.])) #loc of ball2
        self.vel.append(np.array([  5.,  0., 0.])) #vel of ball1
        self.vel.append(np.array([ -5.,  0., 0.])) #vel of ball2
        self.mass.append(1.0) # mass of first ball
        self.mass.append(20.0) # mass of second ball
        self.force.append(np.array([0., 0., 0.]))#Force of ball 1
        self.force.append(np.array([0., 0., 0.]))#Force of ball 2

        self.cameraAt([0,0,50], [0,0,0])


        self.setBackground(b"bg_cosmos.jpg")

    def initObjects(self):
        self.loc[0] = np.array([-15., 5., 0.])
        self.loc[1] = np.array([15., -5., 0.])
        self.vel[0] = np.array([5., 0., 0.])
        self.vel[1] = np.array([-5., 0., 0.])


    def frame(self):

        dt = self.getDt()

        super(mySim,self).frame()
        # your code here
        
        # compute force
        for i in range(0, 2) :
            self.force[i] = np.array([0.,0.,0.])

        G = 350.0
        dir = self.loc[1] - self.loc[0]
        d = np.linalg.norm(dir)
        dir = dir / d;
        mag = G * self.mass[0] * self.mass[1] / (d*d)
        self.force[0] = mag * dir;
        self.force[1] = -self.force[0]

        # simulate with the force
        for i in range(0, 2) :
            self.vel[i] += self.force[i]*dt/self.mass[i]
            self.loc[i] += self.vel[i]*dt

        for balls in self.loc:
            self.drawBall(balls)

        super(mySim,self).afterFrame()


ani = mySim(500, 500, b"Lab07-1:gravity")
ani.grid(True)


def key(k, x, y):
    if k == b' ':
        if ani.timer.timerRunning:
            ani.timerStop()
        else:
            ani.timerStart()
    elif k == b'r':
        ani.timerReset()
        ani.initObjects()



def draw():
    ani.frame()


ani.start(draw, key)
