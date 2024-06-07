import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# Variables declared
DEG2RAD = 3.14159 / 180  # to convert angle from degree to rad
count = 0  # render all parts sequentially.
count1 = 0
launch = False  # state of the rocket launch
sky_color = 0  # chage the background
tx = 0  # translate along X-Axis
ty = 0  # translate along Y-Axis
fumes = 0  # state of the fumes of the rocket


# Function to Display stars
def stars():
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(2)
    glBegin(GL_POINTS)
    for s in range(50):
        x = random.uniform(-400, 400)
        y = random.uniform(-400, 400)
        z = random.uniform(-400, 400)
        glVertex3f(x, y, z)
    glEnd()


# Function to display moon
def moon(radius):
    global tx, ty, DEG2RAD
    glPushMatrix()
    glTranslatef(300 + ty, 500 - tx, 0)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    for i in range(359):
        degInRad = i * DEG2RAD
        glVertex3f(math.cos(degInRad) * radius, math.sin(degInRad) * radius, 0)
    glEnd()
    glPopMatrix()
    tx = tx + 0.1
    ty = ty + 0.1


# Function to display grass
def grass():
    glColor3f(0.0, 0.9, 0.0)
    glBegin(GL_POINTS)
    for s in range(1000):
        x = random.uniform(0, 800)
        y = random.uniform(0, 250)
        glVertex3f(x, y, 0)
    glEnd()


# Function to control the rendering parts of rocket launch
def control():
    global launch, sky_color, count, count1, tx, ty, fumes, DEG2RAD
    count1 += 1
    if count1 == 775659:
        launch = 1
    elif launch == 1 and count1 == 805407:
        rocket_position()
    elif launch == 1 and count1 >= 1000000:
        Moving_Rocket()


