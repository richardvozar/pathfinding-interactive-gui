import pygame
from node import Node

# game
WIDTH = 800
ROWS = 20
COLUMNS = 20
SQUARE_SIZE = WIDTH // ROWS
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
OPEN_SET = 4
CLOSED_SET = 5
ROAD = 6

board = [[0 for x in range(COLUMNS)] for y in range(ROWS)]


def draw_grid(WINDOW):
    # WINDOW.fill(WHITE)
    for i in range(50):
        pygame.draw.line(WINDOW, GREY, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE))
        pygame.draw.line(WINDOW, GREY, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, WIDTH))
    pygame.display.update()


def draw_nodes(WINDOW):
    for y in range(ROWS):
        for x in range(COLUMNS):
            if board[y][x] == 0:
                pygame.draw.rect(WINDOW, WHITE, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif board[y][x] == 1:
                pygame.draw.rect(WINDOW, BLACK, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif board[y][x] == 2:
                pygame.draw.rect(WINDOW, PURPLE, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif board[y][x] == 3:
                pygame.draw.rect(WINDOW, GREEN, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif board[y][x] == 4:
                pygame.draw.rect(WINDOW, ORANGE, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif board[y][x] == 5:
                pygame.draw.rect(WINDOW, YELLOW, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif board[y][x] == 6:
                pygame.draw.rect(WINDOW, TURQUOISE, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


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
    for y in range(ROWS):
        for x in range(COLUMNS):
            if board[y][x] in [2, 3]:
                board[y][x] = 0


def reset_walls():
    for y in range(ROWS):
        for x in range(COLUMNS):
            if board[y][x] == 1:
                board[y][x] = 0


def get_min_f_node(open_set: list[Node]) -> Node:
    min_f: int = open_set[0].f
    min_node: Node = open_set[0]

    for node in open_set:
        if node.f < min_f:
            min_f = node.f
            min_node = node

    return min_node


def get_neighbors(node: Node, diagonal: bool) -> list[tuple[int, int]]:
    x: int = node.x
    y: int = node.y

    is_first_column = x == 0
    is_first_row = y == 0
    is_last_column = x == COLUMNS - 1
    is_last_row = y == ROWS - 1

    isvalid_top_left = x >= 1 and y >= 1 and board[y - 1][x - 1] != 1
    isvalid_top_right = x <= COLUMNS - 2 and y >= 1 and board[y - 1][x + 1] != 1
    isvalid_bot_left = x >= 1 and y <= ROWS - 2 and board[y + 1][x - 1] != 1
    isvalid_bot_right = x <= COLUMNS - 2 and y <= ROWS - 2 and board[y + 1][x + 1] != 1

    neighbors: list[tuple[int, int]] = []

    # left
    if not is_first_column and board[y][x - 1] != 1:
        neighbors.append((x - 1, y))
    # right
    if not is_last_column and board[y][x + 1] != 1:
        neighbors.append((x + 1, y))
    # top
    if not is_first_row and board[y - 1][x] != 1:
        neighbors.append((x, y - 1))
    # bottom
    if not is_last_row and board[y + 1][x] != 1:
        neighbors.append((x, y + 1))

    # diagonal
    if diagonal:
        # top-left
        if isvalid_top_left and (board[x - 1][y] != 1 or board[x][y - 1] != 1):
            neighbors.append((x - 1, y - 1))
        # top-right
        if isvalid_top_right and (board[x + 1][y] != 1 or board[x][y - 1] != 1):
            neighbors.append((x + 1, y - 1))
        # bottom-left
        if isvalid_bot_left and (board[x - 1][y] != 1 or board[x][y + 1] != 1):
            neighbors.append((x - 1, y + 1))
        # bottom-right
        if isvalid_bot_right and (board[x + 1][y] != 1 or board[x][y + 1] != 1):
            neighbors.append((x + 1, y + 1))

    return neighbors


def a_star(start_node: Node, end_node: Node):
    open_set = []
    closed_set = []
    open_set.append(start_node)

    while open_set:
        current = get_min_f_node(open_set)


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

                # TODO: ONLY FOR TESTING, PLEASE REMOVE FROM HERE
                neighbors = get_neighbors(Node(y, x, 0, 0, 0, None, 1), True)
                for x, y in neighbors:
                    board[y][x] = 5
                # TODO: TO HERE

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
