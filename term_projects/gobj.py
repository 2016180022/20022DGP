import random
from pico2d import *

#RES_DIR = '../res'

class Stage:
    def __init__(self):
        self.image = load_image("background_demo.png")
    def draw(self):
        self.image.draw(450, 245, 1200, 400)
    def update(self):
        pass


if __name__ == "__main__":
	print("Running test code ^_^")