def Rocket_on_Ground():
    global launch, count1, DEG2RAD

    # Increase count1 for the animation
    count1 += 1

    # If the rocket is not launched yet
    if launch == 0:
        glClearColor(0.196078, 0.6, 0.8, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Grass
        glColor3f(0, 0.3, 0.0)
        glBegin(GL_POLYGON)
        glVertex3f(0.0, 0.0, 0)
        glVertex3f(0.0, 250.0, 0)
        glVertex3f(300.0, 250.0, 0)
        glVertex3f(600.0, 250.0, 0)
        glVertex3f(600.0, 0.0, 0)
        glEnd()
        grass()

        # Launch pad
        glColor3f(0.0, 0.0, 0.0)
        glBegin(GL_POLYGON)
        glVertex3f(170, 0.0, 0)
        glVertex3f(200, 0.0, 0)
        glVertex3f(200, 180.0, 0)
        glVertex3f(170, 180.0, 0)
        glEnd()
        glLineWidth(5)
        glBegin(GL_LINES)
        glVertex3f(170, 30.0, 0)
        glVertex3f(262, 30.0, 0)

        glVertex3f(170, 130.0, 0)
        glVertex3f(260, 130.0, 0)
        glEnd()

        # Rocket body
        glColor3f(0.5, 0.0, 0.9)
        glBegin(GL_POLYGON)
        glVertex3f(237.5, 20.0, 0)
        glVertex3f(262.5, 20.0, 0)
        glVertex3f(262.5, 120.0, 0)
        glVertex3f(237.5, 120.0, 0)
        glEnd()

        # Rocket top
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_POLYGON)
        glVertex3f(237.5, 120.0, 0)
        glVertex3f(262.5, 120.0, 0)
        glVertex3f(250, 170.0, 0)
        glEnd()

        # Boosters
        glColor3f(0.9, 0.9, 0.0)
        glBegin(GL_POLYGON)
        glVertex3f(237.5, 120.0, 0)
        glVertex3f(217.5, 95.0, 0)
        glVertex3f(237.5, 95.0, 0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f(237.5, 20.0, 0)
        glVertex3f(217.5, 20.0, 0)
        glVertex3f(237.5, 70.0, 0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f(262.5, 20.0, 0)
        glVertex3f(282.5, 20.0, 0)
        glVertex3f(262.5, 70.0, 0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f(262.5, 120.0, 0)
        glVertex3f(262.5, 95.0, 0)
        glVertex3f(282.5, 95.0, 0)
        glEnd()

        # Fumes
        glColor3f(1.0, 0.5, 0)
        glBegin(GL_POLYGON)
        glVertex3f(237.5, 20.0, 0)
        glVertex3f(244.5, 20.0, 0)
        glVertex3f(241, 0.0, 0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f(246.5, 20.0, 0)
        glVertex3f(253.5, 20.0, 0)
        glVertex3f(249.5, 0.0, 0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f(262.5, 20.0, 0)
        glVertex3f(255.5, 20.0, 0)
        glVertex3f(258.5, 0.0, 0)
        glEnd()
        glColor3f(0, 0, 0)
        glBegin(GL_POLYGON)
        glVertex3f(182.5, 15.0, 0)
        glVertex3f(182.5, 0.0, 0)
        glVertex3f(187.5, 0.0, 0)
        glVertex3f(187.5, 10.0, 0)
        glVertex3f(237.5, 10.0, 0)
        glVertex3f(237.5, 15.0, 0)
        glVertex3f(182.5, 15.0, 0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f(312.5, 15.0, 0)
        glVertex3f(312.5, 0.0, 0)
        glVertex3f(307.5, 0.0, 0)
        glVertex3f(307.5, 10.0, 0)
        glVertex3f(262.5, 10.0, 0)
        glVertex3f(262.5, 15.0, 0)
        glVertex3f(312.5, 15.0, 0)
        glEnd()

        # Sky
        glBegin(GL_POLYGON)
        glColor3f(0.4, 0.5, 1.0)
        glVertex3f(600, 600, 0)
        glVertex3f(0, 600, 0)
        glColor3f(0.7, 0.7, 1.0)
        glVertex3f(0, 250, 0)
        glVertex3f(600, 250, 0)
        glEnd()

        glutSwapBuffers()
        glutPostRedisplay()
        glFlush()

    # Rocket has launched
    else:
        control()

def rocket_position():
    global count, fumes

    count += 1

    for i in range(200):
        glClearColor(0.196078, 0.6, 0.8, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Sky
        glBegin(GL_POLYGON)
        glColor3f(0.4, 0.5, 1.0)
        glVertex3f(600, 600, 0)
        glVertex3f(0, 600, 0)
        glColor3f(0.7, 0.7, 1.0)
        glVertex3f(0, 0, 0)
        glVertex3f(600, 0, 0)
        glEnd()

        # Rocket body
        glColor3f(0.5, 0.0, 0.9)
        glBegin(GL_POLYGON)
        glVertex3f(237.5, 20.0 + i, 0)
        glVertex3f(262.5, 20.0 + i, 0)
        glVertex3f(262.5, 120.0 + i, 0)
        glVertex3f(237.5, 120.0 + i, 0)
        glEnd()

        # Rocket top
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_POLYGON)
        glVertex3f(237.5, 120.0 + i, 0)
        glVertex3f(262.5, 120.0 + i, 0)
        glVertex3f(250, 170.0 + i, 0)
        glEnd()

        # Boosters
        glColor3f(0.9, 0.9, 0.0)
        glBegin(GL_POLYGON)
        glVertex3f(237.5, 120.0 + i, 0)
        glVertex3f(217.5, 95.0 + i, 0)
        glVertex3f(237.5, 95.0 + i, 0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f(237.5, 20.0 + i, 0)
        glVertex3f(217.5, 20.0 + i, 0)
        glVertex3f(237.5, 70.0 + i, 0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f(262.5, 20.0 + i, 0)
        glVertex3f(282.5, 20.0 + i, 0)
        glVertex3f(262.5, 70.0 + i, 0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f(262.5, 120.0 + i, 0)
        glVertex3f(262.5, 95.0 + i, 0)
        glVertex3f(282.5, 95.0 + i, 0)
        glEnd()

        # Fumes
        glColor3f(0.556863, 0.137255, 0.419608)
        glBegin(GL_POLYGON)
        glVertex3f(237.5, 20.0 + i, 0)
        glVertex3f(244.5, 20.0 + i, 0)
        glVertex3f(241, 0.0 + i, 0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f(246.5, 20.0 + i, 0)
        glVertex3f(253.5, 20.0 + i, 0)
        glVertex3f(249.5, 0.0 + i, 0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f(262.5, 20.0 + i, 0)
        glVertex3f(255.5, 20.0 + i, 0)
        glVertex3f(258.5, 0.0 + i, 0)
        glEnd()

        # Alternate fumes colors
        if (fumes % 2 == 0):
            glColor3f(1.0, 0.25, 0.0)
        else:
            glColor3f(1.0, 0.816, 0.0)

        glBegin(GL_POLYGON)
        glVertex3f(237.5, 20 + i, 0)
        glVertex3f(234.16, 16.66 + i, 0)
        glVertex3f(230.82, 13.32 + i, 0)
        glVertex3f(227.48, 9.98 + i, 0)
        glVertex3f(224.14, 6.64 + i, 0)
        glVertex3f(220.8, 3.3 + i, 0)
        glVertex3f(217.5, 0 + i, 0)
        glVertex3f(221.56, -5 + i, 0)
        glVertex3f(225.62, -10 + i, 0)
        glVertex3f(229.68, -15 + i, 0)
        glVertex3f(233.74, -20 + i, 0)
        glVertex3f(237.8, -25 + i, 0)
        glVertex3f(241.86, -30 + i, 0)
        glVertex3f(245.92, -35 + i, 0)
        glVertex3f(250, -40 + i, 0)
        glVertex3f(254.06, -35 + i, 0)
        glVertex3f(258.12, -30 + i, 0)
        glVertex3f(262.18, -25 + i, 0)
        glVertex3f(266.24, -20 + i, 0)
        glVertex3f(270.3, -15 + i, 0)
        glVertex3f(274.36, -10 + i, 0)
        glVertex3f(278.42, -5 + i, 0)
        glVertex3f(282.5, 0 + i, 0)
        glVertex3f(278.5, 4 + i, 0)
        glVertex3f(274.5, 8 + i, 0)
        glVertex3f(270.5, 12 + i, 0)
        glVertex3f(266.5, 16 + i, 0)
        glVertex3f(262.5, 20 + i, 0)
        glEnd()

        if (fumes % 2 == 0):
            glColor3f(1.0, 0.816, 0.0)
        else:
            glColor3f(1.0, 0.25, 0.0)

        glBegin(GL_POLYGON)
        glVertex3f(237.5, 20 + i, 0)
        glVertex3f(236.5, 17.5 + i, 0)
        glVertex3f(235.5, 15 + i, 0)
        glVertex3f(234.5, 12.5 + i, 0)
        glVertex3f(233.5, 10 + i, 0)
        glVertex3f(232.5, 7.5 + i, 0)
        glVertex3f(236, 5 + i, 0)
        glVertex3f(239.5, 2.5 + i, 0)
        glVertex3f(243, 0 + i, 0)
        glVertex3f(246.5, -2.5 + i, 0)
        glVertex3f(250, -5 + i, 0)
        glVertex3f(253.5, -2.5 + i, 0)
        glVertex3f(257, 0 + i, 0)
        glVertex3f(260.5, 2.5 + i, 0)
        glVertex3f(264, 5 + i, 0)
        glVertex3f(267.5, 7.5 + i, 0)
        glVertex3f(266.5, 10 + i, 0)
        glVertex3f(265.5, 12.5 + i, 0)
        glVertex3f(264.5, 15 + i, 0)
        glVertex3f(263.5, 17.5 + i, 0)
        glVertex3f(262.5, 20 + i, 0)
        glEnd()

        fumes = fumes + 1

        glutSwapBuffers()
        glutPostRedisplay()
        glFlush()

def Moving_Rocket():
    global sky_color, count, tx, ty
    count += 1
    for i in range(195, 201):
        # Rendering the scene when the rocket is in lower Earth orbit
        if count >= 50:
            glClearColor(0.0, 0.0, 0.0, 1.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            if sky_color == 0:
                glColor3f(0, 0, 1)
                sky_color = 1
            else:
                stars()
                sky_color = 0
        else:
            glClearColor(0.196078, 0.6, 0.8, 1.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        if count >= 100:
            moon(20.0)

        if count <= 300:
            # Rocket body
            glColor3f(0.5, 0.0, 0.9)
            glBegin(GL_POLYGON)
            glVertex3f(237.5, 20.0 + i, 0.0)
            glVertex3f(262.5, 20.0 + i, 0.0)
            glVertex3f(262.5, 120.0 + i, 0.0)
            glVertex3f(237.5, 120.0 + i, 0.0)
            glEnd()

        if count >= 150:
            k = i
            # Core
            glColor3f(1.0, 1.0, 1.0)
            glBegin(GL_POLYGON)
            glVertex3f(237.5, 150.0 + k, 0.0)
            glVertex3f(252.5, 150.0 + k, 0.0)
            glVertex3f(252.5, 120.0 + k, 0.0)
            glVertex3f(237.5, 120.0 + k, 0.0)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex3f(237.5, 140.0 + k, 0.0)
            glVertex3f(230, 140.0 + k, 0.0)
            glVertex3f(230, 130.0 + k, 0.0)
            glVertex3f(237.5, 130.0 + k, 0.0)
            glVertex3f(262.5, 140.0 + k, 0.0)
            glVertex3f(227.5, 140.0 + k, 0.0)
            glVertex3f(227.5, 130.0 + k, 0.0)
            glVertex3f(262.5, 130.0 + k, 0.0)
            glEnd()
        
        else:
            # Rocket top
            glColor3f(1.0, 1.0, 1.0)
            glBegin(GL_POLYGON)
            glVertex3f(237.5, 120.0 + i, 0.0)
            glVertex3f(262.5, 120.0 + i, 0.0)
            glVertex3f(250, 170.0 + i, 0.0)
            glEnd()

        if count <= 120:
            # Boosters
            glColor3f(0.9, 0.9, 0.0)
            glBegin(GL_POLYGON)
            glVertex3f(237.5, 120.0 + i, 0.0)
            glVertex3f(217.5, 95.0 + i, 0.0)
            glVertex3f(237.5, 95.0 + i, 0.0)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex3f(237.5, 20.0 + i, 0.0)
            glVertex3f(217.5, 20.0 + i, 0.0)
            glVertex3f(237.5, 70.0 + i, 0.0)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex3f(262.5, 20.0 + i, 0.0)
            glVertex3f(282.5, 20.0 + i, 0.0)
            glVertex3f(262.5, 70.0 + i, 0.0)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex3f(262.5, 120.0 + i, 0.0)
            glVertex3f(262.5, 95.0 + i, 0.0)
            glVertex3f(282.5, 95.0 + i, 0.0)
            glEnd()

        if count <= 110:
            # Fumes
            glColor3f(0.556863, 0.137255, 0.419608)
            glBegin(GL_POLYGON)
            glVertex3f(237.5, 20.0 + i, 0.0)
            glVertex3f(244.5, 20.0 + i, 0.0)
            glVertex3f(241, 0.0 + i, 0.0)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex3f(246.5, 20.0 + i, 0.0)
            glVertex3f(253.5, 20.0 + i, 0.0)
            glVertex3f(249.5, 0.0 + i, 0.0)
            glEnd()
            glBegin(GL_POLYGON)
            glVertex3f(262.5, 20.0 + i, 0.0)
            glVertex3f(255.5, 20.0 + i, 0.0)
            glVertex3f(258.5, 0.0 + i, 0.0)
            glEnd()

    glutSwapBuffers()
    glutPostRedisplay()
    glFlush()


def iterate():
    glClearColor(0.196078, 0.6, 0.8, 1.0)
    glPointSize(1.0)
    gluPerspective(45, 1, 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5.0)


def Showscreen():
    global launch, sky_color, count, count1, tx, ty, fumes, DEG2RAD
    if launch:
        control()
    else:
        Rocket_on_Ground()

    glutSwapBuffers()
    glutPostRedisplay()
    glFlush()


def main_loop():
    glutMainLoop()

# Initialize OpenGL
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow("Rocket Simulation")

# Set up the OpenGL environment
iterate()

# Register the display function and idle function
glutDisplayFunc(Showscreen)

# Start the main loop
main_loop()
