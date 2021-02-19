import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import math

pygame.init()
clock = pygame.time.Clock()

windowWidth = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Custer V2')
centerX = windowWidth / 2
centerY = windowHeight / 2
twoPi = 2*3.14159263538979323846
intervals = 50
interval = twoPi/intervals

time = 0
step = 0
x = 0
y = 0
lag = {0:0, 10: 0.02, 20:0.03, 30:0.05, 40:0.08, 50:0.1, 60:0.05, 70:0.08, 80:0.05, 90:0.02, 100:0}

while True:
    surface.fill((0,0,0))  

    pygame.draw.circle(surface, (70, 30, 0), (centerX+20,centerY+15), 30)
    pygame.draw.circle(surface, (70, 30, 0), (centerX-20,centerY+15), 30)

    for radius in range(0, 110, 10):
        x = radius*math.cos(time+lag[radius])
        if 0 < time and time < 3.14159265358979323846:
            y = radius*(0.2*math.sin(time+lag[radius]) + 0.4*(math.sin(time+lag[radius])))
        else : 
            y = radius*(0.6*math.sin(time+lag[radius]) + 0.4*(math.sin(time+lag[radius])))

        x += centerX
        y += centerY
        if radius == 100:
            pygame.draw.circle(surface, (153, 0, 230), (x,y), 20)
        else:
            pygame.draw.circle(surface, (128, 42, 0), (x,y), 20)
 
    time += interval
    if step == intervals : 
        time = twoPi
        step = 0
    step += 1
    clock.tick(60)

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()