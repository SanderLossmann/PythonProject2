#import pygame
#pygame.init()
#ekraani seaded
#screen=pygame.display.set_mode([640,480])
#pygame.display.set_caption("Harjutamine")
#screen.fill([204, 255, 204])

#lisame teksti
#font = pygame.font.Font(None, 30)
#text = font.render("Hello PyGame", True, [0,0,0])
#screen.blit(text, [200,200])

#gameover = False
#while not gameover:
  #  #mängu sulgemine ristist
 #   event = pygame.event.poll()
#    if event.type == pygame.QUIT:
 #       break

 #   pygame.display.flip()
#pygame.quit()


#import pygame
#pygame.init()
#ekraani seaded
#screen=pygame.display.set_mode([640,480])
#pygame.display.set_caption("Harjutamine")
#screen.fill([204, 255, 204])

#lisame teksti
#font = pygame.font.Font(pygame.font.match_font('arial'), 50)
#font.set_underline(True)
#text = font.render("Hello PyGame", True, [0,0,0])

#tekstikasti suurus
#text_width = text.get_rect().width
#text_height = text.get_rect().height

#screen.blit(text, [320-text_width/2,240-text_height/2])

#gameover = False
#while not gameover:
    #mängu sulgemine ristist
    #event = pygame.event.poll()
   # if event.type == pygame.QUIT:
  #      break

 #   pygame.display.flip()
#pygame.quit()


import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill([204, 255, 204])

#Lisame pildid
bg = pygame.image.load("img/bg.jpg")
screen.blit(bg,[0,0])
youWin = pygame.image.load("img/youwin.png")
youWin = pygame.transform.scale(youWin, [300, 120])
screen.blit(youWin,[180,100])

gameover = False
while not gameover:
    #mängu sulgemine ristist
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    pygame.display.flip()
pygame.quit()