import pygame
import random
import time
import sys
import colors
import config  # Import the config module

square_color = colors.ROYAL_BLUE # (or whatever color you prefer)
square_x = 10 # Starting x-coordinate for the square
square_y = 20 # Starting y-coordinate for the square

square_vel_x = 2 # Move square 5 pixels to right along x-axis
square_vel_y = 2 # Move square 5 pixels down along y-axis

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events(screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            elif event.key == pygame.K_SPACE:
                
                
                pygame.display.flip()
    return True

def main():
    global square_x, square_y, square_vel_x, square_vel_y   
    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock object
    screen.fill(colors.WHITE)
    pygame.display.flip()
    running = True
    while running:
        running = handle_events(screen)
          # Use color from config
        
        # Draw on the screen
        screen.fill(colors.WHITE)
        text_colors = [colors.BLUE, colors.RED, colors.GREEN, colors.BLACK, colors.PURPLE]
        text_options = ['Apollos', 'Web & App', 'Hello!']
        text_fonts = [
            pygame.font.Font('FreeMono.ttf', 25),
            pygame.font.Font('DejaVuSans.ttf', 25)
            ]
                     
        y = 50
        for text in text_options:
            font = text_fonts[random.randint(0,1)]
                
            if random.randint(0, 1) == 1:
                font.set_bold(True)
            else:
                font.set_bold(False)

            if random.randint(0, 1) == 1:
                font.set_italic(True)
            else:
                font.set_italic(False)

            text_surface = font.render(text, True, text_colors[random.randint(0,4)])
            screen.blit(text_surface, (50, y))
            y += 50
        def draw_rectangle(screen, color, x, y, height, width, thickness):
            pygame.draw.rect(screen, color, (x, y, height, width), thickness)

        draw_rectangle(screen, square_color, square_x, square_y, config.SQUARE_HEIGHT, config.SQUARE_WIDTH, 0)
        pygame.display.flip()
        # Update position of square on screen
        square_x = square_x + square_vel_x
        square_y = square_y + square_vel_y
        # Limit frame rate to certain number of frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
