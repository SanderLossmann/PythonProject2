import pygame
pygame.init()

screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ülesanne 2")
screen.fill([204, 255, 204])

bg = pygame.image.load("img/bg_shop.jpg")
screen.blit(bg,[0,0])
muua = pygame.image.load("img/seller.png")
muua = pygame.transform.scale(muua, [250, 300])
screen.blit(muua,[100,170])
chat = pygame.image.load("img/chat.png")
screen.blit(chat, [250,40])

font = pygame.font.Font(None, 27)
text = font.render("Tere, minu nimi on Sander", True, [255, 255, 255])
screen.blit(text, [280,140])

gameover = False
while not gameover:
    #mängu sulgemine ristist
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    pygame.display.flip()
pygame.quit()