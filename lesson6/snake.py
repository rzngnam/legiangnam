import pygame
import random


width = 800
height = 600

#  tạo khung hiển thị game
display_surf = pygame.display.set_mode((width, height))

red = (250, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

fps = 20  # frame per second
fps_clock = pygame.time.Clock()


class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(display_surf, red, (self.x, self.y, 20, 20))


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
        for i in range(self.tail):
            self.body_x.append(20)
            self.body_y.append(20)

    def update(self, player_move, apple):

            for i in range(self.tail - 1, 0, -1):
                self.body_x[i] = self.body_x[i - 1]
                self.body_y[i] = self.body_y[i - 1]

            if player_move == 1 and self.old_dir != 'left':
                self.move_right()
                self.old_dir = 'right'

            if player_move == 2 and self.old_dir != 'right':
                self.move_left()
                self.old_dir = 'left'

            if player_move == 3 and self.old_dir != 'down':
                self.move_up()
                self.old_dir = 'up'

            if player_move == 4 and self.old_dir != 'up':
                self.move_down()
                self.old_dir = 'down'

            if self.body_x[0] == apple.x and self.body_y[0] == apple.y:
                self.tail += 1
                self.body_x.append(self.body_x[-1])  # Táo bị ăn => body dài ra
                self.body_y.append(self.body_y[-1])
                apple.x = random.randrange(20, 600, 20)
                apple.y = random.randrange(20, 600, 20)

    def move_right(self):
        self.body_x[0] += 20*self.speed

    def move_left(self):
        self.body_x[0] += -20*self.speed

    def move_up(self):
        self.body_y[0] += -20*self.speed

    def move_down(self):
        self.body_y[0] += 20*self.speed

    # def eat(self, apple):
    #
    #         return True
    #     else:
    #         return False

    def death(self):
        for i in range(self.tail):
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
                pygame.draw.rect(display_surf, (255, 242, 0), (self.body_x[0], self.body_y[0], 20, 20))
            else:
                pygame.draw.rect(display_surf, green, (self.body_x[i], self.body_y[i], 20, 20))


def main():
    pygame.init()
    running = True
    pygame.display.set_caption("Snake")
    player = Snake(20, 20, 4, 1, 1, 1)
    food = Apple(560, 400)
    player_move = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player_move = 1
                elif event.key == pygame.K_LEFT:
                    player_move = 2
                elif event.key == pygame.K_UP:
                    player_move = 3
                elif event.key == pygame.K_DOWN:
                    player_move = 4
        display_surf.fill(black)
        player.draw()
        food.draw()
        if player.hit_floor():
            exit()
        if player.hit_celling():
            exit()
        if player.hit_edge():
            exit()
        player.update(player_move, food)
        fps_clock.tick(10)
        pygame.display.update()


if __name__ == '__main__':
    main()
