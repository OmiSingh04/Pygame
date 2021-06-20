#MOVE IT!
import pygame
import random as rd

class Particle:
  def __init__(self, in_x, in_y, in_size):
    self.x = in_x
    self.y = in_y
    self.size = in_size
    self.colour = (255, 0, 0)

  def display(self):
    pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size)

screen_x = 900
screen_y = 600
screen = pygame.display.set_mode((screen_x,screen_y))
color = (0,0,139)
screen.fill(color)
pygame.display.set_caption('ball')

dx, dy = 130, 223
vx, vy = 0.5,0.5 #vectors that move the thing
particle = Particle(dx,dy,30)

running = True
while running:
  screen.fill(color)
  particle.x = dx
  particle.y = dy
  dx = dx + vx
  dy = dy + vy

  if dy > screen_y - particle.size or dy < particle.size:
    vy = vy * -1;
  if dx > screen_x - particle.size or dx < particle.size:
    vx = vx * -1;
  particle.display()
  pygame.display.flip()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
