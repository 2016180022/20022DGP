import random
from pico2d import *

RES_DIR = './res'

class Stage:
    def __init__(self):
        self.image = load_image("background_demo.png")
    def draw(self):
        self.image.draw(450, 245, 1200, 400)
    def update(self):
        pass

def point_add(point1, point2):
	x1,y1 = point1
	x2,y2 = point2
	return x1+x2, y1+y2

def move_obj(obj):
	obj.pos = point_add(obj.pos, obj.delta)


if __name__ == "__main__":
	print("Running test code ^_^")
