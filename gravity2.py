import pygame
import sys
pygame.init()
screen_x = 1000
screen_y = 750
screen = pygame.display.set_mode((screen_x, screen_y))
running = True

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,255,0)
green = (0,0,255)

screen.fill(black)
pygame.display.set_caption('Gravity')


class Ball:
    def __init__(self, x, y, vx, vy, size):
        self.x = x
        self.y = y
        self.radius = size
        self.vx = vx
        self.vy = vy
        self.height = self.y
        self.ay = 0.01
        self.ax = 0

    def tick(self):
        self.vx += self.ax
        self.vy += self.ay

        self.x += self.vx
        self.y += self.vy

        if self.y + self.radius >= screen_y:
            self.vy -= 0.05 * self.vy
            self.vy *= -1
        
        if self.x + self.radius >= screen_x or self.x - self.radius <= 0:
            self.ax *= -1
            self.vx -= 0.05 * self.vx
            self.vx *= -1



    def display(self):
        pygame.draw.circle(screen,blue, (self.x, self.y), self.radius)


ball = Ball(screen_x/2, 40,1,0, 20)


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_SPACE]:
        running = False
        pygame.quit()
        sys.exit()

    screen.fill(white)
    ball.tick()
    ball.display()
    pygame.display.flip()

