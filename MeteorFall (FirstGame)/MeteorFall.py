import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meteorfall")

BG = pygame.image.load("Background for Meteorfall.png")

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5

METR_WIDTH = 50
METR_HEIGHT = 50
METR_VEL = 3

FONT = pygame.font.SysFont("papyrus", 60)

def draw(player, elapsed_time, metrs):
    WIN.blit(BG,(0,0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "black")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, (69, 67, 73), player)

    for metr in metrs:
        pygame.draw.rect(WIN, "black", metr)


    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(500, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    metr_add_increment = 2000
    metr_count = 0

    metrs = []

    hit = False

    while run:
       metr_count += clock.tick(120)
       elapsed_time = time.time() - start_time
       
       if metr_count  > metr_add_increment:
           for _ in range(5):
               metr_x = random.randint(0, WIDTH - METR_WIDTH)
               metr = pygame.Rect(metr_x, -METR_HEIGHT, METR_WIDTH, METR_HEIGHT)
               metrs.append(metr)

           metr_add_increment = max(200, metr_add_increment - 50)
           metr_count = 0
       
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

       keys = pygame.key.get_pressed()
       if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
       if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

       for metr in metrs[:]:
           metr.y += METR_VEL
           if metr.y > HEIGHT:
               metrs.remove(metr)
           elif metr.y + metr.height >= player.y and metr.colliderect(player):
               metrs.remove(metr)
               hit = True
               break

       if hit:
            lost_text = FONT.render("YOU LOSE", 1, "red")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(5000)
            break

       draw(player, elapsed_time, metrs)

    pygame.quit()        

if __name__ == "__main__":
    main()