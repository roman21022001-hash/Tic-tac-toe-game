# game.py

import pygame

# ИWe import the Board class from the gameparts package.
from gameparts import Board

pygame.init()

# Здесь определены разные константы, например
# размер ячейки и доски, цвет и толщина линий.
# Эти константы используются при отрисовке графики.
CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

# Настройка экрана.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-tac-toe')
screen.fill(BG_COLOR)


# The function responsible for rendering horizontal and vertical lines.
def draw_lines():
    # Horizontal lines.
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
            LINE_WIDTH
        )

    # ВVertical lines.
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )


# The function responsible for rendering shapes
# (tic‑tac‑toe) on the board.
def draw_figures(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    X_WIDTH
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (
                        col * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    X_WIDTH
                )
            elif board[row][col] == 'O':
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH
                )


# ФThe save_result() function to save the match outcome
def save_result(result):
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def main():
    game = Board()
    current_player = 'X'
    running = True
    draw_lines()

    # The loop processes events such as
    # Clicking the mouse buttons and closing the window.
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]

                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE

                # If you click on an empty cell
                if game.board[clicked_row][clicked_col] == ' ':
                    # Делаем ход
                    game.make_move(clicked_row, clicked_col, current_player)
                    # We are rendering the updated figures.
                    draw_figures(game.board)
                    pygame.display.update()

                    # We’re checking the victory.
                    if game.check_win(current_player):
                        result_message = f'Победили {current_player}'
                        print(result_message)
                        save_result(result_message)
                        running = False
                    # We’re checking for a draw.
                    elif game.is_board_full():
                        result_message = 'Ничья!'
                        print(result_message)
                        save_result(result_message)
                        running = False

                    # We’re changing the player.
                    current_player = 'O' if current_player == 'X' else 'X'

        # Update the game window.
        pygame.display.update()

    # A short pause before closing the window at the end of the game (optional)
    pygame.time.wait(1000)
    pygame.quit()


if __name__ == '__main__':
    main()
