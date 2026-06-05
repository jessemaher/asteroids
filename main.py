import sys

import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
#Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
#Containers for groups
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0.0
#Game Loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        #Collision Detection: Ship to Asteroid
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            #Collision between shot and asteroid
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        #Fill screen with black
        screen.fill("black")
        #Draw everything in drawable group
        for obj in drawable:
            obj.draw(screen)
        #Render drawings
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
