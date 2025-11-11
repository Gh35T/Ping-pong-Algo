from pygame import *
from random import randint

font.init()
font = font.SysFont('Arial', 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 20, 20))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 20, 20))

window = display.set_mode((700,600))
display.set_caption("Пинг понг")
#конструктор класса
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #отрисовка героя
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
back = (160, 220, 100)

win_width = 800
win_height = 600
window = display.set_mode((win_width, win_height))
window.fill(back)
game = True
finish = False
clock = time.Clock()
FPS = 60
speed_x = randint(1,3)
speed_y = randint(1,3)
lose1 = 0
lose2 = 0
loses = font.render(str(lose1) + ' - ' + str(lose2), True, (180,25,25))
racket1 = Player('racket.png', 50,200,40,150,5)
racket2 = Player('racket.png',700,200,40,150,5)
ball = GameSprite('tenis_ball.png',400,300,50,50,20)

while game:
    for o in event.get():
        if o.type == QUIT:
            game = False
    if not finish:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.x <0:
        lose1 = lose1 + 1
        ball = GameSprite('tennis_ball.png',400,300,50,50,20)
    if ball.rect.x >= win_width - 50:
        lose2 = lose2 + 1
        ball = GameSprite('tennis_ball.png',400,300,50,50,20)
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
    if ball.rect.x > win_width-50 or ball.rect.x < 0:
            speed_x *= -1
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= 1
    loses = font.render(str(lose1) + ' - ' + str(lose2), True, (180, 25, 25))
    window.blit(loses, (300,25))
    racket1.reset()
    racket2.reset()
    ball.reset()
    display.update()
    clock.tick(FPS)