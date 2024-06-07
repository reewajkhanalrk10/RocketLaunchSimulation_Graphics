import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

# Global variables
play_button_clicked = False
countdown_started = False
countdown_value = 3
start_time = 0

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

# Function to display the rectangle after the countdown
def draw_rectangle():
    glColor3f(0.8, 0.2, 0.2)  # Rectangle color
    glBegin(GL_POLYGON)
    glVertex2f(200, 200)
    glVertex2f(400, 200)
    glVertex2f(400, 400)
    glVertex2f(200, 400)
    glEnd()

# Function to display the scene
def Showscreen():
    global play_button_clicked, countdown_started, countdown_value
    glClear(GL_COLOR_BUFFER_BIT)

    if not play_button_clicked:
        draw_play_button()
    elif countdown_started and countdown_value > 0:
        draw_countdown_window()
        display_countdown()
    else:
        draw_rectangle()

    glutSwapBuffers()

# Initialize OpenGL
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow("Play Button")

# Register callbacks
glutDisplayFunc(Showscreen)
glutIdleFunc(Showscreen)
glutMouseFunc(mouse_click)

# Initialize OpenGL settings
glClearColor(0.0, 0.0, 0.0, 1.0)
gluOrtho2D(0.0, 600.0, 0.0, 600.0)

# Start the main loop
glutMainLoop()