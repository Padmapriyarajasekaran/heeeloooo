import pygame as pygame
import sys
import random
import time
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PINK = (255, 192, 203)
RED = (255, 0, 0)
BLOCK_SIZE = 20  # Define BLOCK_SIZE here
class Pacman:
    KEY_MAP = {
        pygame.K_UP: (0, -1),
        pygame.K_DOWN: (0, 1),
        pygame.K_LEFT: (-1, 0),
        pygame.K_RIGHT: (1, 0)
    }

    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = (0, 0)

    def update(self, maze, keys_pressed):
        old_x, old_y = self.x, self.y

        self.direction = self.KEY_MAP.get(keys_pressed[pygame.K_UP], self.direction)[0], self.KEY_MAP.get(keys_pressed[pygame.K_UP], self.direction)[1]
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed

        if maze.collides_with_block(int(self.x), int(self.y)):
            self.x, self.y = old_x, old_y

class Ghost:
    MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.vel = 1
        self.color = color
        self.move_index = 0

    def move(self, maze):
        move = Ghost.MOVES[self.move_index]
        new_x = self.x + move[0] * self.vel
        new_y = self.y + move[1] * self.vel

        if not maze.collides_with_block(int(new_x), int(new_y)):
            self.x, self.y = new_x, new_y

        self.move_index += 1
        if self.move_index == len(Ghost.MOVES):
            self.move_index = 0
            random.shuffle(Ghost.MOVES)
class Maze:
    def __init__(self, level_data, BLOCK_SIZE=20):
        self.level_data = level_data
        self.blocks = self.parse_level_data(BLOCK_SIZE)

    def parse_level_data(self, BLOCK_SIZE=None):
        blocks = []
        for row_index, row in enumerate(self.level_data):
            for col_index, cell in enumerate(row):
                if cell == "#":
                    block = (col_index * BLOCK_SIZE, row_index * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                    blocks.append(block)
        return blocks

    def collides_with_block(self, x, y):
        for block in self.blocks:
            if x < block[0] + block[2] and x + BLOCK_SIZE > block[0] and y < block[1] + block[3] and y + BLOCK_SIZE > block[1]:
                return True
        return False

# ... (previous code remains the same)

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pac-Man")
    clock = pygame.time.Clock()

    level_data = [
        "################",
        "#............#",
        "#.####.####.#",
        "#o####.####.#",
        "#.####.####.#",
        "#................",
        "################",
    ]

    maze = Maze(level_data, BLOCK_SIZE=BLOCK_SIZE)  # Pass BLOCK_SIZE to the Maze constructor
    pacman = Pacman(50, 50, 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys_pressed = pygame.key.get_pressed()
        pacman.update(maze, keys_pressed)

        screen.fill(BLACK)

        for block in maze.blocks:
            pygame.draw.rect(screen, WHITE, block)

        pacman_image = pygame.image.load("C:/Users/Kavi Priya/Desktop/th.png")
        screen.blit(pacman_image, (pacman.x, pacman.y))

        pygame.display.flip()
        clock.tick(12)

if __name__ == "__main__":
    main()