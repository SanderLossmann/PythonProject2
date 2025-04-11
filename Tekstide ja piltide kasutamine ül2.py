import pygame
pygame.init()

screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ülesanne 2")
screen.fill([204, 255, 204])

bg = pygame.image.load("img/bg_shop.jpg")
screen.blit(bg,[0,0])
muua = pygame.image.load("img/seller.png")
muua = pygame.transform.scale(muua, [250, 305])
screen.blit(muua,[105,160])
chat = pygame.image.load("img/chat.png")
chat = pygame.transform.scale(chat, [250,210])
screen.blit(chat, [250,65])

font = pygame.font.Font(None, 25)
text = font.render("Tere, minu nimi on Sander", True, [255, 255, 255])
screen.blit(text, [265,150])

gameover = False
while not gameover:
    #mängu sulgemine ristist
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    pygame.display.flip()
pygame.quit()