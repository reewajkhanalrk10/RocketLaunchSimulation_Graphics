import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import math
import random

# Global variables for play button and countdown
play_button_clicked = False
countdown_started = False
countdown_value = 3
start_time = 0

# Variables for rocket launch
DEG2RAD = 3.14159/180
count = 0
count1 = 0
launch = 0
sky_color = 0
tx = 0
ty = 0
fumes = 0

# Function to draw a play button
def draw_play_button():
    glColor3f(0.3, 0.5, 0.7)  # Button color
    glBegin(GL_POLYGON)
    glVertex2f(250, 250)
    glVertex2f(350, 250)
    glVertex2f(350, 350)
    glVertex2f(250, 350)
    glEnd()

    glColor3f(1.0, 1.0, 1.0)  # Text color
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(280, 280)
    glVertex2f(320, 300)
    glVertex2f(320, 300)
    glVertex2f(280, 320)
    glVertex2f(280, 280)
    glVertex2f(280, 320)
    glEnd()

# Function to draw the countdown window
def draw_countdown_window():
    glColor3f(0.1, 0.1, 0.1)  # Background color
    glBegin(GL_POLYGON)
    glVertex2f(200, 200)
    glVertex2f(400, 200)
    glVertex2f(400, 400)
    glVertex2f(200, 400)
    glEnd()

# Function to display the countdown
def display_countdown():
    global countdown_value, start_time
    glColor3f(1.0, 1.0, 1.0)  # Text color
    glRasterPos2f(300, 300)
    glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(str(countdown_value)))

    # Check if countdown value needs to be updated
    current_time = time.time()
    if current_time - start_time > 1:
        start_time = current_time
        countdown_value -= 1

# Function to handle mouse clicks
def mouse_click(button, state, x, y):
    global play_button_clicked, countdown_started, start_time
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if not play_button_clicked and 250 < x < 350 and 250 < y < 350:
            play_button_clicked = True
            countdown_started = True
            start_time = time.time()

# Function to display stars
def stars():
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(2)
    glBegin(GL_POINTS)
    for _ in range(50):
        x = random.randint(0, 800)
        y = random.randint(0, 800)
        glVertex2i(x, y)
    glEnd()

# Function to display the moon
def moon(radius):  
    global tx, ty, DEG2RAD
    glBegin(GL_POLYGON)
    for i in range(359):
        degInRad = i * DEG2RAD
        glVertex2f(300 + ty + math.cos(degInRad) * radius, 500 - tx + math.sin(degInRad) * radius)
    glEnd()
    tx += 0.1
    ty += 0.1

