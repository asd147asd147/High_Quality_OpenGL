# -*- coding: utf-8 -*-

#OpenGL 모듈
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

#User 모듈
import CGEngine
from Raining import *
from Sunny import *
from moon import *
from Snowing import *
from Fireworks import *
from ObjLoader import *

#추가 모듈
import random
import numpy as np
from math import *


# island false true
# weather 0(sun), 1(cloudy), 2(rain), 3(snow)


class drawObject(CGEngine.Loading):
    def __init__(self, w, h, title):
        super(drawObject, self).__init__(w, h, title)
        self.weather = 0
        self.object = 0
        self.button = 0

        self.rotateTime = 1.0

        self.sun = sunny()
        self.moon = moon()
        self.rain = raining()
        self.snow = snowing()
        self.firework = fireworks()
        self.timerStart()



    def frame(self):
        dt = self.getDt()
        et = self.getEt()

        super(drawObject, self).frame()

        if self.button == 1:
            eye = self.cam.eye
            target = self.cam.target
            up = self.cam.up
            eye[0] = sin(et)*1500
            eye[1] = cos(et)*1500

            self.cam.setPos(eye, target, up)

        if self.weather == 0:
            glEnable(GL_LIGHT0)
            glDisable(GL_LIGHT1)
            glClearColor(0.529412, 0.807843, 0.980392, 1.0)
            self.lighting.LightPosition(cos(et) * 2000, sin(et) * 2000 + 2000)
            self.sun.frame(dt,et)

        elif self.weather == 1:
            glDisable(GL_LIGHT0)
            glEnable(GL_LIGHT1)
            glClearColor(0.1, 0.1, 0.1, 1.0)
            self.lighting.LightSet2()
            self.lighting.LightPosition2(cos(et)*2000,sin(et)*2000+2000)
            self.moon.frame(dt,et)

        elif self.weather == 2 :
            glEnable(GL_LIGHT0)
            glDisable(GL_LIGHT1)
            glClearColor(0.529412, 0.807843, 0.980392, 1.0)
            self.rain.frame(dt,et)


        elif self.weather == 3:
            glEnable(GL_LIGHT0)
            glDisable(GL_LIGHT1)
            glClearColor(0.529412, 0.807843, 0.980392, 1.0)
            self.snow.frame(dt,et)


        elif self.weather == 4:
            glEnable(GL_LIGHT0)
            glDisable(GL_LIGHT1)
            glClearColor(0.529412, 0.807843, 0.980392, 1.0)
            self.firework.frame(dt,et)


        super(drawObject, self).afterFrame()


    def buttonClick(self):
        if self.button == 0:
            self.button = 1
            eye = self.cam.eye
            target = self.cam.target
            up = self.cam.up

            self.cam.setPos(eye, target, up)
        else:
            self.button = 0

    def changeCamera(self, key):
        eye = self.cam.eye
        target = self.cam.target
        up = self.cam.up

        if key == 'w':
            eye[2] += 100
        elif key == 's':
            eye[2] -= 100
        elif key == 'a':
            eye[0] += 100
        elif key == 'd':
            eye[0] -= 100
        elif key == 'q':
            eye[1] -= 100
        elif key == 'z':
            eye[1] += 100
        self.cam.setPos(eye, target, up)