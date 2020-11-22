#bullet
from pico2d import *
from gobj import *
import gfw

class Bullet:
    def __init__(self, pos):
        self.image = gfw.image.load(RES_DIR + 'sprite_simon_sfx.png')
        x, y = pos
        self.pos = x + 55, y + 5
        self.dx = 1
        self.frame = 0
        self.count = 0
        self.width = 20
        self.height = 8

    def draw(self):
        x, y = self.pos
        self.pos = x, y
        sx = self.frame * 20
        self.image.clip_draw(sx, 76, 20, 8, *self.pos, 30, 12)

    def update(self):
        x,y = self.pos
        x += 0.2
        x += self.dx
        self.count += 1
        acceleration = 0.2
        self.dx += acceleration
        if self.count % 2 != 0:
            self.frame = (self.frame + 1) % 9
        #else:
        if self.count > 9:
            self.count = 0

        if x < -100 or x > get_canvas_width() + 100:
            self.remove()

        self.pos = x, y

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        x, y = self.pos
        hw = self.width - 6
        hh = self.height
        return x - hw, y - hh, x + hw, y + hh