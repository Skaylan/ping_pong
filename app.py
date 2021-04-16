import pygame, sys, random
from pygame.locals import *

WIDTH = 1000
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
        self.speed = 7


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


def reset_ball():
    global ball_speed_x, ball_speed_y, timer

    ball.center = WIDTH/2, HEIGHT/2
    current_time = pygame.time.get_ticks()

    if current_time - timer < 2000:
        ball_speed_x = 0
        ball_speed_y = 0
    else:
        ball_speed_x = 7 * random.choice((1, -1))
        ball_speed_y = 7 * random.choice((1, -1))
        timer = None

def ball_logic():
    global ball_speed_x, ball_speed_y, player2_ponto, player_ponto, timer
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    if ball.colliderect(player2.rect) or ball.colliderect(player.rect):
        ball_speed_x *= -1

    if ball.right >= WIDTH:
        player2_ponto += 1
        timer = pygame.time.get_ticks()
        
    if ball.left <= 0:
        player_ponto += 1
        timer = pygame.time.get_ticks()

def main():
    global ball, ball_speed_x, ball_speed_y, timer, player, player2, player2_ponto, player_ponto
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Ping-Pong')
    fps = pygame.time.Clock()
    font = pygame.font.SysFont("monospace", 26)
    timer = None

    #PLAYER 1
    player = Player(10, HEIGHT/2)
    player_splrites = pygame.sprite.Group()
    player_splrites.add(player)
    player_ponto = 0



    #PLAYER 2
    player2 = Player(WIDTH - 10, HEIGHT / 2)
    player2_sprites = pygame.sprite.Group()
    player2_sprites.add(player2)
    player2_ponto = 0


    # #LINHA
    # linha = pygame.Rect(WIDTH / 2, 0, 5, HEIGHT)

    #BALL
    ball = pygame.Rect(WIDTH / 2 - 15, HEIGHT / 2 - 15,30,30)
    ball_speed_x = 7
    ball_speed_y = 7
    
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()




        screen.fill(BLACK)
        pygame.draw.aaline(screen, WHITE, (WIDTH / 2, 0), (WIDTH/2, HEIGHT), 5)
        pygame.draw.ellipse(screen, (255,255,255), ball)
        ball_logic()
            
            

        player_splrites.draw(screen)
        player_splrites.update(K_w, K_s)

        player2_sprites.draw(screen)
        player2_sprites.update(K_UP, K_DOWN)

        player_pontos_label = font.render(f' {player2_ponto} ', 1, (255, 255, 255))
        screen.blit(player_pontos_label, (WIDTH / 2 - 45 , HEIGHT/ 2))


        player2_pontos_label = font.render(f' {player_ponto} ', 1, (255, 255, 0))
        screen.blit(player2_pontos_label, (WIDTH / 2 , HEIGHT/ 2 ))
  

        if timer:
            reset_ball()

        fps.tick(60)
        pygame.display.flip()





def menu():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Ping-Pong')
    fps = pygame.time.Clock()
    font = pygame.font.SysFont("monospace", 26)

    button = pygame.Rect(WIDTH/2 - 50, HEIGHT/2, 100, 50)

    

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if button.collidepoint(mouse_pos):
                    main()

        start_label = font.render('START', 1, (255,255,0))

        screen.fill(BLACK)
        pygame.draw.rect(screen, (255,0,0), button)
        screen.blit(start_label, (WIDTH/2 - 40, HEIGHT/2 + 10))
        fps.tick(60)
        pygame.display.flip()




menu()