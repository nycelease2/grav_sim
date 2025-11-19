#!/bin/python3

import pygame
import math

#pygame setup
pygame.init()
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
running = True

G = 6.67 * math.pow(10,-11)
T = 1

class planet:
    def __init__(self, radius, color, x,y):
        self.radius = radius
        self.color = color
        self.coords = pygame.Vector2((x,y))
        self.vel = pygame.Vector2()


#making planets
p1 = planet(10, "red", 0,50)
p2 = planet(70, "white", 350,100)

bodies = [p1,p2]

def gravForce(o1,o2):
    m = (3.14*math.pow(o1.radius,2))*(3.14*math.pow(o2.radius,2))
    r = pygame.math.Vector2((o1.coords-o2.coords))
    R = pygame.math.Vector2.length_squared(r)
    if R == 0:
        F=0
    else:
        F = G*(m/R)

    return F

def force_displacement(force, init_velocity, radius):
    a = force/(3.14*math.pow(radius, 2))

    s = init_velocity * T + 1/2*a*math.pow(T,2)
    
    

#gameloop
while running:
    #getting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #math and coords shifting
    f_grav = gravForce(bodies[0], bodies[1])

    bodies[1].coords.move_towards(bodies[0].coords, f_grav)
    bodies[0].coords.move_towards(bodies[1].coords, -f_grav)


    pygame.math.Vector2.update(bodies[1].coords)
    pygame.math.Vector2.update(bodies[0].coords)

    screen.fill((28,28,28))#fill screen

    #render here
    for i in bodies:
        pygame.draw.circle(screen,i.color, i.coords, i.radius)
    #render ends

    pygame.display.flip()#put work on screen

    clock.tick(60)#framerate=60

pygame.quit()

