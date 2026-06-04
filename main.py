import pygame
from player import Player 
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    
    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    #Create Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid = AsteroidField()

    #Game Loop
    while True:
        log_state()
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        #Iterate through drawable group and draw the items in the group
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        #This renders all the previous drawings, have it last if you want to see all the things you are "drawing"
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
