import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def init():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslate(0.0, 0.0, -5)

def draw_particle():
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex3fv((0, 0, 0))
    glEnd()

def animate():
    clock = pygame.time.Clock()

    angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_particle()
        pygame.display.flip()
        clock.tick(60)

init()
animate()