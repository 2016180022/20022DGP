#move character with key
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

#esc handle event
def handle_events():
	global running
	global dir
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN:
			if event.key == SDLK_ESCAPE:
				running = False
			elif event.key == SDLK_RIGHT:
				dir += 1
			elif event.key == SDLK_LEFT:
				dir -= 1
		elif event.type == SDL_KEYUP:
			if event.key == SDLK_RIGHT:
				dir -= 1
			elif event.key == SDLK_LEFT:
				dir += 1

running = True
x = 800//2
dir = 0
frame = 0
while (x < 800 and running):
	clear_canvas()
	grass.draw(400, 30)
	character.clip_draw(frame * 100, 0, 100, 100, x, 85)
	update_canvas()
	frame = (frame + 1) % 8
	x += dir * 5
	delay(0.01)
	handle_events()

close_canvas()