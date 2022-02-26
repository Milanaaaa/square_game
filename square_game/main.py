import random
import pygame


def inter(x1, y1, x2, y2, db1, db2):
    self_x1 = x1
    self_x2 = x1 + db1
    self_y1 = y1
    self_y2 = y1 + db1

    other_x1 = x2
    other_x2 = x2 + db2
    other_y1 = y2
    other_y2 = y2 + db2

    s1 = (self_x1 > other_x1 and self_x1 < other_x2) or (self_x2 > other_x1 and self_x2 < other_x2)
    s2 = (self_y1 > other_y1 and self_y1 < other_y2) or (self_y2 > other_y1 and self_y2 < other_y2)
    s3 = (other_x1 > self_x1 and other_x1 < self_x2) or (other_x2 > self_x1 and other_x2 < self_x2)
    s4 = (other_y1 > self_y1 and other_y1 < self_y2) or (other_y2 > self_y1 and other_y2 < self_y2)
    if ((s1 and s2) or (s3 and s4)) or ((s1 and s4) or (s3 and s2)):
        return True
    else:
        return False


class Square:
    def __init__(self, listSquares):
        self.color = random.choice(((66, 170, 255), (255, 255, 0), (0, 255, 255), (253, 233, 16), (255, 163, 67),
                                    (255, 73, 108), (102, 0, 255), (153, 50, 204)))
        self.side = random.randrange(5, 50)
        self.speed = random.choice((0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1))
        self.shape = pygame.Surface((self.side, self.side))
        self.x = random.choice((random.randrange(1, 190 - self.side), random.randrange(210, 400 - self.side)))
        self.y = random.choice((random.randrange(1, 190 - self.side), random.randrange(210, 400 - self.side)))


class MainSquare:
    def __init__(self, side, color):
        self.color = color
        self.side = side
        self.speed = 10
        self.x = 190
        self.y = 190
        self.shape = pygame.Surface((20, 20))


pygame.init()

img_bg = pygame.image.load("square_game_images/retrowave.png")
window = pygame.display.set_mode((400, 400))
screen = pygame.Surface((400, 400))
my_font = pygame.font.SysFont('monospace', 40)

main_sq = MainSquare(20, (255, 255, 255))
needSide = random.randrange(6, 50, 2)
while needSide == main_sq.side:
    needSide = random.randrange(6, 50, 2)
need_sq = MainSquare(needSide, (0, 0, 0))

squares = []
player = pygame.Surface((20, 20))

win = False
done = False
while not win or not done:
    screen.blit(img_bg, (0, 0))
    if len(squares) < 10:
        squares.append(Square(squares))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
            main_sq.y += main_sq.speed
        if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
            main_sq.y -= main_sq.speed
        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            main_sq.x -= main_sq.speed
        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            main_sq.x += main_sq.speed

    pygame.draw.rect(screen, need_sq.color, ((main_sq.x, main_sq.y), (needSide, needSide)))
    pygame.draw.rect(screen, main_sq.color, ((main_sq.x, main_sq.y), (main_sq.side, main_sq.side)))
    if needSide < main_sq.side:
        pygame.draw.rect(screen, need_sq.color, ((main_sq.x, main_sq.y), (needSide, needSide)))

    for s in squares:
        pygame.draw.rect(screen, s.color, ((s.x, s.y), (s.side, s.side)))

    for s in squares:
        if inter(main_sq.x, main_sq.y, s.x, s.y, main_sq.side, s.side):
            s.x = 1000
            s.y = 1000
            if main_sq.side > s.side:
                main_sq.side -= 2
            elif main_sq.side < s.side:
                main_sq.side += 2
            squares.pop(squares.index(s))

    if win:
        string = my_font.render('!!!you won!!!', 5, (0, 255, 0))
        screen.blit(string, (50, 160))
        main_sq.x, main_sq.y = 1000, 1000
        if len(squares) > 8:
            for i in range(2):
                squares.pop(random.randrange(len(squares)))
    # pygame.display.flip()
    window.blit(screen, (0, 0))
    pygame.display.update()

    if main_sq.side == needSide:
        win = True

pygame.quit()
