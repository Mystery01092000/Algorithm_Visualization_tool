import pygame
import sys


pygame.font.init()

# Total window
screen = pygame.display.set_mode(
    (900, 650)
)

# Title and Icon
pygame.display.set_caption("SORTING VISUALISER")


color = (255, 255, 255)


color_light = (0, 0, 0)


color_dark = (100, 100, 100)

width = 900

height = 600


smallfont = pygame.font.SysFont('Corbel', 40)


text = smallfont.render('quit', True, color)
# while True:
#
#     for ev in pygame.event.get():
#
#         if ev.type == pygame.QUIT:
#             pygame.quit()
#
#
#         if ev.type == pygame.MOUSEBUTTONDOWN:
#
#             if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
#                 pygame.quit()
#
#     screen.fill((0, 0, 60))
#
#     mouse = pygame.mouse.get_pos()
#
#     if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
#         pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])
#
#     else:
#         pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])
#
#     screen.blit(text, (width / 2 + 50, height / 2))
#
#     pygame.display.update()