import pygame
import random
import time
import sys
import colors
import config  # Import the config module

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
    return True

def draw_rectangle(screen, color, x, y, height, width, thickness):
            pygame.draw.rect(screen, color, (x, y, height, width), thickness)

def draw_rectangle2(screen, color, x, y, height, width, thickness):
            pygame.draw.rect(screen, color, (x, y, height, width), thickness)


def main():
    # BOTH
    width = 50
    height = 50
    speed_x = 10
    speed_y = 5
    
    # RED
    x = 100
    y = 100

    positive_x = True
    positive_y = True

    # YELLOW
    x2 = 700
    y2 = 500

    positive_x2 = False
    positive_y2 = False

    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock object
    screen.fill(colors.WEIRDLY_SATURATED_SKY_BLUE)
    pygame.display.flip()
    running = True
    while running:
        running = handle_events(screen)
          # Use color from config
        
        # Draw on the screen
        #screen.fill(colors.WEIRDLY_SATURATED_SKY_BLUE)

        if x >= 749:
            positive_x = False
        if x <= 0:
            positive_x = True

        if y >= 549:
            positive_y = False
        if y <= 0:
            positive_y = True
        
        if positive_x:
            x += speed_x
        else:
            x -= speed_x

        if positive_y:
            y += speed_y
        else:
            y -= speed_y

        if x2 >= 749:
            positive_x2 = False
        if x2 <= 0:
            positive_x2 = True

        if y2 >= 549:
            positive_y2 = False
        if y2 <= 0:
            positive_y2 = True
        
        if positive_x2:
            x2 += speed_x
        else:
            x2 -= speed_x

        if positive_y2:
            y2 += speed_y
        else:
            y2 -= speed_y

        draw_rectangle(screen, colors.ARTIFICIAL_BANANA_YELLOW, x, y, height, width, 0)
        draw_rectangle(screen, colors.BLACK, x, y, height, width, 5)
        draw_rectangle2(screen, colors.YOUTUBE_AD_RED, x2, y2, height, width, 0)
        draw_rectangle2(screen, colors.BLACK, x2, y2, height, width, 5)
        pygame.display.flip()
        # Limit frame rate to certain number of frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
