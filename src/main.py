#!/bin/python3
import math
import pygame

# --- SCALE ---
KM_PER_PX = 2000
M_PER_PX  = 2_000_000

# scaled gravity
G = 6.67e-11 / (M_PER_PX**2)

# time acceleration
TIME_SCALE = 2000

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
    screen = pygame.display.set_mode((640, 480))
    screen.fill((75, 25, 75))
    clock = pygame.time.Clock()
    running = True


    earth = object(
        8,
        5.97e24,
        pygame.Vector2(0, 0),  # temporary
        pygame.Vector2(320, 240),
        (50, 100, 255),
    )

    MOON_DIST = 384400 / KM_PER_PX

    moon1 = object(
        3,
        7.34767309e22,
        pygame.Vector2(0, 0),  # temporary
        earth.Position + pygame.Vector2(MOON_DIST, 0),
        (255, 255, 255),
    )

    moon2 = object(
        3,
        7.34767309e22,
        pygame.Vector2(0, 0),  # temporary
        earth.Position - pygame.Vector2(MOON_DIST, 0),
        (255, 100, 0),
    )

    # --- orbital velocities ---
    v_moon = math.sqrt(G * earth.mass / MOON_DIST)

    moon2.Velocity = pygame.Vector2(0, -v_moon)
    moon1.Velocity  = pygame.Vector2(0,  v_moon)
    earth.Velocity = pygame.Vector2(0, -v_moon * (moon1.mass / earth.mass))

    objects = [moon1, earth, moon2]

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


if __name__ == "__main__":
    main()
