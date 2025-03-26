import pygame
import random
pygame.init()

#värvid
Roheline = (153, 204, 0)
Punane = (255, 0, 0)
Must = (0, 0, 0)
Valge = (255, 255, 255)

#ekraani tekitamine
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ruudu pela")
screen.fill(Valge)
clock = pygame.time.Clock()


posX, posY = screenX / 2, screenY / 2
speedX, speedY = 0, 0
directionX, directionY = 0, 0


num_obstacles = 5
obstacles = []

#Ruutude tekitamine ekraanile
for _ in range(num_obstacles):
    width = random.randint(30, 60)
    height = random.randint(30, 60)
    x = random.randint(0, screenX - width)
    y = random.randint(0, screenY - height)
    obstacles.append(pygame.Rect(x, y, width, height))

def check_collision(rect, obstacles):
    for obstacle in obstacles:
        if rect.colliderect(obstacle):
            return True
    return False
#Mängu sulgemine ristist
gameover = False
while not gameover:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

#Ruudu liikuma panemine klaviatuuriga
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                directionX = "move_right"
            elif event.key == pygame.K_LEFT:
                directionX = "move_left"
            elif event.key == pygame.K_UP:
                directionY = "move_up"
            elif event.key == pygame.K_DOWN:
                directionY = "move_down"

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                directionX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                directionY = 0


    if directionX == "move_left":
        if posX > 0:
            posX -= 3
    elif directionX == "move_right":
        if posX + 30 < screenX:
            posX += 3
    if directionY == "move_up":
        if posY > 0:
            posY -= 3
    elif directionY == "move_down":
        if posY + 30 < screenY:
            posY += 3

    for obstacle in obstacles:
        pygame.draw.rect(screen, Must, obstacle)

    player_rect = pygame.Rect(posX, posY, 30, 30)
    if check_collision(player_rect, obstacles):
        pygame.draw.rect(screen, Punane, player_rect)
        pygame.display.flip()
        pygame.time.wait(1000)
        gameover = True

    if not gameover:
        pygame.draw.rect(screen, Roheline, player_rect)

    pygame.display.flip()
    screen.fill(Valge)

pygame.quit()
