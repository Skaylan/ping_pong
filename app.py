import pygame, sys, random
from pygame.locals import *

WIDTH = 800
HEIGHT = 600
WHITE = (255,255,255)
BLACK = (0,0,0)


class Player(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 130))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)
        self.speed = 5


    def update(self, tecla_up, tecla_down):
        keys = pygame.key.get_pressed()


        if keys[tecla_up]:
            self.rect.centery -= self.speed
        if keys[tecla_down]:
            self.rect.centery += self.speed


        #MOVE LIMIT
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Ping-Pong')
    fps = pygame.time.Clock()
    font = pygame.font.SysFont("monospace", 26)


    #PLAYER 1
    player = Player(20, 70)
    player_splrites = pygame.sprite.Group()
    player_splrites.add(player)
    player_ponto = 0



    #PLAYER 2
    player2 = Player(WIDTH - 20, HEIGHT - 70)
    player2_sprites = pygame.sprite.Group()
    player2_sprites.add(player2)
    player2_ponto = 0


    #BALL
    ball = pygame.Rect(WIDTH / 2 - 15, HEIGHT / 2 - 15,30,30)
    ball_speed_x = 5
    ball_speed_y = 5
    

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()




        screen.fill(BLACK)
        pygame.draw.ellipse(screen, (255,255,255), ball)
        ball.x += ball_speed_x
        ball.y += ball_speed_y
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed_x *= -1

        if ball.colliderect(player2.rect) or ball.colliderect(player.rect):
            ball_speed_x *= -1

        if ball.right >= WIDTH:
            player_ponto += 1
        
        if ball.left <= 0:
            player2_ponto += 1

        player_splrites.draw(screen)
        player_splrites.update(K_w, K_s)

        player2_sprites.draw(screen)
        player2_sprites.update(K_UP, K_DOWN)

        player_pontos_label = font.render(f' {player2_ponto} ', 1, (255, 255, 255))
        screen.blit(player_pontos_label, (WIDTH / 2 , HEIGHT/ 2))
        dash = font.render('-', 1, (255,255,255))

        player2_pontos_label = font.render(f' {player_ponto} ', 1, (255, 255, 255))
        screen.blit(player2_pontos_label, (WIDTH / 2 - 30, HEIGHT/ 2 ))

        screen.blit(dash, (WIDTH /2 , HEIGHT/2))    



        fps.tick(60)
        pygame.display.flip()



main()