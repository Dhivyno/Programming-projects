import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (1500, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Insertion Sort Visualization")

# Set the width of the bars
bar_width = 5

# Set the space between bars
bar_spacing = 2

# Set the height of the bars
bar_heights = [random.randint(10, 350) for i in range(200)]

# Set the initial color of the bars
bar_colors = [(0, 0, 0) for i in range(200)]

# Set the font for the text
font = pygame.font.Font(None, 25)

# Set the initial speed of the sort (in milliseconds)
speed = 10

# Run the game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Pressing the space bar will start/pause the sort
            if event.key == pygame.K_SPACE:
                speed = 0 if speed > 0 else 10
            # Pressing the r key will reset the list and start the sort over
            if event.key == pygame.K_r:
                bar_heights = [random.randint(10, 350) for i in range(200)]
                bar_colors = [(0, 0, 0) for i in range(200)]
                speed = 10

    # Sort the list using insertion sort
    for i in range(1, len(bar_heights)):
        key = bar_heights[i]
        j = i - 1
        while j >= 0 and key < bar_heights[j]:
            bar_heights[j + 1] = bar_heights[j]
            j -= 1
        bar_heights[j + 1] = key

        # Delay the sort
        pygame.time.delay(speed)

        # Clear the screen
        screen.fill((255, 255, 255))

        # Set the colors of the sorted bars
        for i in range(len(bar_heights)):
            bar_colors[i] = (i, i, i)

        # Draw the bars
        for i in range(len(bar_heights)):
            x = i * (bar_width + bar_spacing)
            y = 400 - bar_heights[i]
            rect = pygame.Rect(x, y, bar_width, bar_heights[i])
            pygame.draw.rect(screen, bar_colors[i], rect)

            # Draw the text
            text = font.render("Press SPACE to pause/resume, press R to reset", True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (300, 375)
            screen.blit(text, text_rect)

            # Update the display
        pygame.display.flip()

        # Delay the game loop
        pygame.time.delay(speed)

    # Quit Pygame
    pygame.quit()
