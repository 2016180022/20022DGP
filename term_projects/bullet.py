#bullet
from pico2d import *
from gobj import *
import gfw

class Bullet:
    bullets = []
    dx = 1
    frame = 0
    count = 0

    def __init__(self, pos):
        self.image = gfw.image.load(RES_DIR + '/sprite_simon_sfx.png')
        self.pos = pos

    def draw(self):
        x, y = self.pos
        sx = self.frame * 20
        self.image.clip_draw(sx, 76, 20, 8, x + 55, y + 5, 30, 12)

    def update(self):
        x,y = self.pos
        x += 1
        x += self.dx
        self.count += 1
        acceleration = 1
        self.dx += acceleration
        if self.count % 2 != 0:
            self.frame = (self.frame + 1) % 9
        #else:
        if self.count > 9:
            self.count = 0

        if x < -100 or x > get_canvas_width() + 100:
            Bullet.bullets.remove(self)

        self.pos = x, y
