import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Don't touch the floor")
screen.fill((0,0,0))

pygame.display.flip()

while True:
	pygame.event.pump()
	for evt in pygame.event.get():
		if evt.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE:
			pygame.quit()
			sys.exit()
			