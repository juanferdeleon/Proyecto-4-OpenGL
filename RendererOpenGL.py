import pygame
from pygame.locals import *

from gl import Renderer, Model
import glm
import shaders

deltaTime = 0.0

# Inicializacion de pygame
pygame.init()
clock = pygame.time.Clock()
screenSize = (960, 540)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)

# Inicializacion de nuestro Renderer en OpenGL
r = Renderer(screen)
r.camPosition.z = 3
r.pointLight.x = 5

r.setShaders(shaders.vertex_shader, shaders.fragment_shader)

# Model 1: Face
r.modelList.append(Model('./Models/model.obj', './Models/model.bmp', scale = glm.vec3(1, 1, 1)))

# Model 2: Eye Ball
r.modelList.append(Model('./Models/eyeball.obj', './Models/Eye_D.bmp', scale = glm.vec3(0.5, 0.5, 0.5)))

# Model 3: Lolipop
r.modelList.append(Model('./Models/pinwihell_lolipop.obj', './Models/Christmas Candy Caneeeeee_pinwihell_lolipop1_BaseColor.bmp', scale = glm.vec3(0.15, 0.15, 0.15)))
r.modelList[2].position.y = -2

# Model 4: Spider
r.modelList.append(Model('./Models/Only_Spider_with_Animations_Export.obj', './Models/Spinnen_Bein_tex.bmp', scale = glm.vec3(0.01, 0.01, 0.01)))
r.modelList[3].position.y = -0.5

isPlaying = True
while isPlaying:

    # Para revisar si una tecla esta presionada
    keys = pygame.key.get_pressed()

    # Move cam
    if keys[K_d]:
        r.camPosition.x += 1 * deltaTime
    if keys[K_a]:
        r.camPosition.x -= 1 * deltaTime
    if keys[K_w]:
        r.camPosition.z -= 1 * deltaTime
    if keys[K_s]:
        r.camPosition.z += 1 * deltaTime


    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isPlaying = False
        elif ev.type == pygame.KEYDOWN:
            # para revisar en el momento que se presiona una tecla
            if ev.key == pygame.K_1:
                r.filledMode()
            elif ev.key == pygame.K_2:
                r.wireframeMode()
            elif ev.key == pygame.K_ESCAPE:
                isPlaying = False
            elif ev.key == pygame.K_SPACE:
                r.activeModel = (r.activeModel + 1) % len(r.modelList)

    # Main Renderer Loop
    r.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000


pygame.quit()
