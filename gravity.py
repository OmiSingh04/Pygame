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
    def __init__(self, x, y, vx, vy, radius):
        self.x = x
        self.y = y
        self.vy = vy
        self.vx = vx
        self.size = radius
        self.color = red

    def tick(self, x_acceleration, y_acceleration):
        
        self.vx += x_acceleration
        self.vy += y_acceleration

        self.x += self.vx
        self.y += self.vy
        
        if self.y >= screen_y or self.y <= 0:
           self.vy *= -1 
           self.vy -= 5/100*self.vy

        if self.x <= 0 or self.x >= screen_x:
            self.vx *= -1

    def display(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)



ball = Ball(100,100,0.3,0.01,20)

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
    
    screen.fill(black)
    y_acceleration = 0.01
    ball.tick(0,y_acceleration)
    y_acceleration -= 0.001
    ball.display()
    pygame.display.flip()
