import pygame, sys

pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)
clock = pygame.time.Clock()

# graafika laadimine
ball = pygame.image.load("img/ball.png")

# kiirus ja asukoht
posX, posY = 0, 0
speedX = 3

gameover = False
while not gameover:
    # fps
    clock.tick(60)

    # mängu sulgemine ristist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Kui on akna sulgemine
            gameover = True  # Seadistame mängu lõppemise
            pygame.quit()  # Lõpetame Pygame
            sys.exit()  # Sulgeme programmi

    # pildi lisamine ekraanile
    screen.blit(ball, (posX, posY))

    posX += speedX

    # graafika kuvamine ekraanil
    pygame.display.flip()
    screen.fill(lBlue)

pygame.quit()