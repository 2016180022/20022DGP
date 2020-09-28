#bullet
from pico2d import *
from gobj import *
import gfw_image

class Bullet:
    bullets = []
    dx = 1
    frame = 0
    count = 0

    def __init__(self, pos):
        self.image = gfw_image.load("sprite_simon.png")
        self.pos = pos

    def draw(self):
        x, y = self.pos
        sx = 33 + self.frame * 20
        self.image.clip_draw(sx, 275, 20, 10, x + 55, y, 30, 15)

    def update(self):
        x,y = self.pos
        x += 2
        x += self.dx
        self.count += 1
        acceleration = 3
        self.dx += acceleration
        if self.count % 2 != 0:
            self.frame = (self.frame + 1) % 9
        #else:
        if self.count > 9:
        	self.count = 0

        if x < -100 or x > get_canvas_width() + 100:
            Bullet.bullets.remove(self)

        self.pos = x, y
