# MADE BY YYXOF - @TTV_YYXOF / ARSENY / PROD.ARP
import pygame
from pygame.locals import *
import sys
import time

pygame.init()

# Set up the resolution and screen
resolution = (600, 600)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Tic-Tac-Toe")

clock = pygame.time.Clock()

# Load images
background = pygame.image.load("Tik_Tak_Toe_BG.png")
x_image = pygame.image.load("X.png")
o_image = pygame.image.load("O.png")

# Scale X and O images
cell_size = 200
scaled_x_image = pygame.transform.scale(x_image, (cell_size, cell_size))
scaled_o_image = pygame.transform.scale(o_image, (cell_size, cell_size))

# Create a 3x3 grid
grid = [['' for _ in range(3)] for _ in range(3)]

# Set up rectangles for each cell
cell_rects = [[pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size) for col in range(3)] for row in range(3)]

# Main Loop
running = True
current_player = 'X'
game_over = False

def check_winner():
    # Check rows
    for row in range(3):
        if grid[row][0] == grid[row][1] == grid[row][2] != '':
            return True

    # Check columns
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] != '':
            return True

    # Check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] != '' or grid[0][2] == grid[1][1] == grid[2][0] != '':
        return True

    return False

def check_cat():
    return all(all(cell != '' for cell in row) for row in grid)

def reset_game():
    global grid, current_player, game_over
    grid = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN and not game_over:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for row in range(3):
                    for col in range(3):
                        if cell_rects[row][col].collidepoint(mouse_x, mouse_y) and grid[row][col] == '':
                            grid[row][col] = current_player
                            if check_winner():
                                winner_text = f"{current_player} wins!"
                                game_over = True
                            elif check_cat():
                                winner_text = "CAT!"
                                game_over = True
                            else:
                                current_player = 'O' if current_player == 'X' else 'X'

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the grid
    for row in range(3):
        for col in range(3):
            pygame.draw.rect(screen, (255, 255, 255), cell_rects[row][col], 2)
            if grid[row][col] == 'X':
                screen.blit(scaled_x_image, cell_rects[row][col].topleft)
            elif grid[row][col] == 'O':
                screen.blit(scaled_o_image, cell_rects[row][col].topleft)

    if game_over:
        # Display the winner
        font = pygame.font.Font(None, 36)
        text = font.render(winner_text, True, (255, 255, 255))
        screen.blit(text, (resolution[0] // 2 - text.get_width() // 2, resolution[1] // 2))
        pygame.display.flip()
        time.sleep(4)  # Wait for 4 seconds before resetting
        reset_game()

    pygame.display.flip()
    clock.tick(60)

    keys = pygame.key.get_pressed()
    if keys[K_BACKSPACE] and game_over:
        reset_game()

pygame.quit()
sys.exit()
