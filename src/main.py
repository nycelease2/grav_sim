#!/bin/python3

import pygame
import math

G = 6.67 * math.pow(10,-11)

class planet:
    def __init__(self, radius, color, x,y, velocity):
        self.radius = radius
        self.color = color
        self.coords = pygame.Vector2((x,y))
        self.vel = velocity


#taking input for planets
print("Hello user, this is a 2 planet system gravity simulator, please input the prefered values")
print("for your information, screen size is 800 by 600")
p1_r = float(input("radius of first planet: "))
p1_x = float(input("x coordinate: "))
p1_y = float(input("y coordinate: "))
p1_xvel = float(input("x velocity: "))
p1_yvel = float(input("y velocity: "))

p2_r = float(input("radius of second planet: "))
p2_x = float(input("x coordinate: "))
p2_y = float(input("y coordinate: "))
p2_xvel = float(input("x velocity: "))
p2_yvel = float(input("y velocity: "))

T = int(input("prefered time multiplier(I reccomend 1000): "))

#pygame setup
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
running = True

#making planets
p1 = planet(p1_r, "red", p1_x, p1_y, pygame.math.Vector2(p1_xvel, p1_yvel))
p2 = planet(p2_r, "white", p2_x, p2_y, pygame.math.Vector2(p2_xvel, p2_yvel))

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

