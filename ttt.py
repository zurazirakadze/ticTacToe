import sys

import numpy as np
import pygame

pygame.init()
pygame.display.set_caption(' CREATED BY ZURA ZIRAKADZE')


class TicTacToe:
    def __init__(self):
        self.WIDTH = 600
        self.HEIGHT = self.WIDTH
        self.BOARD_ROWS = 3
        self.BOARD_COLS = 3
        self.SQUARE_SIZE = self.WIDTH // self.BOARD_COLS
        self.player = 1
        self.CIRCLE_COLOR = (239, 231, self.SQUARE_SIZE)
        self.color = None
        self.game_over = False
        # rgb: red green blue
        self.RED = (255, 0, 0)
        self.BG_COLOR = (28, 170, 156)
        self.CIRCLE_RADIUS = self.SQUARE_SIZE // 3
        self.CIRCLE_WIDTH = 15
        self.CROSS_WIDTH = 25
        self.SPACE = self.SQUARE_SIZE // 4
        self.CROSS_COLOR = (66, 66, 66)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen.fill(self.BG_COLOR)
        self.LINE_WIDTH = 15
        self.LINE_COLOR = (23, 145, 135)
        self.board = np.zeros((self.BOARD_ROWS, self.BOARD_COLS))

    def draw_lines(self) -> None:
        pygame.draw.line(self.screen, self.LINE_COLOR, (0, self.SQUARE_SIZE), (self.WIDTH, self.SQUARE_SIZE),
                         self.LINE_WIDTH)
        pygame.draw.line(self.screen, self.LINE_COLOR, (0, 2 * self.SQUARE_SIZE), (self.WIDTH, 2 * self.SQUARE_SIZE),
                         self.LINE_WIDTH)
        pygame.draw.line(self.screen, self.LINE_COLOR, (self.SQUARE_SIZE, 0), (self.SQUARE_SIZE, self.HEIGHT),
                         self.LINE_WIDTH)
        pygame.draw.line(self.screen, self.LINE_COLOR, (2 * self.SQUARE_SIZE, 0), (2 * self.SQUARE_SIZE, self.HEIGHT),
                         self.LINE_WIDTH)

    def mainLoop(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    clicked_row = int(mouseY // self.SQUARE_SIZE)
                    clicked_col = int(mouseX // self.SQUARE_SIZE)
                    if self.available_square(clicked_row, clicked_col):

                        if self.player == 1:
                            self.mark_square(clicked_row, clicked_col, 1)
                            if self.check_win(self.player):
                                self.game_over = True
                            self.player = 2
                        elif self.player == 2:
                            self.mark_square(clicked_row, clicked_col, 2)
                            if self.check_win(self.player):
                                self.game_over = True
                            self.player = 1
                        print(self.board)
                        self.draw_figures()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.restart()
                        self.game_over = False
            pygame.display.update()

    def mark_square(self, row: int, col: int, player) -> None:
        self.board[row][col] = player
        print(self.board)

    def available_square(self, row: int, col: int) -> bool:
        if self.board[row][col] == 0:
            return True
        else:
            return False

    def is_board_full(self) -> bool:
        for row in range(self.BOARD_ROWS):
            for col in range(self.BOARD_COLS):
                if self.board[row][col] == 0:
                    return False
        return True

    def draw_figures(self) -> None:
        for row in range(self.BOARD_ROWS):
            for col in range(self.BOARD_COLS):
                if self.board[row][col] == 1:
                    pygame.draw.circle(self.screen, self.CIRCLE_COLOR,
                                       (int(col * self.SQUARE_SIZE + self.SQUARE_SIZE / 2),
                                        int(row * self.SQUARE_SIZE + self.SQUARE_SIZE / 2)), self.CIRCLE_RADIUS,
                                       self.CIRCLE_WIDTH)
                elif self.board[row][col] == 2:
                    pygame.draw.line(self.screen, self.CROSS_COLOR,
                                     (col * self.SQUARE_SIZE + self.SPACE,
                                      row * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE),
                                     (col * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE,
                                      row * self.SQUARE_SIZE + self.SPACE),
                                     self.CROSS_WIDTH)
                    pygame.draw.line(self.screen, self.CROSS_COLOR,
                                     (col * self.SQUARE_SIZE + self.SPACE, row * self.SQUARE_SIZE + self.SPACE),
                                     (col * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE,
                                      row * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE), self.CROSS_WIDTH)

    def check_win(self, player) -> bool:
        # vertical in check
        for col in range(self.BOARD_COLS):
            if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
                self.draw_vertical_winning_line(col, player)
                return True
        # horizontal win check
        for row in range(self.BOARD_ROWS):
            if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
                self.draw_horizontal_winning_line(row, player)
                return True

        # asc diagonal win check
        if self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
            self.draw_asc_diagonal(player)
            return True
        # desc diagonal win check
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            self.draw_desc_diagonal(player)
            return True
        return False

    def draw_vertical_winning_line(self, col, player) -> None:
        posX = col * self.SQUARE_SIZE + 100
        if player == 1:
            self.color = self.CIRCLE_COLOR
        elif player == 2:
            self.color = self.CROSS_COLOR
        pygame.draw.line(self.screen, self.color, (posX, 15), (posX, self.HEIGHT - 15), 15)

    def draw_horizontal_winning_line(self, row, player) -> None:
        posY = row * self.SQUARE_SIZE + 100
        if player == 1:
            self.color = self.CIRCLE_COLOR
        elif player == 2:
            self.color = self.CROSS_COLOR
        pygame.draw.line(self.screen, self.color, (15, posY), (self.WIDTH - 15, posY), 15)

    def draw_asc_diagonal(self, player) -> None:
        if player == 1:
            self.color = self.CIRCLE_COLOR
        elif player == 2:
            self.color = self.CROSS_COLOR
        pygame.draw.line(self.screen, self.color, (15, self.HEIGHT - 15), (self.WIDTH - 15, 15), 15)

    def draw_desc_diagonal(self, player) -> None:
        if player == 1:
            self.color = self.CIRCLE_COLOR
        elif player == 2:
            self.color = self.CROSS_COLOR
        pygame.draw.line(self.screen, self.color, (15, 15), (self.WIDTH - 15, self.HEIGHT - 15), 15)

    def restart(self) -> None:
        self.screen.fill(self.BG_COLOR)
        self.draw_lines()
        self.player = 1
        for row in range(self.BOARD_ROWS):
            for col in range(self.BOARD_COLS):
                self.board[row][col] = 0


if __name__ == "__main__":
    obj = TicTacToe()
    obj.draw_lines()
    obj.mainLoop()
