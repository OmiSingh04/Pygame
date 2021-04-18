import pygame
import sys
import math

# taking inputs from the user to make an actual game
pygame.init()
screen_x = 1000
screen_y = 750
screen = pygame.display.set_mode((screen_x,screen_y))
color = (255,255,255)
screen.fill(color)
pygame.display.set_caption('Brick Breaker')

running = True

#Game objects
dimension = (100,30)
x_y = (400,470)


class Bar:
  def __init__(self, x, y, width, height):
  	self.rectangle = pygame.Rect(x,y,width,height)
  	self.color = (0,128,0)

  def display(self):
    pygame.draw.rect(screen, self.color, self.rectangle)

  def tick(self, x):
    self.rectangle.x =  self.rectangle.x + x
    if self.rectangle.x < -1:
      self.rectangle.x = self.rectangle.x + 1
    elif self.rectangle.x + self.rectangle.width > screen_x + 1:
      self.rectangle.x = self.rectangle.x - 1


class Ball:

  def __init__(self, x, y, vx, vy, radius):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
    self.size = radius
    self.color = (0,0,139)

  def tick(self, bar):
  	self.x += self.vx
  	self.y += self.vy

  	if self.x <=0 or self.x >= screen_x:
  	  self.vx *= -1
  	elif self.y <=0:
  	  self.vy *= -1
  	elif self.y >= screen_y:
  	  print("you lost :O")
  	  pygame.quit()
  	  sys.exit()


  	if self.x - self.size >= bar.rectangle.x and self.x + self.size <= bar.rectangle.x + bar.rectangle.width:
  	  if self.y + self.size >= screen_y - screen_y/8:
  		  self.vy *= -1


  def display(self):
	  pygame.draw.circle(screen, self.color, (self.x, self.y),  self.size)


bar = Bar(400,screen_y - screen_y/8,120,20)
ball = Ball(450,300,1,-1,10)

while running:


  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_LEFT]:
  	bar.tick(-1)

  if pressed[pygame.K_RIGHT]:
  	bar.tick(1)

  ball.tick(bar)

  events = pygame.event.get()

  for event in events:
    if event.type == pygame.QUIT:
      running = False

  screen.fill(color)
  bar.display()
  ball.display()
  pygame.display.flip()

 
