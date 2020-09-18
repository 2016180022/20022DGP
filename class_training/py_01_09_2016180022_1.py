#soccer team called by class boy
from pico2d import *
from random import randint as rand

class Grass:
	def __init__(self):
		self.image = load_image('grass.png')

	def draw(self):
		self.image.draw(400, 30)

class Boy:
	def __init__(self):
		self.x, self.y = rand(100, 700), 85
		self.frame = 0
		self.image = load_image('run_animation.png')

	def update(self):
		self.frame = rand(0, 7)
		self.x += 5

	def draw(self):
		self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

def handle_events():
	global running
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			running = False

open_canvas()
team = [Boy() for i in range(11)]
boy = Boy()
grass = Grass()

running = True

while (running):

	for boy in team:
		boy.update()

	clear_canvas()
	grass.draw()
	for boy in team:
		boy.draw()
	update_canvas()

	delay(0.05)
	handle_events()

close_canvas()