from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time
import numpy as np

import CGGame
from math import *


class myGame(CGGame.Game) :

    def frame(self):
        dt = self.getDt()
        et = self.getEt()

        super().frame()
        # your code here
        self.drawBall([5.0*cos(et),0, 5.0*sin(et)])
        super().afterFrame()

game = myGame(1500,1000, b"Lab06-3:Moving Ball with CGGame")
game.grid(True)

def key(k, x,y) :
    game.timerStart()
def draw() :
    game.frame()

game.start(draw, key)
