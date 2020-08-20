import pygame
from Board import Board
from Tile import Tile

pygame.init()
screen=pygame.display.set_mode((1200, 1200))
pygame.display.set_caption("Minesweeper")
board = Board()
score = 0
rungame = True
font = pygame.font.Font('freesansbold.ttf', 10)
score_font = pygame.font.Font('freesansbold.ttf', 30)

score = 0
while rungame:
    screen.fill((0, 0, 0))
    text = score_font.render("SCORE:  " + str(score), True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (500, 50)
    screen.blit(text, textRect)

    for y in range(0, board.height):
        for x in range(0, board.width):
            if board.get(y, x).visible and board.get(y, x).destruct:
                text = font.render("BOMB", True, (255, 255, 255),
                                   (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (100 + x * int(board.width), 100 + y * int(board.height))
                screen.blit(text, textRect)
            elif board.get(y, x).visible:
                text = font.render(str(board.get(y, x).get_bombs()), True, (255, 255, 255),
                                   (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (100 + x * int(board.width) + int((board.width) * 0.5), 100 + y * int(board.height) + int((board.height) * 0.5))
                screen.blit(text, textRect)
            else:
                pygame.draw.rect(screen, (255, 0, 128),
                                 (100 + x * board.width, 100 + y * board.width, board.width, board.height))
                pygame.draw.rect(screen, (128, 0, 128),
                        (100 + x * board.width, 100 + y * board.width, board.width, board.height), 2)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            pos_x = (x - 100)//board.width
            pos_y = (y - 100)//board.height
            tile: Tile = board.get(pos_y, pos_x)
            if tile.destruct and not tile.visible:
                board.destruct(pos_y, pos_x)
            elif not tile.visible:
                board.calculate_bombs(pos_y, pos_x)
                tile.visible = True
                score += 1

    pygame.display.update()






