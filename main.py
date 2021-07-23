import chess
import pygame
import sys
from get_square_num import get_square_num
from chess_wrapper import chessWrapper

board = chess.Board()
white_pawn = chessWrapper(chess.Piece(1, True), 'images/pawn_white.png')
image = pygame.image.load(white_pawn.image)

# VARIABLES TO GO IN PARAM FILE
WHITE = (255, 255, 255)
GREY = (128, 128, 128)


def draw_board(game_window):
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                pygame.draw.rect(game_window, GREY, (i*100, j*100, 100, 100))
            else:
                pygame.draw.rect(game_window, WHITE, (i*100, j*100, 100, 100))


while 1:
    pygame.time.delay(50)  # stops the cpu from dying
    window = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Chess")

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        draw_board(window)
        window.blit(image, (400, 400) )
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(board)
            # move = chess.Move(chess.A2, chess.A4)
            # board.push(move)
            pos = pygame.mouse.get_pos()
            x = pos[0] // 100
            y = pos[1] // 100

            print(get_square_num(x,y))


