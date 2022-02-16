import pygame
import requests

WIDHT = 550
background_color = (251, 247, 245)
grid_color = (52, 123, 200)
buff = 5

response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json()['board']
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]


def insert(win, position):
    font = pygame.font.SysFont("Aerials", 40)
    i, j = position[1], position[0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if grid_original[i - 1][j - 1] != 0:
                    return
                if event.key == 48:
                    grid[i - 1][j - 1] = event.key - 48
                    pygame.draw.rect(win, background_color, (position[0]*50 + buff, position[1]*50+ buff,50 -2*buff , 50 - 2*buff))
                    pygame.display.update()
                    return
                if 0 < event.key - 48 < 10:
                    pygame.draw.rect(win, background_color, (position[0]*50 + buff, position[1]*50+ buff,50 -2*buff , 50 - 2*buff))
                    value = font.render(str(event.key-48), True, (0,0,0))
                    win.blit(value, (position[0]*50 + 15, position[1]*50))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return
                return


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDHT, WIDHT))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)
    font = pygame.font.SysFont("Aerials", 40)

    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()

    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if 0 < grid[i][j] < 10:
                value = font.render(str(grid[i][j]), True, grid_color)
                win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50 + 12))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                xpto = (pos[0] // 50, pos[1] // 50)
                insert(pos, xpto)

            if event.type == pygame.QUIT:
                pygame.quit()
                return


main()
