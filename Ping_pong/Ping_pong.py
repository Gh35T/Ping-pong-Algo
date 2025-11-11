from pygame import *
from random import randint
init()
font.init()
font = font.SysFont('Arial', 35)
lose1_text = font.render('PLAYER 1 LOSE!', True, (180, 20, 20))
lose2_text = font.render('PLAYER 2 LOSE!', True, (180, 20, 20))
# Параметры окна
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Пинг понг")
# Цвет фона
back = (160, 220, 100)
# Конструктор класса
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
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

# Создание ракетов и мяча
racket1 = Player('racket.png', 30, 200, 40, 150, 5)
racket2 = Player('racket.png', win_width - 70, 200, 40, 150, 5)
ball = GameSprite('tenis_ball.png', 350, 250, 50, 50, 0)
game = True
finish = False
clock = time.Clock()
FPS = 60
speed_x = 3
speed_y = 3
# Счет
score1 = 0
score2 = 0
#Игровой цикл
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        # Отскок от границ поля
        if ball.rect.y <= 0 or ball.rect.y >= win_height - 50:
            speed_y *= -1
        # Отскок от ракеток
        if sprite.collide_rect(ball, racket1) or sprite.collide_rect(ball, racket2):
            speed_x *= -1
            speed_y += randint(-1, 1)
        #Проверка был ли гол
        if ball.rect.x < 0:
            score2 += 1
            ball.rect.x = 350
            ball.rect.y = 250
            speed_x = 3 * (-1 if randint(0, 1) else 1)
            speed_y = 3 * (-1 if randint(0, 1) else 1)
        
        if ball.rect.x > win_width:
            score1 += 1
            ball.rect.x = 350
            ball.rect.y = 250
            speed_x = 3 * (-1 if randint(0, 1) else 1)
            speed_y = 3 * (-1 if randint(0, 1) else 1)
        
        # Проверка условий победы
        if score1 >= 5:
            finish = True
            win_text = font.render('LEFT PLAYER WINS!', True, (180, 20, 20))
            window.blit(win_text, (250, 250))
        
        if score2 >= 5:
            finish = True
            win_text = font.render('RIGHT PLAYER WINS!', True, (180, 20, 20))
            window.blit(win_text, (250, 250))
        
        # Отображение счета
        score_display = font.render(f'{score1} - {score2}', True, (50, 50, 150))
        window.blit(score_display, (320, 20))
        
        # Отрисовка объектов
        racket1.reset()
        racket2.reset()
        ball.reset()
    
    display.update()
    clock.tick(FPS)

quit()
