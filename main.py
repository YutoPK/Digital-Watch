import pygame
from time import gmtime, strftime

pygame.init()

size_of_window_x = 1300
size_of_window_y = 400


class Proj:
    def __init__(self):
        self.run = True
        self.window = pygame.display.set_mode((size_of_window_x, size_of_window_y))
        self.bg = pygame.image.load("bg.png").convert_alpha()
        self.ar = [[(50, 50, 20, 100), (170, 50, 20, 100), (50, 170, 20, 100), (170, 170, 20, 100), (70, 30, 100, 20), (70, 270, 100, 20)],
                   [(170, 170, 20, 100), (170, 50, 20, 100)],
                   [(170, 50, 20, 100), (50, 170, 20, 100), (70, 30, 100, 20), (70, 150, 100, 20), (70, 270, 100, 20)],
                   [(170, 170, 20, 100), (170, 50, 20, 100), (70, 30, 100, 20), (70, 150, 100, 20), (70, 270, 100, 20)],
                   [(170, 170, 20, 100), (170, 50, 20, 100), (70, 150, 100, 20), (50, 50, 20, 100)],
                   [(50, 50, 20, 100), (170, 170, 20, 100), (70, 30, 100, 20), (70, 150, 100, 20), (70, 270, 100, 20)],
                   [(50, 50, 20, 100), (70, 150, 100, 20), (50, 170, 20, 100), (170, 170, 20, 100), (70, 30, 100, 20), (70, 270, 100, 20)],
                   [(170, 170, 20, 100), (170, 50, 20, 100), (70, 30, 100, 20)],
                   [(50, 50, 20, 100), (170, 50, 20, 100), (70, 150, 100, 20), (50, 170, 20, 100), (170, 170, 20, 100), (70, 30, 100, 20), (70, 270, 100, 20)],
                   [(50, 50, 20, 100), (170, 50, 20, 100), (70, 150, 100, 20), (170, 170, 20, 100), (70, 30, 100, 20), (70, 270, 100, 20)]]

    def draw_line(self, i, s1, s2, r):
        r1 = int(gmtime()[i]) + r
        k1 = r1 // 10
        k2 = r1 % 10
        for i in range(len(self.ar[k1])):
            pygame.draw.rect(self.window, (0, 0, 255), (self.ar[k1][i][0] + s1, self.ar[k1][i][1], self.ar[k1][i][2], self.ar[k1][i][3]))
        for i in range(len(self.ar[k2])):
            pygame.draw.rect(self.window, (0, 0, 255), (self.ar[k2][i][0] + s2, self.ar[k2][i][1], self.ar[k2][i][2], self.ar[k2][i][3]))

    def redraw(self):
        self.window.fill((0, 0, 0))
        pygame.draw.rect(self.window, (0, 0, 255), (375, 200, 25, 25))
        pygame.draw.rect(self.window, (0, 0, 255), (375, 100, 25, 25))
        pygame.draw.rect(self.window, (0, 0, 255), (745, 200, 25, 25))
        pygame.draw.rect(self.window, (0, 0, 255), (745, 100, 25, 25))
        self.draw_line(3, 0, 165, 2)
        self.draw_line(4, 370, 370 + 165, 0)
        self.draw_line(5, 2 * 370, 2 * 370 + 165, 0)
        pygame.display.update()

    def draw_img(self, img, x1, y1):
        self.window.blit(img, (x1, y1))

    def main(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.redraw()


n = Proj()
n.main()