# Function to display grass
def grass():
    glColor3f(0.0, 0.9, 0.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    for _ in range(1000):
        x = random.randint(0, 800)
        y = random.randint(0, 250)
        glVertex2i(x, y)
    glEnd()

# Function to control the rendering parts of the rocket launch
def control():
    global launch, sky_color, count, count1, tx, ty, fumes, DEG2RAD
    count1 += 1
    if count1 == 775659:
        launch = 1
    elif launch == 1 and count1 == 805407:
        rocket_position()
    elif launch == 1 and count1 >= 1000000:
        Moving_Rocket()

# Function to display rocket scene on the ground
def Rocket_on_Ground():
    global launch, count1, DEG2RAD
    count1 += 1
    if count1 == 150:
        launch = 1
    if launch == 0:
        glClearColor(0.196078, 0.6, 0.8, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
       
        # Grass
        glColor3f(0, 0.3, 0.0)
        glBegin(GL_POLYGON)
        glVertex2f(0.0, 0.0)
        glVertex2f(0.0, 250.0)
        glVertex2f(300.0, 250.0)
        glVertex2f(600.0, 250.0)
        glVertex2f(600.0, 0.0)
        glEnd()
        grass()

        # Launch pad
        glColor3f(0.0, 0.0, 0.0)
        glBegin(GL_POLYGON)
        glVertex2f(170, 0.0)
        glVertex2f(200, 0.0)
        glVertex2f(200, 180.0)
        glVertex2f(170, 180.0)
        glEnd()
        glLineWidth(5)
        glBegin(GL_LINES)
        glVertex2f(170, 30.0)
        glVertex2f(262, 30.0)

        glVertex2f(170, 130.0)
        glVertex2f(260, 130.0)
        glEnd()

        # Rocket body
        glColor3f(0.5, 0.0, 0.9)
        glBegin(GL_POLYGON)
        glVertex2f(237.5, 20.0)
        glVertex2f(262.5, 20.0)
        glVertex2f(262.5, 120.0)
        glVertex2f(237.5, 120.0)
        glEnd()

        # Rocket top
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_POLYGON)
        glVertex2f(237.5, 120.0)
        glVertex2f(262.5, 120.0)
        glVertex2f(250, 170.0)
        glEnd()

        # Boosters
        glColor3f(0.9, 0.9, 0.0)
        glBegin(GL_POLYGON)
        glVertex2f(237.5, 120.0)
        glVertex2f(217.5, 95.0)
        glVertex2f(237.5, 95.0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(237.5, 20.0)
        glVertex2f(217.5, 20.0)
        glVertex2f(237.5, 70.0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(262.5, 20.0)
        glVertex2f(282.5, 20.0)
        glVertex2f(262.5, 70.0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(262.5, 120.0)
        glVertex2f(262.5, 95.0)
        glVertex2f(282.5, 95.0)
        glEnd()

        # Fumes
        glColor3f(1.0, 0.5, 0)
        glBegin(GL_POLYGON)
        glVertex2f(237.5, 20.0)
        glVertex2f(244.5, 20.0)
        glVertex2f(241, 0.0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(246.5, 20.0)
        glVertex2f(253.5, 20.0)
        glVertex2f(249.5, 0.0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(262.5, 20.0)
        glVertex2f(255.5, 20.0)
        glVertex2f(258.5, 0.0)
        glEnd()
        glColor3f(1.0, 1.0, 0)
        glBegin(GL_POLYGON)
        glVertex2f(237.5, 20.0)
        glVertex2f(242, 20.0)
        glVertex2f(240, 10.0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(246.5, 20.0)
        glVertex2f(252, 20.0)
        glVertex2f(249.5, 10.0)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(262.5, 20.0)
        glVertex2f(257.5, 20.0)
        glVertex2f(260.5, 10.0)
        glEnd()
        glFlush()

# Function to handle rocket launch movements
def rocket_position():
    global count, count1, tx, ty, DEG2RAD
    count += 1
    ty += 0.5
    tx -= 1
    if count <= 500:
        rocket_position()
    else:
        Moving_Rocket()

# Function to handle rocket moving in the sky
def Moving_Rocket():
    global count, count1, launch, sky_color, tx, ty, fumes, DEG2RAD
    count1 += 1
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Drawing stars
    stars()

    # Drawing moon
    glColor3f(1.0, 1.0, 1.0)
    moon(50)

    # Drawing rocket
    glColor3f(0.5, 0.0, 0.9)
    glBegin(GL_POLYGON)
    glVertex2f(237.5 + tx, 20.0 + ty)
    glVertex2f(262.5 + tx, 20.0 + ty)
    glVertex2f(262.5 + tx, 120.0 + ty)
    glVertex2f(237.5 + tx, 120.0 + ty)
    glEnd()

    # Drawing rocket top
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(237.5 + tx, 120.0 + ty)
    glVertex2f(262.5 + tx, 120.0 + ty)
    glVertex2f(250 + tx, 170.0 + ty)
    glEnd()

    # Drawing boosters
    glColor3f(0.9, 0.9, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(237.5 + tx, 120.0 + ty)
    glVertex2f(217.5 + tx, 95.0 + ty)
    glVertex2f(237.5 + tx, 95.0 + ty)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(237.5 + tx, 20.0 + ty)
    glVertex2f(217.5 + tx, 20.0 + ty)
    glVertex2f(237.5 + tx, 70.0 + ty)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(262.5 + tx, 20.0 + ty)
    glVertex2f(282.5 + tx, 20.0 + ty)
    glVertex2f(262.5 + tx, 70.0 + ty)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(262.5 + tx, 120.0 + ty)
    glVertex2f(262.5 + tx, 95.0 + ty)
    glVertex2f(282.5 + tx, 95.0 + ty)
    glEnd()

    # Drawing fumes
    if count1 % 2 == 0:
        glColor3f(1.0, 0.5, 0)
        glBegin(GL_POLYGON)
        glVertex2f(237.5 + tx, 20.0 + ty)
        glVertex2f(244.5 + tx, 20.0 + ty)
        glVertex2f(241 + tx, 0.0 + ty)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(246.5 + tx, 20.0 + ty)
        glVertex2f(253.5 + tx, 20.0 + ty)
        glVertex2f(249.5 + tx, 0.0 + ty)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(262.5 + tx, 20.0 + ty)
        glVertex2f(255.5 + tx, 20.0 + ty)
        glVertex2f(258.5 + tx, 0.0 + ty)
        glEnd()
        glColor3f(1.0, 1.0, 0)
        glBegin(GL_POLYGON)
        glVertex2f(237.5 + tx, 20.0 + ty)
        glVertex2f(242 + tx, 20.0 + ty)
        glVertex2f(240 + tx, 10.0 + ty)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(246.5 + tx, 20.0 + ty)
        glVertex2f(252 + tx, 20.0 + ty)
        glVertex2f(249.5 + tx, 10.0 + ty)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex2f(262.5 + tx, 20.0 + ty)
        glVertex2f(257.5 + tx, 20.0 + ty)
        glVertex2f(260.5 + tx, 10.0 + ty)
        glEnd()
    glFlush()

# Display function to render the scene
def display():
    global play_button_clicked, countdown_started, countdown_value

    glClear(GL_COLOR_BUFFER_BIT)

    if not play_button_clicked:
        draw_play_button()
    elif countdown_started:
        if countdown_value > 0:
            draw_countdown_window()
            display_countdown()
        else:
            countdown_started = False
            launch = 1  # Start the rocket launch
    else:
        if launch == 0:
            Rocket_on_Ground()
        elif launch == 1:
            control()
            Moving_Rocket()

    glutSwapBuffers()

# Function to update the screen
def update(value):
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

# Function to initialize OpenGL settings
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 800.0, 0.0, 600.0)

# Main function to start the program
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Rocket Launch Simulation")
    init()
    glutDisplayFunc(display)
    glutMouseFunc(mouse_click)
    glutTimerFunc(16, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
