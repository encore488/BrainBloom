import pygame

# Initialize Pygame
pygame.init()

# Set up display window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sequence Recall Memory Game")

# Show where the player is
player = pygame.Rect(50, 50, 50, 50)

#Game Loop
run = True
while run:
    screen.fill((0, 0, 0))  # Clear the screen with black
    pygame.draw.rect(screen, (255, 0, 0), player)  # Draw the player rectangle

    key = pygame.key.get_pressed()  # Get the current state of the keyboard
    if key[pygame.K_UP]:
        player.move_ip(0, -1)
    elif key[pygame.K_DOWN]:
        player.move_ip(0, 1)
    elif key[pygame.K_LEFT]:
        player.move_ip(-1, 0)
    elif key[pygame.K_RIGHT]:
        player.move_ip(1, 0)

    pygame.display.flip()  # Update the display

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



pygame.quit()  # Quit the game and exit the loop

