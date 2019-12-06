import time
import numpy as np

import CGGame

import math

from OpenGL.GL import *




class myGame(CGGame.Game) :

    def __init__(self, w, h, title):
        super().__init__(w,h,title)
        self.loc = np.array([0.,  0. , 0.])
        self.vel = np.array([0., 10. , 0.])
        self.acc = np.array([0., -9.8, 0.])

    def frame(self):
        dt = self.getDt()
        et = self.getEt()
        super().frame()
        # your code here
        # 가속을 수치적분한다!!!
        self.vel += self.acc * dt
        # 속도를 수치적분한다!!!
        if self.loc[1] < 0:
            self.vel = np.array([0., 10., 0.]);
        self.loc += self.vel * dt

        glColor3f(math.sin(et),math.cos(et),math.sin(et))
        self.drawBall(self.loc)
        super().afterFrame()


game = myGame(1500,1000, b"Lab06-4:Moving Ball with Dynamics")
game.grid(True)

def key(k, x,y) :
    game.timerStart()
def draw() :
    game.frame()

game.start(draw, key)
