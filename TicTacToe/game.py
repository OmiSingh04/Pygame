import pygame
import sys

clock = pygame.time.Clock()

fps = 30

pygame.init()
running = True

print("Cross plays first")
player1 = input("Player1 (cross):")
player2 = input("Player2 (circle):")

screen_x = 840
screen_y = 840
screen = pygame.display.set_mode((screen_x,screen_y))

screen.fill((255, 255, 255))
#pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0,840,840), 15)
pygame.display.set_caption('TicTacToe')


#game assets
circle = pygame.image.load("circle.png")
cross = pygame.image.load("cross.png")


#game variables
gaps = 15
game_over = False
remaining_spaces = 9
switch = 0
a = [[0,0,0],
	 [0,0,0],
	 [0,0,0]]

#0 indicates blank
#1 indicates cross
#2 indicates circle

#basic functions for the game
def draw_lines():
	pygame.draw.line(screen, (0,0,0), (25 + 250, 0), (25 + 250, 840), 15)
	pygame.draw.line(screen, (0,0,0), (25 + 500, 0), (25 + 500, 840), 15)
	pygame.draw.line(screen, (0,0,0), (0,25 + 250),(840, 25 + 250), 15)
	pygame.draw.line(screen, (0,0,0), (0,25 + 500),(840, 25 + 500), 15)
	pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0,840,840), 15)


def render(gaps):
	for i in range(3):
		startY = gaps
		for j in range(3):
			startX = gaps
			if not a[i][j] == 0:	
				obj = cross if a[i][j] == 1 else circle
				screen.blit(obj, (startX + j*250, startY + i*250))
				if j == 0:
					startX += gaps
		if i == 0:
			startY += gaps


def check_win():#returns 0 if game is in progress, 1 if cross wins, 2 if circle wins
	#check diagonals
	if a[0][0] == a[1][1] == a[2][2]:
		return a[0][0]
	if a[0][2] == a[1][1] == a[2][0]:
		return a[0][2]

	#check verticals
	for i in range(3):
		if a[0][i] == a[1][i] == a[2][i]:
			return a[0][i]

	#check horizontals
	for j in range(3):
		if a[j][0] == a[j][1] == a[j][2]:
			return a[j][0]

	return 0

draw_lines()
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	if event.type == pygame.MOUSEBUTTONUP:
		(mouseX, mouseY) = pygame.mouse.get_pos()
		i = mouseY//280
		j = mouseX//280
		if not a[i][j] == 0:
			continue
		else:
			a[i][j] = 1 if switch == 0 else 2
			switch = 0 if switch == 1 else 1
			remaining_spaces -= 1
	render(gaps)

	flag = check_win()
	if flag == 1 or flag == 2:
		name = "cross" if flag == 1 else "circle"
		player = player1 if name == "cross" else player2
		print(f"{player} wins")
		pygame.quit()
		sys.exit()

	if remaining_spaces == 0:
		print("its a tie!")
		pygame.quit()
		sys.exit()

	pygame.display.flip()
	clock.tick(fps)
