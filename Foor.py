import pygame
pygame.init()

screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("Foor - Sander Lossmann")

#värvid
Punane = (255, 0, 0)
Kollane = (255, 255, 0)
Roheline = (0, 255, 0)
Must = (0, 0, 0)
Hall = (128, 128, 128)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(Must)

    #joonistame
    pygame.draw.rect(screen, Hall, [50, 50, 100, 247], 2)
    pygame.draw.circle(screen, Punane, [100, 100], 35, 35)
    pygame.draw.circle(screen, Kollane, [100, 175], 35, 35)
    pygame.draw.circle(screen, Roheline, [100, 250], 35, 35)

    pygame.display.flip()