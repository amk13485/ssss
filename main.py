from pygame import *


#класс-родителель для других спрайтоы
class Gamesprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        #вызываем конструктор класса(Sprite):
        sprite_Sprite.__init__(self)
        #каждый спрайт должен хранить свойство image - изоброжение
        self.image = transform.scale(image.load(player_image),(size_x, size_y))


        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




class Player(GameSprite):
    #метод, в котором реализовано управление спрайтом по кнопке
        def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
            #вызываем конструктор класса (Sprite):
            GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)


            self.x_speed = player_x_speed
            self.y_speed = player_y_speed
        def update(self):
            '''перемещает персонажа, применяя текущую горизонтольную и вертикальную скорость'''
            #сначала движение по горизонтали
            if pacman.rect.x <= win_width-80 and pacman.x_speed > 0 or pacman.rect.x >= 0 and pacman.x_speed < 0:
                self.rect.x += self.x_speed
                #если зашли за стенку, то встанем вплотную к стене
                platforms_touched = sprite.spritecollide(self, barriers, False)
                if self-x_speed › 0: # идём направо, правый край персонажа - вплотную к левому краю стены
                    for p in platforms_touched:
                        self-rect.right = min(self.rect.right, p.rect.left) # если коснулись сразу нескольких, то про
                elif self.x_speed ‹ 0: # идем налево, ставим левый край персонажа вплотную к правому краю стены
                    for p in platforms_touched:
                        self.rect.left = max(self.rect.left, p.rect.right) # если коснулись нескольких стен, то левый
            if packman.rect.y <= win_height-80 and packman.y_speed › 0 or packman.rect.y ›= 0 and packman-y_speed ‹ €
                self.rect.y += self-y_speed
                # если зашли за стенку,то встанем вплотную к стене
                platforms_touched = sprite.spritecollide(self, barriers, False)
                if self-y_speed › 0: # идем вниз
                    for p in platforms_touched:
                        # Проверяем, какая из платформ снизу самая бысокая, выравниваемся по ней, запоминаем ее как с
                        self.rect.bottom = min(self.rect.bottom, p.rect.top)
                elif self-y_speed ‹ 0: # ude 66ерх
                    for p in platforms_touched:
                        self.rect.top = max(self.rect.top, p.rect.bottom) # выравниваем верхний край по нижним краям

