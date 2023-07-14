import pygame
pygame.init()

width = 1000
height = 2200
screen_res = (width, height)
pygame.display.set_caption("Bouncing game")
screen = pygame.display.set_mode(screen_res)

red = (255, 0, 0)
black = (0, 0, 0)

ball_obj = pygame.draw.circle(
	surface=screen, color=red, center=[100, 100], radius=40)
speed = [4, 4]

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	screen.fill(black)

	ball_obj = ball_obj.move(speed)
	if ball_obj.left <= 0 or ball_obj.right >= width:
		speed[0] = -speed[0]
	if ball_obj.top <= 0 or ball_obj.bottom >= height:
		speed[1] = -speed[1]

	pygame.draw.circle(surface=screen, color=red,
					center=ball_obj.center, radius=40)

	pygame.display.flip()