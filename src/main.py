#!/bin/python3

import pygame
import math

#pygame setup
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
running = True

G = 6.67 * math.pow(10,-11)
T = 1000

class planet:
    def __init__(self, radius, color, x,y, velocity):
        self.radius = radius
        self.color = color
        self.coords = pygame.Vector2((x,y))
        self.vel = velocity


#making planets
p1 = planet(50, "red", 300,500, pygame.math.Vector2(0.000002,0.000024))
p2 = planet(70, "white", 550,100, pygame.math.Vector2())

bodies = [p1,p2]

def gravForce(o1,o2):
    m = (3.14*math.pow(o1.radius,2))*(3.14*math.pow(o2.radius,2))
    r = pygame.math.Vector2((o1.coords-o2.coords))
    R = pygame.math.Vector2.length_squared(r)
    if R == 0:
        F=0
    else:
        F = G*(m/R)

    f_vec = r.copy()
    f_vec.scale_to_length(F)

    return f_vec

def force_displacement(force, obj):
    a = force/(3.14*math.pow(obj.radius, 2))
    
    s = obj.vel*T + 1/2* a*T*T

    obj.vel = obj.vel + a*T

    return s



#gameloop
while running:
    #getting events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #math and coords shifting
    f_grav = gravForce(bodies[0], bodies[1])
    s = force_displacement(f_grav, bodies[0])
    s1 = force_displacement(f_grav, bodies[1])

    bodies[1].coords += s1
    bodies[0].coords -= s



    #render here

    screen.fill((28,28,28))#fill screen

    for i in bodies:
        pygame.draw.circle(screen,i.color, i.coords, i.radius)
    #render ends

    pygame.display.flip()#put work on screen

    clock.tick(600)#framerate

pygame.quit()

