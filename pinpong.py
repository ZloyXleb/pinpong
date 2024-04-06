from pygame import *
from random import randint


font.init()
font1 = font.SysFont('Arial', 70)

my_win = display.set_mode((700, 500))
display.set_caption('пин-понг')
fon = transform.scale(image.load('stol.webp'), (700, 500))



class GameSprite(sprite.Sprite):
    def __init__(self, p_image, x, y, w, h, speed):
        super().__init__()
        self.speed = speed
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(p_image), (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        my_win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def updateL(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_p] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_l] and self.rect.y < 450:
            self.rect.y += self.speed
    def updateR(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
    




            

l_p = Player('raketka.png', 0, 200, 50, 150, 4)
r_p = Player('raketka.png', 650, 200, 50, 150, 4)



win = font1.render('You win!', True, (100, 255, 100))
lose = font1.render('You lose!', True, (255, 100, 100))

finich = False







lost = 0
score = 0
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        '''if e.type == MOUSEBUTTONDOWN and e.button == 1:
            if num_fire < 5 and realding == False:
                num_fire += 1
                mause.fire()
            if num_fire >= 5 and realding == False:
                last_time = timer()
                realding = True'''


    my_win.blit(fon, (0, 0))
    l_p.updateL()
    r_p.updateR()
    l_p.reset()
    r_p.reset()
    
    clock.tick(60)
    display.update()
