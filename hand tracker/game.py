import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

FPS = 60
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
BALL_RADIUS = 10



class Paddle:
    VEL = 5

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, win):
        pygame.draw.rect(
            win, "white", (self.x, self.y, self.width, self.height))

    def move(self, direction=1):
        self.x = self.x + self.VEL * direction


class Ball:
    VEL = 5

    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_vel = 0
        self.y_vel = -self.VEL

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def set_vel(self, x_vel, y_vel):
        self.x_vel = x_vel
        self.y_vel = y_vel

    def draw(self, win):
        pygame.draw.circle(win, "white", (self.x, self.y), self.radius)


class Brick:
    def __init__(self, x, y, width, height, health, colors):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.max_health = health
        self.colors = colors
        self.color = colors[0]

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))

    def collide(self, ball):
        if not (ball.x <= self.x + self.width and ball.x >= self.x):
            return False
        if not (ball.y - ball.radius <= self.y + self.height):
            return False

        self.hit()
        ball.set_vel(ball.x_vel, ball.y_vel * -1)
        return True

    def hit(self):
        self.health -= 2
        

    @staticmethod
    def interpolate(color_a, color_b, t):
        # 'color_a' and 'color_b' are RGB tuples
        # 't' is a value between 0.0 and 1.0
        # this is a naive interpolation
        return tuple(int(a + (b - a) * t) for a, b in zip(color_a, color_b))


def draw(win, paddle, ball, bricks, lives):
    win.fill("black")
    paddle.draw(win)
    ball.draw(win)

    for brick in bricks:
        brick.draw(win)

    pygame.display.update()


def ball_collision(ball):
    if ball.x - BALL_RADIUS <= 0 or ball.x + BALL_RADIUS >= WIDTH:
        ball.set_vel(ball.x_vel * -1, ball.y_vel)
    if ball.y + BALL_RADIUS >= HEIGHT or ball.y - BALL_RADIUS <= 0:
        ball.set_vel(ball.x_vel, ball.y_vel * -1)


def ball_paddle_collision(ball, paddle):
    if not (ball.x <= paddle.x + paddle.width and ball.x >= paddle.x):
        return
    if not (ball.y + ball.radius >= paddle.y):
        return

    paddle_center = paddle.x + paddle.width/2
    distance_to_center = ball.x - paddle_center

    percent_width = distance_to_center / paddle.width
    angle = percent_width * 90
    angle_radians = math.radians(angle)

    x_vel = math.sin(angle_radians) * ball.VEL
    y_vel = math.cos(angle_radians) * ball.VEL * -1

    ball.set_vel(x_vel, y_vel)


def generate_bricks(rows, cols):
    gap = 2
    brick_width = WIDTH // cols - gap
    brick_height = 20

    bricks = []
    for row in range(rows):
        for col in range(cols):
            brick = Brick(col * brick_width + gap * col, row * brick_height +
                          gap * row, brick_width, brick_height, 2, [(0, 255, 0), (255, 0, 0)])
            bricks.append(brick)

    return bricks


def main():
    clock = pygame.time.Clock()

    paddle_x = WIDTH/2 - PADDLE_WIDTH/2
    paddle_y = HEIGHT - PADDLE_HEIGHT - 5
    paddle = Paddle(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT, "black")
    ball = Ball(WIDTH/2, paddle_y - BALL_RADIUS, BALL_RADIUS, "black")

    bricks = generate_bricks(3, 10)
    lives = 3

    def reset():
        paddle.x = paddle_x
        paddle.y = paddle_y
        ball.x = WIDTH/2
        ball.y = paddle_y - BALL_RADIUS




    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


        if event.type == pygame.MOUSEMOTION:
            mouse_x,mouse_y = event.pos
            if mouse_x<paddle.x:
                paddle.x -=40
            if mouse_x > paddle.x:
                paddle.x += 40
        ball.move()
        ball_collision(ball)
        ball_paddle_collision(ball, paddle)

        for brick in bricks[:]:
            brick.collide(ball)

            if brick.health <= 0:
                bricks.remove(brick)

        # lives check
        if ball.y + ball.radius >= HEIGHT:
            lives -= 1
            ball.x = paddle.x + paddle.width/2
            ball.y = paddle.y - BALL_RADIUS
            ball.set_vel(0, ball.VEL * -1)

        if lives <= 0:
            bricks = generate_bricks(3, 10)
            lives = 3
            reset() 

        if len(bricks) == 0:
            bricks = generate_bricks(3, 10)
            lives = 3
            reset()

        draw(win, paddle, ball, bricks, lives)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()