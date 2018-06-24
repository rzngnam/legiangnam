import pygame
import random


width = 800
height = 600

#  tạo khung hiển thị game
display_surf = pygame.display.set_mode((width, height))

red = (250, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)


fps_clock = pygame.time.Clock()

apple_img = pygame.image.load('apple.png').convert_alpha()
snake_body = pygame.image.load('snake body.png').convert_alpha()
snake_head = pygame.image.load('snkhead.jpg').convert_alpha()


class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        display_surf.blit(apple_img, (self.x, self.y))


class Snake:
    body_x = []   # body_x[0] và body_y[0] là head của rắn
    body_y = []

    def __init__(self, w, h, tail, speed, player_move, old_dir):
        self.w = w
        self.h = h
        self.tail = tail
        self.speed = speed
        self.old_dir = old_dir
        self.player_move = player_move
        self.img = pygame.image.load('snkhead.jpg').convert_alpha()
        for i in range(self.tail):
            self.body_x.append(20)
            self.body_y.append(20)

    def update(self, player_move, apple, scoreboard):

            for i in range(self.tail - 1, 0, -1):
                self.body_x[i] = self.body_x[i - 1]
                self.body_y[i] = self.body_y[i - 1]

            if player_move == 1:
                self.move_right()
                self.img = pygame.image.load('snkhead.jpg')

            if player_move == 2:
                self.move_left()
                self.img = pygame.transform.rotate(snake_head, 180)

            if player_move == 3:
                self.move_up()
                self.img = pygame.transform.rotate(snake_head, 90)

            if player_move == 4:
                self.move_down()
                self.img = pygame.transform.rotate(snake_head, -90)

            if self.body_x[0] == apple.x and self.body_y[0] == apple.y:
                self.tail += 1
                self.body_x.append(self.body_x[-1])  # Táo bị ăn => body dài ra
                self.body_y.append(self.body_y[-1])
                apple.x = random.randrange(20, 600, 20)
                apple.y = random.randrange(20, 600, 20)
                scoreboard.score += 1

    def move_right(self):
        self.body_x[0] += 20*self.speed

    def move_left(self):
        self.body_x[0] += -20*self.speed

    def move_up(self):
        self.body_y[0] += -20*self.speed

    def move_down(self):
        self.body_y[0] += 20*self.speed

    def death(self):
        for i in range(1, self.tail):
            if (self.body_x[0] == self.body_x[i]) and (self.body_y[0] == self.body_y[i]):
                return True
            else:
                return False

    def hit_celling(self):
        if self.body_y[0] < 0:
            return True
        else:
            return False

    def hit_floor(self):
        if self.body_y[0] == height:
            return True
        else:
            return False

    def hit_edge(self):
        if (self.body_x[0] < 0) or (self.body_x[0] > width):
            return True
        else:
            return False

    def draw(self):

        for i in range(self.tail):
            if i == 0:
                display_surf.blit(self.img, (self.body_x[0], self.body_y[0]))
            else:
                display_surf.blit(snake_body, (self.body_x[i], self.body_y[i]))


class ScoreBoard:
    def __init__(self, x, y, score, size):
        self.x = x
        self.y = y
        self.score = score
        self.size = size
        self.font = pygame.font.Font(None, self.size)

    def display(self):
        display_score = self.font.render(' Score : ' + str(self.score), True, (0, 0, 0))
        display_surf.blit(display_score, (self.x, self.y))


def main():
    pygame.init()
    running = True
    pygame.display.set_caption("Snake")
    player = Snake(20, 20, 3, 1, 1, 1)
    food = Apple(600, 400)
    scoreboard = ScoreBoard(500, 20, 0, 20)
    player_move = 0
    old_move = 0
    fps = 10  # frame per second
    flag = False

    while running:
        if player.hit_floor() or player.hit_edge() or player.hit_celling():
            display_surf.fill((0, 0, 0))
            font = pygame.font.Font(None, 100)
            gameover = font.render(' Game over ', True, (255, 255, 255))
            display_surf.blit(gameover, (width / 2 - 200, height / 2 - 50))
            pygame.display.update()
            if pygame.event.get() == pygame.QUIT:
                flag = True
                break
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and old_move != 2:
                        player_move = 1
                        old_move = 1
                    elif event.key == pygame.K_LEFT and old_move != 1:
                        player_move = 2
                        old_move = 2
                    elif event.key == pygame.K_UP and old_move != 4:
                        player_move = 3
                        old_move = 3
                    elif event.key == pygame.K_DOWN and old_move != 3:
                        player_move = 4
                        old_move = 4
            if flag:
                break
            display_surf.fill((214, 225, 147))
            player.draw()
            food.display()
            scoreboard.display()

            player.update(player_move, food, scoreboard)
            fps_clock.tick(fps)
            pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
