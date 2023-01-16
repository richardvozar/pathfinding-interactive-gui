import pygame
import node

WIDTH = 800
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))

# colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# states
EMPTY = 0
WALL = 1
PLAYER_ONE = 2
PLAYER_TWO = 3

board = [[0 for x in range(20)] for y in range(20)]


def draw_grid(WINDOW):
    # WINDOW.fill(WHITE)
    for i in range(50):
        pygame.draw.line(WINDOW, GREY, (0, i * 40), (WIDTH, i * 40))
        pygame.draw.line(WINDOW, GREY, (i * 40, 0), (i * 40, WIDTH))
    pygame.display.update()


def draw_nodes(WINDOW):
    for y in range(20):
        for x in range(20):
            if board[y][x] == 0:
                pygame.draw.rect(WINDOW, WHITE, (x * 40, y * 40, 40, 40))
            elif board[y][x] == 1:
                pygame.draw.rect(WINDOW, BLACK, (x * 40, y * 40, 40, 40))
            elif board[y][x] == 2:
                pygame.draw.rect(WINDOW, PURPLE, (x * 40, y * 40, 40, 40))
            elif board[y][x] == 3:
                pygame.draw.rect(WINDOW, GREEN, (x * 40, y * 40, 40, 40))


def draw_everything(WINDOW):
    draw_nodes(WINDOW)
    draw_grid(WINDOW)
    pygame.display.update()


def build_wall(x, y):
    return 1 if board[y][x] == 0 else board[y][x]


def destroy_wall(x, y):
    return 0 if board[y][x] == 1 else board[y][x]


def draw_map():
    for row in board:
        print(row)


def set_player_one(x, y):
    return 2 if board[y][x] == 0 else board[y][x]


def set_player_two(x, y):
    return 3 if board[y][x] == 0 else board[y][x]


def unset_players():
    for y in range(20):
        for x in range(20):
            if board[y][x] in [2, 3]:
                board[y][x] = 0


def reset_walls():
    for y in range(20):
        for x in range(20):
            if board[y][x] == 1:
                board[y][x] = 0


def main():
    run = True

    is_player_one_set = False
    is_player_two_set = False

    while run:

        draw_everything(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_1:  # set player 1
                    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
                    x = mouse_pos_x // 40
                    y = mouse_pos_y // 40
                    if not is_player_one_set:
                        is_player_one_set = True
                        board[y][x] = set_player_one(x, y)
                if event.key == pygame.K_2:  # set player 2
                    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
                    x = mouse_pos_x // 40
                    y = mouse_pos_y // 40
                    if not is_player_two_set:
                        is_player_two_set = True
                        board[y][x] = set_player_two(x, y)
                if event.key == pygame.K_3:  # unset players
                    unset_players()
                    is_player_one_set = False
                    is_player_two_set = False
                if event.key == pygame.K_4:  # reset walls
                    reset_walls()
                if event.key == pygame.K_5:  # reset everything
                    unset_players()
                    is_player_one_set = False
                    is_player_two_set = False
                    reset_walls()

            if pygame.mouse.get_pressed()[0]:  # left click
                mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
                x = mouse_pos_x // 40
                y = mouse_pos_y // 40
                board[y][x] = build_wall(x, y)
                # print(f'{mouse_pos_x=}, {mouse_pos_y=}')
                # print(f'{x=}, {y=}')
                # draw_map()

            if pygame.mouse.get_pressed()[2]:  # right click
                mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
                x = mouse_pos_x // 40
                y = mouse_pos_y // 40
                board[y][x] = destroy_wall(x, y)
                # print(f'{mouse_pos_x=}, {mouse_pos_y=}')
                # print(f'{x=}, {y=}')

    pygame.quit()


if __name__ == '__main__':
    main()
