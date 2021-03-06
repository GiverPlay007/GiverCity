import pygame

from solids import *

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def main():
    display = (800, 600)
    pygame.init()
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        show_teste()
        pygame.display.flip()
        pygame.time.wait(10)


main()
