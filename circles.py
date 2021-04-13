import pygame
import random as rd

class Particle:
  def __init__(self, in_x, in_y, in_size):
    self.x = in_x
    self.y = in_y
    self.size = in_size
    self.colour = (255, 0, 0)
    self.thickness = 3

  def display(self):
    pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

screen = pygame.display.set_mode((900,600))
color = (255,255,255)
screen.fill(color)
pygame.display.set_caption('ball')
pygame.display.flip()

particles = []
for i in range(30):
	size = rd.randint(20,50)
	x = rd.randint(size,900-size)
	y = rd.randint(size,600-size)
	particles.append(Particle(x,y,size))

for each in particles:
  each.display()

pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False