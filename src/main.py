#!/bin/python3
import math
import pygame

# --- SCALE ---
KM_PER_PX = 4_500_000   # 10 million km per pixel
M_PER_PX  = KM_PER_PX * 1000

# scaled gravity
G = 6.67e-11 / (M_PER_PX**2)

# time acceleration
TIME_SCALE = 200

CENTER = pygame.Vector2(720, 450)

#masses
SUN     = 1.98847e30
MERCURY = 3.301e23
VENUS   = 4.867e24
EARTH   = 5.972e24
MARS    = 6.417e23
JUPITER = 1.898e27
SATURN  = 5.683e26
URANUS  = 8.681e25
NEPTUNE = 1.024e26

class object:
    def __init__(self, radius, mass, Velocity, Position, color):
        self.radius = radius
        self.mass = mass
        self.Position = Position
        self.Velocity = Velocity
        self.Acceleration = pygame.math.Vector2()
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.Position, self.radius)

    def gravMath(self, objects):
        force = pygame.math.Vector2()
        for i in objects:
            # calc distance
            direction = i.Position - self.Position
            dist = direction.length()

            if dist != 0:
                force += (
                    (G * self.mass * i.mass) / math.pow(dist, 2)
                ) * direction.normalize()
            else:
                continue

        return force


def main():

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1440, 900))
    screen.fill((75, 25, 75))
    clock = pygame.time.Clock()
    running = True




    sun = object(
        21,
        SUN,
        pygame.Vector2(0,0),
        CENTER,
        (255,220,120),
    )

    mercury = make_planet(2, MERCURY, 57.9e6, (200,200,200))
    venus   = make_planet(4, VENUS, 108.2e6, (220,180,120))
    earth   = make_planet(5, EARTH, 149.6e6, (100,150,255))
    mars    = make_planet(3, MARS, 227.9e6, (200,100,80))
    jupiter = make_planet(12, JUPITER, 778.6e6, (220,200,160))
    saturn  = make_planet(10, SATURN, 1.43e9, (210,190,140))
    uranus  = make_planet(7, URANUS, 2.87e9, (180,220,220))
    neptune = make_planet(7, NEPTUNE, 4.50e9, (120,150,255))

    objects = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        dt = clock.tick(60)/1000 * TIME_SCALE

        # getting acceleration for objects
        for i in objects:
            i.Acceleration = i.gravMath(objects) / i.mass

        # updating velocity
        for i in objects:
            i.Velocity += i.Acceleration * dt

        # updating position
        for i in objects:
            i.Position += i.Velocity * dt

        screen.fill((75, 25, 75))
        draw(objects, screen)
        pygame.display.flip()


        clock.tick(60)


def draw(objects, surface):
    for i in objects:
        i.draw(surface)

def make_planet(radius_px, mass, orbit_km, color):
    r = orbit_km / KM_PER_PX
    pos = CENTER + pygame.Vector2(r, 0)
    v = math.sqrt(G * SUN / r)
    vel = pygame.Vector2(0, v)
    return object(radius_px, mass, vel, pos, color)

if __name__ == "__main__":
    main()
