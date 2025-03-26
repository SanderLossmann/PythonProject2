import pygame
pygame.init()

#värvid
IGreen = [153, 255, 153]

#Pildi loomine
screen = pygame.display.set_mode([640,480])
pygame.display.set_caption("Ralliauto mäng")
screen.fill(IGreen)


#Taustapildi lisamine
Rally = pygame.image.load("img/bg_rally.jpg")
Rally = pygame.transform.scale(Rally, [640, 480])

#Autode lisamine
punane_auto = pygame.image.load("img/f1_red.png")

sinine_auto = pygame.image.load("img/f1_blue.png")

posX, posY = 420, 100

PosX, PosY = 180, 0

speed = 0.2

Speed = 0.3


gameover = False

#Mängu sulgemine ristist
while not gameover:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameover = True

        screen.blit(Rally,[0,0])

        screen.blit(punane_auto, (300, 390))

        screen.blit(sinine_auto, (PosX, PosY))

        screen.blit(sinine_auto, (posX, posY))

        posY += Speed

        PosY += speed

        if PosY > 480:
                PosY = -sinine_auto.get_height()

        if posY > 480:
                posY = -sinine_auto.get_height()

        pygame.display.flip()

pygame.quit()