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
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
    def updateR(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_p] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_l] and self.rect.y < 450:
            self.rect.y += self.speed
    




            
m_p = GameSprite('ball.png', 350, 250, 30, 30, 3)
l_p = Player('raketka.png', 0, 200, 50, 150, 4)
r_p = Player('raketka.png', 650, 200, 50, 150, 4)



winl = font1.render('Win left player!', True, (100, 255, 100))
winr = font1.render('Win right player!', True, (100, 255, 100))

finich = False






speed_x = 3
speed_y = 3
lost = 0
score = 0
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finich != True:
            
        m_p.rect.x += speed_x
        m_p.rect.y += speed_y

        if m_p.rect.y < 0 or m_p.rect.y > 470:
            speed_y *= -1
        if sprite.collide_rect(l_p, m_p) or sprite.collide_rect(r_p, m_p):
            speed_x *= -1
            speed_y *= -1
        
        
      

        my_win.blit(fon, (0, 0))
        l_p.updateL()
        r_p.updateR()
        l_p.reset()
        r_p.reset()
        m_p.update()
        m_p.reset()


        if m_p.rect.x > 700:
            my_win.blit(winl, (150, 250))
            finich = True

        if m_p.rect.x < 0:
            my_win.blit(winr, (150, 250))
            finich = True
    

    clock.tick(60)
    display.update()

display.update()