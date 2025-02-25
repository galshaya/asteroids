import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    

    # Create our player at the center of the screen
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    
    # Create groups and set up containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroid, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shot)
    player = Player(x, y)
    asteroidfeild = AsteroidField()


    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Clear screen with black backgroundß
        screen.fill((0, 0, 0))
        
        # Update all objects
        updatable.update(dt)

        for a in asteroid:
            for s in shot:
                if a.check_collisions(s):
                    a.split()
                    s.kill()
            if a.check_collisions(player):
                print("Game Over")
                pygame.quit()
        
    
        # Draw all objects
        for drawable_obj in drawable:
            drawable_obj.draw(screen)
        
        # Update display
        pygame.display.flip()
        
        # Control frame rate and get dt
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()